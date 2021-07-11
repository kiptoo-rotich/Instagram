$(document).ready(function () {
    var button = document.querySelector(".like");
    document.body.style.background = "white";
    button.addEventListener("click", function () {
        if (document.body.style.background == "white") {
            document.body.style.background = "purple";
        } else if (document.body.style.background == "purple") {
            document.body.style.background = "white";
        }
    });
});
