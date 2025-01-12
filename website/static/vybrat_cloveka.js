let kluci = ["Jenda", "Kuba", "Marek", "Rocco"]

for (let k of kluci) {
    document.getElementById(k+"_img").addEventListener("click", function() {
        document.getElementById(k).checked = !document.getElementById(k).checked;
    });
}

