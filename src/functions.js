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
    
    document.getElementById("cena").innerHTML = rez;
}