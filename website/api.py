from flask import Blueprint, render_template, request, redirect, url_for
import json
from pathlib import Path
from .volno_handling import get_volno, get_casova_okna_pro_lidi, volna_for_admin
from .pozvanky_handling import get_pozvanky

pozvanky = Path('pozvanky.json')
volno = Path('volno.json')

api = Blueprint("api",__name__)

@api.route("/pozvanky")
def get_pozvanky_js():
    pozvanky = get_pozvanky()
    for pozvanka in pozvanky:
        pozvanka["kdo"] = ", ".join(pozvanka["kdo"])
        pozvanka["prespat"] = "Ano" if pozvanka["prespat"] else "Ne"
        pozvanka["odemcena"] = "Ano" if pozvanka["odemcena"] else "Ne"
    return json.dumps(pozvanky)
    
@api.route("/volna")
def get_volna():
    return json.dumps(volna_for_admin())

@api.route("/terminy/<string:lidi>")
def get_terminy(lidi):
    lidi = json.loads(lidi)
    volna = get_casova_okna_pro_lidi(lidi)
    return json.dumps(volna)