const contenido= document.getElementById("contenido");

// contenido.innerHTML="Hola Programadores";

let nombre = "Daniel Santillan";
let edad =19;

let edades=[23,45,2,42, 89, 23];
//let edad=17;
// // const COLOR_ROJO= "#FF0000";
// // let resultado= "Nombre: " + nombre;
// // nombre= "Feliciano Santillan";
// // console.log(edades.length);
// contenido.innerHTML = "<h2>"+nombre+"</h2>";
// contenido.innerHTML = "<h3>"+edad+"</h3>";
// let resultado="Nombre"+nombre;


// if(edad>8){
//     alert("Puede entrar en la disco");
// }else if(edad>13){
//     alert("Puede entrar con un adulto");
// }else{
//     alert("No puede entrar")
// }

addContent("<h2>"+nombre+"</h2>"+"<h3>"+edad+"</h3>");


for(let i=6; i <= 10; i++){
    addContent("<h3>La edad es de "+i+" años</h3>");
}
function addContent(newContent){
    contenido.innerHTML += newContent;
}


for(let i=0; i <= edades.length; i++){
    addContent("<h3>La edad es de: "+edades[i]+" años.</h3>");
}
function addContent(newContent){
    contenido.innerHTML += newContent;
}

