function load() {
     console.info("Stran se je nalozila");
}


function izracunaj() {


    var razdalja = parseFloat(document.getElementById("vnos_razdalja").value);
    var e = document.getElementById("tip_goriva");
    var gorivo = parseFloat(e.options[e.selectedIndex].value);
    var po = parseFloat(document.getElementById("vnos_poraba").value);
    var e = document.getElementById("potniki");
    var sp =parseFloat(e.options[e.selectedIndex].value);
    var e = document.getElementById("teza");
    var kt = parseFloat(e.options[e.selectedIndex].value);
    var rez = (((razdalja/100) * (po + sp +kt)) * gorivo);
    rez=rez.toFixed(2)

    if (!isNaN(rez))  document.getElementById("cena").innerHTML = rez;
}

function izracunajMojaVozila() {
    var kgoriva = parseFloat(document.getElementById("vnoskolicinagoriva").value);
    var e = document.getElementById("tip_goriva1");
    var gorivo = parseFloat(e.options[e.selectedIndex].value);
    var razdalja = parseFloat(document.getElementById("vnosPrevozenihKM").value);
    var poraba = (kgoriva/(razdalja/100));
    var strosek = kgoriva * gorivo;
    var strosekNaSTO = poraba * gorivo;
    var staraPoraba = 6.5;
    var novaPoraba = (staraPoraba + poraba) / 2;

    if (!isNaN(poraba)) document.getElementById("povprecnaPorabaPoti").innerHTML = poraba.toFixed(2);
    if (!isNaN(strosek)) document.getElementById("strosek").innerHTML = strosek.toFixed(2);
    if (!isNaN(strosekNaSTO)) document.getElementById("strosek100").innerHTML = strosekNaSTO.toFixed(2);
    if (!isNaN(novaPoraba)) document.getElementById("novaPorvprecnaPoraba").innerHTML = novaPoraba.toFixed(2);


}

function toogleMenu() {
    var menu = document.querySelector('.menu ul');
    menu && menu.classList.toggle('open');
}

function openStream(stream){
     video.src=window.URL.createObjectURL(stream);
     video.play();};
     function errorFunction(error){
        console.log("Error: ", error);

     }
     function paintCapture() {
     context.drawImage(video, 0, 0, 140, 130);

     }
     function doVideo() {
        canvas = document.getElementById("slika");
        context = canvas.getContext("2d");
        video = document.getElementById("video"),videoObj = { "video": true, "audio": true };
        navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia ||navigator.mozGetUserMedia || navigator.msGetUserMedia;
        if(navigator.getUserMedia) {
            navigator.getUserMedia(videoObj, openStream, errorFunction );
        }
     }

function showSlika(){
   document.getElementById("div-slikaj").style.display = 'block';
}

function showDodajAvtomobil(){
   document.getElementById("dodajvozilo-div").style.display = 'block';
}

function showDodajPorabo() {
    document.getElementById("dodajporabo-div").style.display = 'block';
}

function dodajVozilo() {


    var neki = document.getElementById("vnosZnamkaMojaVozila").value;
    var poraba = document.getElementById("vnosPrabaMojaVozila").value;

    if(isNaN(parseFloat(poraba)) ||  neki.trim().length == 0 || poraba.length == 0) return;

    var table = document.getElementById("mojA");
    var row = table.insertRow(1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);

    cell1.innerHTML =neki;

    if (document.getElementById("radioBD").checked == true){
        cell2.innerHTML = poraba.toString();
        cell3.innerHTML = '0';

    } else {
        cell2.innerHTML = '0';
        cell3.innerHTML = poraba.toString();
    }


}