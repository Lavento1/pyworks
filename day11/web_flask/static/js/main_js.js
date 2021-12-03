setInterval(myWatch, 1000);

function myWatch(){
    var date = new Date();
    var nowTime = date.toLocaleTimeString();

    document.getElementById("display").innerHTML = nowTime;
}