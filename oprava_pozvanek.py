# single time, kdy koody poozvanek zdrcavam


from pathlib import Path
import json

pozvanky_path = Path.cwd() / 'pozvanky.json'

with pozvanky_path.open() as f:
    pozvanky = json.load(f)
    for pozvanka in pozvanky:
        pozvanka["kod"] = pozvanka["kod"].replace(", ", "").strip()
        pozvanka["kdo"] = []
        pozvanka["cas"] = ""
        pozvanka["prespat"] = False
    
with pozvanky_path.open("w") as f:
    json.dump(pozvanky, f, indent=4)