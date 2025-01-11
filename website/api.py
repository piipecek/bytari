from flask import Blueprint, render_template, request, redirect, url_for
import json
from pathlib import Path

pozvanky = Path('pozvanky.json')
volno = Path('volno.json')

api = Blueprint("api",__name__)

@api.route("/pozvanky")
def get_pozvanky():
    with pozvanky.open() as f:
        return json.dumps(json.load(f))
    
@api.route("/volna")
def get_volno():
    with volno.open() as f:
        volno_list = json.load(f)
        volno_list.sort(key=lambda x: (x["jmeno"], x["start"]))
        return json.dumps(volno_list)