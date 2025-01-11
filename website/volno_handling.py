import json
from pathlib import Path
import datetime

volno = Path('volno.json')

def get_volno() -> dict:
    with volno.open() as f:
        return json.load(f)
    
def save_volno(volno_dict: dict) -> None:
    with volno.open("w") as f:
        json.dump(volno_dict, f, indent=4)

def ulozit_nove_volno(jmeno: str, start: str, end: str) -> None:
    print(jmeno, start, end)
    start_d = datetime.datetime.fromisoformat(start.replace("Z", "+00:00"))
    end_d = datetime.datetime.fromisoformat(end.replace("Z", "+00:00"))
    volno = get_volno()
    volno.append({
        "id": max([zaznam["id"] for zaznam in volno], default=-1) + 1,
        "jmeno": jmeno,
        "start": start_d.isoformat(),
        "end": end_d.isoformat()
    })
    save_volno(volno)
    
def delete_volno_by_id(id_: int) -> None:
    volno = get_volno()
    volno = [zaznam for zaznam in volno if zaznam["id"] != id_]
    save_volno(volno)