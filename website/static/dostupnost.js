let plusbutton = document.getElementById("+");
let volno_div = document.getElementById("volno");
let submit_button = document.getElementById("submit_button");
let form = document.getElementById("form");
let name_select = document.getElementById("select");
let data_input = document.getElementById("data");
let tbody = document.getElementById("tbody");

import httpGet from "./http_get.js"

let volno = JSON.parse(httpGet("/volna"))

plusbutton.addEventListener("click", function() {
    let row = document.createElement("div");

    let date = document.createElement("input");
    date.type = "date";
    date.name = "date";
    date.classList.add("mx-2");
    row.appendChild(date);

    let od_span = document.createElement("span");
    od_span.innerText = "od";
    od_span.classList.add("mx-2");
    row.appendChild(od_span);

    let start_time = document.createElement("input");
    start_time.type = "time";
    start_time.name = "start_time";
    start_time.classList.add("mx-2");
    row.appendChild(start_time);

    let do_span = document.createElement("span");
    do_span.innerText = "do";
    do_span.classList.add("mx-2");
    row.appendChild(do_span);

    let end_time = document.createElement("input");
    end_time.type = "time";
    end_time.name = "end_time";
    end_time.classList.add("mx-2");
    row.appendChild(end_time);

    volno_div.appendChild(row);
})


submit_button.addEventListener("click", function() {
    let result = {}
    let name = name_select.value;
    let error = false
    result["name"] = name;
    result["dates"] = []
    for (let row of volno_div.children) {
        let date = row.children[0].value;
        let start_time = row.children[2].value;
        let end_time = row.children[4].value;
        if (!date || !start_time || !end_time) {
            error = true;
            break;
        }
        result["dates"].push({
            "date": date,
            "start": start_time,
            "end": end_time
        })
    }
    if (error) {
        alert("Chyba v zadávání času, opravte ji.");
        return;
    }
    data_input.value = JSON.stringify(result);
    form.submit();
})

for (let v of volno) {
    let tr = document.createElement("tr");
    let td1 = document.createElement("td");
    let td2 = document.createElement("td");
    let td3 = document.createElement("td");
    let td4 = document.createElement("td");
    let td5 = document.createElement("td");

    td1.innerText = v["jmeno"];
    td2.innerText = v["date"];
    td3.innerText = v["start"];
    td4.innerText = v["end"];

    let smazat_button = document.createElement("button");
    smazat_button.innerText = "Smazat";
    smazat_button.name = "smazat";
    smazat_button.value = v["id"];
    smazat_button.type = "submit";
    smazat_button.classList.add("custom-delete-button");
    td5.appendChild(smazat_button);

    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tr.appendChild(td4);
    tr.appendChild(td5);
    tbody.appendChild(tr);
}