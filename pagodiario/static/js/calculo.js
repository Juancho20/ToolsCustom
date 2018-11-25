function sumar (valor) {
    //var total = 0;  
    //valor = parseFloat(valor); // Convertir el valor a un entero (número).
  
    actual = document.getElementById('total').val());

    var valor1 = parseFloat(document.getElementById("base").val());
    var valor2 = parseFloat(document.getElementById("gastos").val());
    var valor3 = parseFloat(document.getElementById("compras").val());
    var valor4 = parseFloat(document.getElementById("dinero").val());
    var valor5 = parseFloat(document.getElementById("ventas").val());
    var suma = parseFloat(valor1) + parseFloat(valor2) + parseFloat(valor3) + parseFloat(valor4) + parseFloat(valor5);
    var promedio = parseFloat(suma) / parseFloat(2);
    var actual = promedio.toFixed(1);
    //console.log(promedio.toFixed(1));
  
    // Colocar el resultado de la suma en el control "span".
    document.getElementById('total').val() = actual;
    alert("Esto funcion");
}