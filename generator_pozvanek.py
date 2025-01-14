# vygeneruje pozvanky, pokud jeste neexistuji.

from pathlib import Path
import json

pozvanky_path = Path.cwd() / 'pozvanky.json'
triplety_path = Path.cwd() / "kody" / 'triplets.txt'

pozvanky = []
triplety = []
with open(triplety_path, 'r') as t:
    triplety = t.readlines()
    

if not pozvanky_path.exists():
    for i, triplet in enumerate(triplety):
        pozvanka = {
            "id": i,
            "kod": triplet.strip().replace("\n", "").replace(",", "").replace(" ", ""),
            "jmeno": "",
            "email": "",
            "datum": "",
            "cas": "",
            "doba": "",
            "odemcena": True,
            "prespat": False,
            "kdo": [],
            "poznamka": ""
        }
        pozvanky.append(pozvanka)

    with open(pozvanky_path, 'w') as p:
        p.write(json.dumps(pozvanky, indent=4))