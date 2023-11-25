/*!
* Start Bootstrap - Blog Post v5.0.8 (https://startbootstrap.com/template/blog-post)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-post/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

// home\static\js\scripts.js

// Espera a que el contenido de la página esté cargado
document.addEventListener("DOMContentLoaded", function () {
    // Selecciona la imagen por su ID
    var aboutImage = document.getElementById("about-image");

    // Agrega un evento para cambiar la opacidad al hacer hover sobre la imagen
    aboutImage.addEventListener("mouseover", function () {
        this.style.opacity = "0.8";
    });

    // Agrega un evento para restaurar la opacidad al quitar el hover
    aboutImage.addEventListener("mouseout", function () {
        this.style.opacity = "1";
    });
});
