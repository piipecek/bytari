import httpGet from "./http_get.js"

let pozvanky = JSON.parse(httpGet("/pozvanky"))

let tbody = document.querySelector("tbody")

for (let pozvanka of pozvanky) {
    let tr = document.createElement("tr")
    let td1 = document.createElement("td")
    let td2 = document.createElement("td")
    let td3 = document.createElement("td")
    let td4 = document.createElement("td")
    let td5 = document.createElement("td")
    let td6 = document.createElement("td")
    let td7 = document.createElement("td")
    let td8 = document.createElement("td")
    let td9 = document.createElement("td")
    let td10 = document.createElement("td")
    let td11 = document.createElement("td")
    let td12 = document.createElement("td")

    td1.innerText = pozvanka["id"]
    td2.innerText = pozvanka["kod"]
    td3.innerText = pozvanka["jmeno"]
    td4.innerText = pozvanka["email"]
    td5.innerText = pozvanka["datum"]
    td6.innerText = pozvanka["cas"]
    td7.innerText = pozvanka["doba"]
    td8.innerText = pozvanka["kdo"]
    td9.innerText = pozvanka["poznamka"]
    td10.innerText = pozvanka["prespat"]
    td11.innerText = pozvanka["odemcena"]


    let button1 = document.createElement("button")
    button1.innerText = "Vynulovat"
    button1.name = "vynulovat"
    button1.value = pozvanka["id"]
    button1.type = "submit"
    button1.classList.add("btn", "btn-light", "mx-2")
    
    let button2 = document.createElement("button")
    if (pozvanka["odemcena"]) {
        button2.innerText = "Uzamknout"
    } else {
        button2.innerText = "Odemknout"
    }
    button2.name = "toggle"
    button2.value = pozvanka["id"]
    button2.type = "submit"
    button2.classList.add("btn", "btn-dark")

    td12.appendChild(button1)
    td12.appendChild(button2)

    tr.appendChild(td1)
    tr.appendChild(td2)
    tr.appendChild(td3)
    tr.appendChild(td4)
    tr.appendChild(td5)
    tr.appendChild(td6)
    tr.appendChild(td7)
    tr.appendChild(td8)
    tr.appendChild(td9)
    tr.appendChild(td10)
    tr.appendChild(td11)
    tr.appendChild(td12)

    tbody.appendChild(tr)
}



