window.addEventListener('load', () => {
    const contenedor_loader = document.querySelector('.contenedorLoader')
    contenedor_loader.style.opacity = 0
    contenedor_loader.style.visibility = 'hidden'
})

/*var check1 = document.querySelector(".checkMode");
check1.addEventListener('click', modoNocheDia);

function modoNocheDia() {
    let idi = check1.checked;
    if (idi == true) {
        $('.theme').attr('href', 'static/styles/dark.css');
    } else {
        $('.theme').attr('href', 'static/styles/estilos.css');
    }
}*/
$(document).ready(function() {
    //Modificar el CSS de la class cabecera metiendo un borde negro
    $(".cabecera").css("border", "3px solid black");
    //Modo nocturno
    $('.checkMode').click(function() {
        if ($('input.checkMode').is(':checked')) {
            $('.theme').attr('href', '../static/styles/dark.css');
        } else {
            $('.theme').attr('href', '../static/styles/estilos.css');
        }
    })
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