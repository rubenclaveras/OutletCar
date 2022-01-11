$(document).ready(function() {
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