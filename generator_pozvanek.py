# vygeneruje pozvanky, pokud jeste neexistuji.

from pathlib import Path
import json

pozvanky_path = Path.cwd() / 'pozvanky.json'
triplety_path = Path.cwd() / "kody" / 'triplets_120p.txt'

pozvanky = []
triplety = []
triplety_pre_filter = []
with open(triplety_path, 'r') as t:
    triplety_pre_filter = t.read().split("\n")
    triplety = list(set(triplety_pre_filter))

if len(triplety) != len(triplety_pre_filter):
    print("Pozor, v souboru s kódy jsou duplicity, ale budou vyřešeny a duplicitní kódy smazány.")
else:
    print("V souboru s kódy nejsou žádné duplicity.")
    
triplety = sorted(triplety)

if not pozvanky_path.exists():
    for i, triplet in enumerate(triplety):
        print(triplet, "==")
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
        
    print("Pozvánky byly vygenerovány.")