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

def ulozit_nove_volno(jmeno: str, date:str, start: str, end: str) -> None:
    start_datetime = datetime.datetime.fromisoformat(date + "T" + start + ":00+00:00")
    end_datetime = datetime.datetime.fromisoformat(date + "T" + end + ":00+00:00")
    volno = get_volno()
    volno.append({
        "id": max([zaznam["id"] for zaznam in volno], default=-1) + 1,
        "jmeno": jmeno,
        "start": start_datetime.isoformat(),
        "end": end_datetime.isoformat()
    })
    save_volno(volno)
    
def delete_volno_by_id(id_: int) -> None:
    volno = get_volno()
    volno = [zaznam for zaznam in volno if zaznam["id"] != id_]
    save_volno(volno)
    
def volna_for_admin() -> list:
    volna = get_volno()
    result = []
    for zaznam in volna:
        result.append({
            "id": zaznam["id"],
            "jmeno": zaznam["jmeno"],
            "date": datetime.datetime.fromisoformat(zaznam["start"]).strftime("%d. %m. %Y"),
            "start": datetime.datetime.fromisoformat(zaznam["start"]).strftime("%H:%M"),
            "end": datetime.datetime.fromisoformat(zaznam["end"]).strftime("%H:%M"),
        })
    result.sort(key=lambda x:(x["jmeno"], x["date"], x["start"]))
    return result

def get_casova_okna_pro_lidi(lidi: list) -> list:
    volna = get_volno()
    print(lidi)
    result = []
    if len(lidi) == 1:
        for volno in volna:
            if volno["jmeno"] == lidi[0]:
                zaznam = {
                    "start": datetime.datetime.fromisoformat(volno["start"]),
                    "end": datetime.datetime.fromisoformat(volno["end"])
                }
                result.append(zaznam)
                
    else:
        for volno in volna:
            if volno["jmeno"] in lidi:
                zaznam = {
                    "start": datetime.datetime.fromisoformat(volno["start"]),
                    "end": datetime.datetime.fromisoformat(volno["end"]),
                    "jmeno": volno["jmeno"]
                }
                result.append(zaznam)
        
        result.sort(key=lambda x: x["start"])
        
        overlaps = []
        for i in range(len(result)):
            lidi_current = []
            lidi_current.append(result[i]["jmeno"])
            for j in range(i + 1, len(result)):
                if result[i]["end"] > result[j]["start"]:
                    overlap_start = max(result[i]["start"], result[j]["start"])
                    overlap_end = min(result[i]["end"], result[j]["end"])
                    lidi_current.append(result[j]["jmeno"])
                    if (len(lidi_current) == len(lidi)):
                        overlaps.append(
                            {
                                "start": overlap_start,
                                "end": overlap_end,
                            }
                        )
        
        result = overlaps
        
    # overit delku okna a budoucnost a udelat hezky
    
    result_final = []
    print(result, "+++")
    for okno in result:
        if okno["end"]-okno["start"] >= datetime.timedelta(minutes=30) and okno["start"].replace(tzinfo=None) > datetime.datetime.now().replace(tzinfo=None):
            zaznam = {
                "datum": okno["start"].strftime("%d. %m. %Y"),
                "od": okno["start"].strftime("%H:%M"),
                "do": okno["end"].strftime("%H:%M")
            }
            result_final.append(zaznam)
                
    return result_final