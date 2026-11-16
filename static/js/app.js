document.addEventListener("DOMContentLoaded", () => {

    // explorar catalogo
    const btnExplorar = document.querySelector(".btn-primary");
    const seccionProductos = document.querySelector(".latest-collection");

    if (btnExplorar && seccionProductos) {
        btnExplorar.addEventListener("click", (e) => {
            e.preventDefault();
            seccionProductos.scrollIntoView({ behavior: "smooth" });
        });
    }

    // menu responsivo
    const nav = document.querySelector("nav");
    
    // boton
    const menuBtn = document.createElement("div");
    menuBtn.innerHTML = "☰"; // 
    menuBtn.style.fontSize = "24px";
    menuBtn.style.cursor = "pointer";
    menuBtn.style.display = "none"; // oculto por defecto en escritorio

    
    nav.parentNode.insertBefore(menuBtn, nav);

    // logica para mostrar/ocultar 
    menuBtn.addEventListener("click", () => {
        
        if (nav.style.display === "block") {
            nav.style.display = "none";
        } else {
            nav.style.display = "block";
            nav.style.position = "absolute";
            nav.style.top = "70px";
            nav.style.left = "0";
            nav.style.width = "100%";
            nav.style.backgroundColor = "#fff";
            nav.style.padding = "20px";
            nav.style.textAlign = "center";
            nav.style.boxShadow = "0 5px 10px rgba(0,0,0,0.1)";
        }
    });

    // mostrar el boton solo en pantallas pequeñas
    function checkScreenSize() {
        if (window.innerWidth <= 900) {
            menuBtn.style.display = "block";
            nav.style.display = "none"; // ocultar meno en movil por defecto
        } else {
            menuBtn.style.display = "none";
            nav.style.display = "block"; // mostrar menu en escritorio
        }
    }

    // ejecutar al cargar y al redimensionar la ventana
    checkScreenSize();
    window.addEventListener("resize", checkScreenSize);
});