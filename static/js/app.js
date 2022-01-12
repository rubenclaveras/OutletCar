$(document).ready(function() {
    //Modificar el CSS de la class cabecera metiendo un borde negro
    $(".cabecera").css("border", "3px solid black");

    var check = document.querySelector(".check");
    check.addEventListener('clic', idioma);

    function idioma() {
        let id = check.checked;
        if (id == true) {
            location.href = "../../ingles/index.html";
        } else {
            location.href = "../../templates/indexhtml";
        }
    }
})