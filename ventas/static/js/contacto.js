function mostrarSegundaLista(opcion) {
    var segundaListaRow = document.getElementById("segundaListaRow");
    var segundaLista = document.getElementById("opcion2");
  
    segundaLista.innerHTML = ""; // Limpiar las opciones anteriores
  
    if (opcion === "urbanas") {
        mostrarOpciones(["G 310 R", "FZ-25", "XR-190"]);
      } else if (opcion === "vintage") {
        mostrarOpciones(["Euromot Vintage Cafe Racer", "Kawasaki Z 650 RS", "Scrambler Ducati 1100 Tribute Pro"]);
      } else if (opcion === "hyper-naked") {
        mostrarOpciones(["HONDA CB190 R Repsol", "YAMAHA NEW MT-07", "TRIUMPH Street Triple RS"]);
      } else if (opcion === "adventure-touring") {
        mostrarOpciones(["Africa Twin Mecánica 2023", "Super Teneré (XT-1200ZE)", "Tiger 1200 Rally Explorer"]);
      } else if (opcion === "scooters") {
        mostrarOpciones(["Vespa Primavera", "Honda PCX", "Yamaha NMAX"]);
      } else {
        segundaListaRow.style.display = "none";
      }
  }
  
  function mostrarOpciones(opciones) {
    var segundaLista = document.getElementById("opcion2");
    opciones.forEach(function (opcion) {
      var option = document.createElement("option");
      option.value = opcion;
      option.text = opcion;
      segundaLista.add(option);
    });
  
    segundaListaRow.style.display = "table-row";
  }
  