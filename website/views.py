from flask import Blueprint, render_template, request, redirect, url_for, session
from .pozvanky_handling import vynulovat_by_id, toggle_zamknuti_by_id, get_pozvanky, existuje_kod_zdrcnuty, save_pozvanky, get_pozvanka_by_kod, update_pozvanka
from .volno_handling import ulozit_nove_volno, delete_volno_by_id
import json
from .mail_handler import mail_sender
import os


views = Blueprint("views",__name__)

def sanitize_kod(kod):
    kod = kod.replace(" ", "")
    kod = kod.replace(",", "")
    kod = kod.replace(".", "")
    kod = kod.replace("-", "")
    kod = kod.replace("_", "")
    kod = kod.replace(";", "")
    kod = kod.replace(":", "")
    kod = kod.strip()
    kod = kod.lower()
    
    return kod
    


@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        kod = request.form.get("kod")
        kod = sanitize_kod(kod)
        pozvanka = get_pozvanka_by_kod(kod)
        if pozvanka:
            if pozvanka["odemcena"]:
                pozvanka["jmeno"] = request.form.get("jmeno")
                pozvanka["email"] = request.form.get("email")
                update_pozvanka(pozvanka)
                return redirect(url_for("views.vybrat_cloveka", kod=kod))
            else:
                return redirect(url_for("views.summary", kod=kod))
        else:
            return redirect(url_for("views.wrong_code"))
            

@views.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "GET":
        return render_template("admin.html")
    
    if request.method == "POST":
        if id := request.form.get("vynulovat"):
            vynulovat_by_id(int(id))
        elif id := request.form.get("toggle"):
            toggle_zamknuti_by_id(int(id))
        
    return redirect(url_for("views.admin"))

@views.route("/dostupnost", methods=["GET", "POST"])
def dostupnost():
    if request.method == "GET":
        return render_template("dostupnost.html")
    else:
        if id := request.form.get("smazat"):
            delete_volno_by_id(int(id))
        else:
            data = request.form.get("data")
            data = json.loads(data)
            for zaznam in data["dates"]:
                ulozit_nove_volno(data["name"], zaznam["date"], zaznam["start"], zaznam["end"])
        return redirect(url_for("views.dostupnost"))

@views.route("/wrong_code")
def wrong_code():
    return render_template("wrong_code.html")

@views.route("/vybrat_cloveka/<string:kod>", methods=["GET", "POST"])
def vybrat_cloveka(kod):
    if request.method == "GET":
        pozvanka = get_pozvanka_by_kod(kod)
        if pozvanka:
            if pozvanka["odemcena"]:
                return render_template("vybrat_cloveka.html")
            else:
                return redirect(url_for("views.summary", kod=kod))
        else:
            return redirect(url_for("views.wrong_code"))
    else:
        lidi = []
        if (request.form.get("Jenda")):
            lidi.append("Jenda")
        if (request.form.get("Kuba")):
            lidi.append("Kuba")
        if (request.form.get("Marek")):
            lidi.append("Marek")
        if (request.form.get("Rocco")):
            lidi.append("Rocco")
            
        if len(lidi) == 0:
            return redirect(url_for("views.vybrat_cloveka", kod=kod))
            
        session["lidi"] = lidi
        pozvanka = get_pozvanka_by_kod(kod)
        pozvanka["kdo"] = lidi
        update_pozvanka(pozvanka)
        return redirect(url_for("views.vybrat_termin", kod=kod))

@views.route("/vybrat_termin/<string:kod>", methods=["GET", "POST"])
def vybrat_termin(kod):
    if request.method == "GET":
        pozvanka = get_pozvanka_by_kod(kod)
        if pozvanka:
            if pozvanka["odemcena"]:
                lidi = session.get("lidi")
                lidi_pretty = []
                if "Jenda" in lidi:
                    lidi_pretty.append("Jendou")
                if "Kuba" in lidi:
                    lidi_pretty.append("Kubou")
                if "Marek" in lidi:
                    lidi_pretty.append("Markem")
                if "Rocco" in lidi:
                    lidi_pretty.append("Roccem")
                if (len(lidi) == 1):
                    pretty_string = lidi_pretty[0]
                else:
                    pretty_string = ", ".join(lidi_pretty[:-1]) + " a " + lidi_pretty[-1]
                return render_template("vybrat_termin.html", lidi=json.dumps(lidi), lidi_pretty=pretty_string)
            else:
                return redirect(url_for("views.summary", kod=kod))
        else:
            return redirect(url_for("views.wrong_code"))
        
    else:
        pozvanka = get_pozvanka_by_kod(kod)
        pozvanka["datum"] = request.form.get("datum")
        pozvanka["doba"] = request.form.get("doba")
        pozvanka["cas"] = request.form.get("kdy")
        pozvanka["prespat"] = request.form.get("prespat") == "on"
        pozvanka["odemcena"] = False
        pozvanka["poznamka"] = request.form.get("poznamka")
        update_pozvanka(pozvanka)
        
        mail_sender("tva_rezervace", pozvanka["email"], data=kod)
        mail_sender("nova_rezervace", os.environ.get("MAIL_USERNAME"), data=pozvanka["jmeno"]) 
        
        return redirect(url_for("views.summary", kod=kod))

@views.route("/summary/<string:kod>")
def summary(kod):
    pozvanka = get_pozvanka_by_kod(kod)
    if pozvanka:
        koho_potkam_list = []
        if "Jenda" in pozvanka["kdo"]:
            koho_potkam_list.append("Jendu")
        if "Kuba" in pozvanka["kdo"]:
            koho_potkam_list.append("Kubu")
        if "Marek" in pozvanka["kdo"]:
            koho_potkam_list.append("Marka")
        if "Rocco" in pozvanka["kdo"]:
            koho_potkam_list.append("Rocca")
        if len(koho_potkam_list) == 1:
            koho_potkam = koho_potkam_list[0]
        else:
            koho_potkam = ", ".join(koho_potkam_list[:-1]) + " a " + koho_potkam_list[-1] 
        prespani = "Ano" if pozvanka["prespat"] else "Ne"
        return render_template("summary.html", pozvanka=pozvanka, koho_potkam=koho_potkam, prespani=prespani)
    else:
        return redirect(url_for("views.wrong_code"))
        
        