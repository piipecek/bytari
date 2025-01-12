import json
from pathlib import Path

pozvanky_path = Path('pozvanky.json')

def get_pozvanky() -> dict:
    with pozvanky_path.open() as f:
        return json.load(f)

def get_pozvanka_by_kod(kod: str) -> dict:
    kod = kod.replace(",", "").replace(" ", "").strip()
    pozvanky = get_pozvanky()
    for pozvanka in pozvanky:
        if pozvanka["kod"] == kod:
            return pozvanka
    return None

def update_pozvanka(pozvanka: dict) -> None:
    pozvanky = get_pozvanky()
    for i, p in enumerate(pozvanky):
        if p["kod"] == pozvanka["kod"]:
            pozvanky[i] = pozvanka
            break
    save_pozvanky(pozvanky)

def vynulovat_by_id(id_: int) -> None:
    pozvanky = get_pozvanky()
    for pozvanka in pozvanky:
        if pozvanka["id"] == id_:
            pozvanka["jmeno"] = ""
            pozvanka["cislo"] = ""
            pozvanka["datum"] = ""
            pozvanka["doba"] = ""
            pozvanka["odemcena"] = True
            pozvanka["kdo"] = []
            pozvanka["cas"] = ""
            pozvanka["prespat"] = False
    
    save_pozvanky(pozvanky)

def toggle_zamknuti_by_id(id_: int) -> None:
    pozvanky = get_pozvanky()
    for pozvanka in pozvanky:
        if pozvanka["id"] == id_:
            pozvanka["odemcena"] = not pozvanka["odemcena"]
    
    save_pozvanky(pozvanky)

def save_pozvanky(pozvanky: dict) -> None:
    with pozvanky_path.open("w") as f:
        json.dump(pozvanky, f, indent=4)

def existuje_kod_zdrcnuty(kod: str) -> bool:
    pozvanky = get_pozvanky()
    for pozvanka in pozvanky:
        if pozvanka["kod"].replace(", ", "") == kod:
            return True
    return False