var create = document.getElementById('create');
var inp2 = document.getElementById("inp2");

function create_cn(){
    var create_cn_one = document.createElement("canvas");
    create_cn_one.style.position = 'absolute';
    create_cn_one.style.top = '100px';
    create_cn_one.style.left = '100px';
    create_cn_one.style.background = 'blue';
    create_cn_one.style.width = '75px';
    document.body.appendChild(create_cn_one);
    create_cn_one.hidden = true;
}

function test(){
    alert('test');
}
function pls_work(){
    var pls = document.createElement("h1");
    pls.style.position = 'absolute';
    pls.innerHTML = 'HolaMundo';
    pls.style.top = '100px';
    pls.style.left = '100px';

    document.body.appendChild(pls);

    create.addEventListener("click", function(){
        pls.style.position = 'absolute';
        pls.style.top = '170px';
    });
}

var pass_next = false;

var test1 = create.addEventListener("click", function(){
    var create_pls_one = document.createElement("h1");
    create_pls_one.style.position = 'absolute';
    create_pls_one.innerHTML = 'HolaMundo';
    create_pls_one.style.top = '100px';
    create_pls_one.style.left = '100px';

    document.body.appendChild(create_pls_one);

    pass_next = true;
});

pass_test1_bool = false;
pass_test2_bool = false;
pass_test3_bool = false;
pass_test4_bool = false;
function pass_test1(){
    create.addEventListener("click", function(){
        var create_two = document.createElement("h1");
        create_two.style.position = 'absolute';
        create_two.innerHTML = 'HolaMundo';
        create_two.style.left = '100px';
    });
    pass_test1_bool = true;
}

if (pass_next = true){
    pass_test1();
}
else {
    null;
}

function pass_test2(){
    create.addEventListener("click", function(){
        var create_three = document.createElement("h1");
        create_three.style.position = 'absolute';
        create_three.innerHTML = 'HolaMundo';
        create_three.style.left = '100px';
        create_three.style.top = '200px';

        document.body.appendChild(create_three);
    });
    pass_test2_bool = true;
}

function pass_test3(){
    create.addEventListener("click", function(){
        var create_for = document.createElement("h1");
        create_for.style.position = 'absolute';
        create_for.innerHTML = 'HolaMundo';
        create_for.style.left = '100px';
        create_for.style.top = '300px';

        document.body.appendChild(create_for);
    });
    pass_test3_bool = true;
}
function pass_test4(){
    create.addEventListener("click", function(){
        var create_five = document.createElement("h1");
        create_five.style.position = 'absolute';
        create_five.innerHTML = 'HolaMundo';
        create_five.style.left = '100px';
        create_five.style.top = '400px';
    });
    pass_test4_bool = true;
}


function pass_test_nop(){
    create.addEventListener("click", function(){
        alert("Noooooo, para porfa.")
    });
}

if (pass_test1_bool = true) {
    pass_test2();
}
else if (pass_test2_bool = true) {
    pass_test3();
}
else if (pass_test3_bool = true) {
    pass_test4();
}
else{
    pass_test_nop();
}

var licence = "12htrsh2552bs52";
var aprove = false;
function pass_verify(){
    if (inp2.innerHTML == "12htrsh2552bs52"){
        alert("Yes!");
    }
    else if (inp2.innerHTML != "12htrsh2552bs52"){
        alert("No!");
    }
    aprove = true;
}

inp2.addEventListener("dblclick", function(){
    pass_verify();
});

var mouse = window.MouseEvent();

var can = document.createElement("canvas");
var dsu = document.getElementById("canvas");
var doc = document.getElementById("canvas").addEventListener("dragstart", function(){
    dsu.style.position = mouse;
});