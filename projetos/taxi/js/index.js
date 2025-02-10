function que() {
    let total1 = document.getElementById("total").value;
    let total2 = document.getElementById("total2").value;
    let coisado1 = document.getElementById("coisado").value;
    let combustivel = 6.50

    let km = (total1 && total2 / 1000);
    let kmfinal = (total1 =+ total2);
    let gasto = km / combustivel
    let lucro = coisado1 / gasto

    document.getElementById("resultado").innerHTML = "carro andou por: " + kmfinal + "km \n combustivel gasto foi de:" + gasto + "Litros. \n  o valor do combustivel hoje é R$" + combustivel + ". \n o valor total ganho pela corrida foi: R$" + coisado1 + "\n lucro de: R$" + lucro
}