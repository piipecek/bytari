import json
from pathlib import Path

pozvanky_path = Path('pozvanky.json')

def get_pozvanky() -> dict:
    with pozvanky_path.open() as f:
        return json.load(f)

def vynulovat_by_id(id_: int) -> None:
    pozvanky = get_pozvanky()
    for pozvanka in pozvanky:
        if pozvanka["id"] == id_:
            pozvanka["jmeno"] = ""
            pozvanka["cislo"] = ""
            pozvanka["datum"] = ""
            pozvanka["doba"] = ""
            pozvanka["odemcena"] = True
    
    with pozvanky_path.open("w") as f:
        json.dump(pozvanky, f)

def toggle_zamknuti_by_id(id_: int) -> None:
    pozvanky = get_pozvanky()
    for pozvanka in pozvanky:
        if pozvanka["id"] == id_:
            pozvanka["odemcena"] = not pozvanka["odemcena"]
    
    with pozvanky_path.open("w") as f:
        json.dump(pozvanky, f)