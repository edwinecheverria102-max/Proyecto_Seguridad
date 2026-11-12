document.addEventListener("DOMContentLoaded", () => {

    // explorar catalogo
    const btnExplorar = document.querySelector(".btn-primary");
    const seccionProductos = document.querySelector(".latest-collection");

    btnExplorar.addEventListener("click", (e) => {
        e.preventDefault(); // el enlace no vuelve a recargar la pagina
        seccionProductos.scrollIntoView({ behavior: "smooth" });
    });

    // carrito   
    const iconoCarrito = document.querySelector(".nav-icons span:last-child .icon");

    // evitar que se creen multiples toasts si el usuario hace clic muy rápido
    let toastActivo = null;

    if (iconoCarrito) {
        iconoCarrito.addEventListener("click", () => {
            // si hay un toast en pantalla, lo eliminamos para reiniciar la animacion
            if (toastActivo) {
                toastActivo.remove();
            }
        });
    }


    const toast = document.createElement("div");
    toast.className = "toast";
    toast.innerText = "Tu carrito está vacío. ¡Explora el catálogo!";

    document.body.appendChild(toast);
    toastActivo = toast;

    // delay para el registro del elemento 
    setTimeout(() => {
        toast.classList.add("show");
    }, 10);

    // logica para ocultarlo 
    setTimeout(() => {
        toast.classList.remove("show"); // quita la clase y hace la transicion inversa

        // espera a que termine la transición para borrarlo del html
        setTimeout(() => {
            toast.remove();
            toastActivo = null;
        }, 300);

    }, 3000);
});

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
