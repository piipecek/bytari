from flask import Blueprint, render_template, request, redirect, url_for
import json
from pathlib import Path

pozvanky = Path('pozvanky.json')

api = Blueprint("api",__name__)

@api.route("/pozvanky")
def get_pozvanky() -> dict:
    with pozvanky.open() as f:
        return json.dumps(json.load(f))