window.addEventListener('load', () => {
    const contenedor_loader = document.querySelector('.contenedorLoader')
    contenedor_loader.style.opacity = 0
    contenedor_loader.style.visibility = 'hidden'
})
$(document).ready(function() {
    //Modificar el CSS de la class cabecera metiendo un borde negro
    $(".cabecera").css("border", "3px solid black");
})
$(".checkMode").click(function() {
    if ($("input.checkMode").is(":checked")) {
        $(".theme").attr("href", "styles/dark.css");
    } else {
        $(".theme").attr("href", "styles/estilos.css");
    }
})
var check = document.querySelector(".check");
check.addEventListener('click', idioma);

function idioma() {
    let id = check.checked;
    if (id == true) {
        location.href = "/indexIngles.html";
    } else {
        location.href = "../";
    }
}