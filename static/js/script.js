 // ----------------------------- ADD ACTIVE CLASS TO THE CURRENT LINK ---------------------------
var header = document.getElementById("main-nav");
var btns = header.getElementsByClassName("nav-item");
console.log(btns);
for (var i = 0; i < btns.length; i++) {
     btns[i].addEventListener("click", function() {
        var current = document.getElementsByClassName("nav-tabs");
        console.log(current);
        current[0].className = current[0].className.replace(" nav-tabs", "");
        this.className += " nav-tabs";
    });
}

jQuery(document).ready(function($) {
    //---------------- PRELOADER -------------
    if ($("#preloader")) {
        $("#preloader").remove();
    }
});
