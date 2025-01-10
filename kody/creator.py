# tohle bylo one time use - triplety jsou hotove. Nespouštět znovu, jinak se přepíšou
exit()

import json
import random

with open("kody/db.json") as f:
    data = json.load(f)

    triplets = []
    for _ in range(30):
        triplet = random.sample(data, 3)
        triplets.append(", ".join(triplet))

    with open("kody/triplets.txt", "w") as f:
        f.write("\n".join(triplets))