import httpGet from "./http_get.js"

let lidi_input = document.getElementById('lidi');
let lidi = JSON.parse(lidi_input.value);

let terminy = JSON.parse(httpGet("/terminy/"+JSON.stringify(lidi)))

console.log(terminy)

if (terminy.length == 0){
    document.getElementById("zadne_terminy").style.display = "flex";
    document.getElementById("terminy-wrapper").style.display = "none";
} else {
    document.getElementById("zadne_terminy").style.setProperty('display', 'none', 'important');
    document.getElementById("terminy-wrapper").style.display = "flex";
    generovat_terminy(terminy);
}

function generovat_terminy(terminy){
    for (let termin of terminy){
        let form = document.createElement('form');
        form.method = "POST";
        let termin_div = document.createElement('div');
        termin_div.classList.add('termin');
        let row = document.createElement('div');
        row.classList.add('row');
        let col1 = document.createElement('div');
        col1.classList.add('col', 'd-flex', 'flex-column', 'align-items-end', 'justify-content-between', 'px-4');
        let col2 = document.createElement('div');
        col2.classList.add('col', 'd-flex', 'flex-column', 'align-items-start', 'justify-content-between', 'px-4');
        
        let casove_okno_div = document.createElement('div');
        casove_okno_div.classList.add('casove-okno');
        casove_okno_div.innerText = "Časové okno"
    
        let kdy_div = document.createElement('div');
        kdy_div.innerText = "Kdy: "+termin.datum;
    
        let od_div = document.createElement('div');
        od_div.innerText = "Od: "+termin.od;
    
        let do_div = document.createElement('div');
        do_div.innerText = "Do: "+termin.do;
    
        let kdy_prijit_div = document.createElement('div');
        kdy_prijit_div.innerText = "Kdy chci přijít: "
        let date_input = document.createElement('input');
        date_input.name = "kdy";
        date_input.type = "time";
    
        let na_jak_dlouho_div = document.createElement('div');
        na_jak_dlouho_div.innerText = "Na jak dlouho: "
        let select = document.createElement('select');
        select.name = "doba";
        let option1 = document.createElement('option');
        option1.value = "30 minut";
        option1.innerText = "30 minut";
        let option2 = document.createElement('option');
        option2.value = "1 hodina";
        option2.innerText = "1 hodina";
        let option3 = document.createElement('option');
        option3.value = "1 hodina 30 minut";
        option3.innerText = "1 hodina 30 minut";
        let option4 = document.createElement('option');
        option4.value = "2 hodiny";
        option4.innerText = "2 hodiny";
        let option5 = document.createElement('option');
        option5.value = "3 hodiny";
        option5.innerText = "3 hodiny";
        let option6 = document.createElement('option');
        option6.value = "déle než 3 hodiny";
        option6.innerText = "déle než 3 hodiny";
    
        let prespat_div = document.createElement('div');
        prespat_div.classList.add('d-flex', "align-items-center");
        prespat_div.innerText = "Přeji si přespat: "
        let prespat_input = document.createElement('input');
        prespat_input.type = "checkbox";
        prespat_input.name = "prespat";
        prespat_input.classList.add("checkbox");
    
        let odeslat_div = document.createElement('div');
        odeslat_div.classList.add('d-flex', "justify-content-center");
        let button = document.createElement('button');
        button.innerText = "Odeslat";
        button.type = "button";
        button.classList.add('custom-button');

        button.addEventListener('click', function(){
            if (date_input.value == ""){
                alert("Vyplňte prosím všechny údaje");
            } else {
                form.submit();
            }
        })

        let datum_input = document.createElement('input');
        datum_input.type = "hidden";
        datum_input.name = "datum";
        datum_input.value = termin.datum;
    
        form.appendChild(termin_div);
        termin_div.appendChild(row);
        termin_div.appendChild(odeslat_div);
        row.appendChild(col1);
        row.appendChild(col2);
        col1.appendChild(casove_okno_div);
        col1.appendChild(kdy_div);
        col1.appendChild(od_div);
        col1.appendChild(do_div);
        col2.appendChild(kdy_prijit_div);
        kdy_prijit_div.appendChild(date_input);
        col2.appendChild(na_jak_dlouho_div);
        na_jak_dlouho_div.appendChild(select);
        select.appendChild(option1);
        select.appendChild(option2);
        select.appendChild(option3);
        select.appendChild(option4);
        select.appendChild(option5);
        select.appendChild(option6);
        col2.appendChild(prespat_div);
        prespat_div.appendChild(prespat_input);
        odeslat_div.appendChild(button);
        form.appendChild(datum_input);
    
        document.getElementById('terminy').appendChild(form);
    }
}
