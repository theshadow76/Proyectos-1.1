var bg = document.getElementById("changebg");
var c = document.getElementById("body");
var a_cn_one = document.getElementById("main-cn-fm-one");

bg.addEventListener("click", function(){
    var data1 = prompt("Enter your color code: ");
    data1.toString();
    document.body.style.backgroundColor = data1;
    c.style.backgroundColor = data1;
});

a_cn_one.addEventListener("mouseover", function(){
    if (a_cn_one.mouseover = true) {
        a_cn_one.style.backgroundColor = "white";
        a_cn_one.style.cursor = "pointer";
        a_cn_one.style.lightingColor = "white";

        var div1 = document.createElement("div");
        div1.style.position = "absolute";
        div1.style.top = y;
        div1.style.left = x;
        div1.style.right = x;
        div1.style.bottom = y;
        div1.style.margin = "5px";

    }
    else{
        a_cn_one.style.backgroundColor = "black";
    }
});
a_cn_one.addEventListener("mouseout", function(){
    a_cn_one.style.backgroundColor = "black";
});