window.indexedDB = window.indexedDB || window.mozIndexedDB || window.webkitIndexedDB || 
window.indexedDB;
 
window.IDBTransaction = window.IDBTransaction || window.webkitIDBTransaction || 
window.IDBTransaction;
window.IDBKeyRange = window.IDBKeyRange || 
window.webkitIDBKeyRange || window.IDBKeyRange
 
if (!window.indexedDB) {
   window.alert("Your browser doesn't support a stable version of IndexedDB.")
}

const email = document.getElementById("email");
const password = document.getElementById("password");
const submitter = document.getElementById("submit");

const loginData = [
    {id: 01, email: email, password: password}
];

function add() {
    var request = db.transaction(["login"], "readwrite")
    .objectStore("login")
    .add({ id: "01", email: email, password: password});
    
    request.onsuccess = function(event) {
       alert("Prasad has been added to your database.");
    };
    
    request.onerror = function(event) {
       alert("Unable to add data\r\nPrasad is already exist in your database! ");
    }
 }

function read() {
    var transaction = db.transaction(["login"]);
    var objectStore = transaction.objectStore("login");
    var request = objectStore.get("00-03");

    request.onerror = function(event) {
        alert("Unable to retrieve daa from database!");
    };

    request.onsuccess = function(event) {
        
        if(request.result) {
            alert("emailL " + request.result.email, "password: " + request.result.password);
        } else {
            alert("Kenny couldn't be found in your database!");  
        }
    };
}

submitter.addEventListener("click", function(event) {
    add();
    read();
});

add();
read();