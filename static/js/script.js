jQuery(document).ready(function($) {
    //---------------- PRELOADER -------------
    if ($("#preloader")) {
        $("#preloader").remove();
    }

    var pathname = window.location.pathname;
    var searchQuery = window.location.search;
    var pathnameArr = pathname.split('/');
    var searchQueryArr = searchQuery.split('=');
    if (searchQuery) {
    var editPath = '/' + pathnameArr[1] + '/' + searchQueryArr[0] + '/';
    }
    else{
    var editPath = '/' + pathnameArr[1] + '/';
    }
    if  (window.location.pathname === "/") {
        var currentActive = document.getElementsByClassName("active");
        currentActive[0].className = currentActive[0].className.replace(" active","");
        var homeTab = document.getElementById("Home-link");
        homeTab.className += " active";
        homeTab.style.borderBottom = "2px solid #fff";
    }
    else if (editPath == '/products/') {
        var currentActive = document.getElementsByClassName("active");
        currentActive[0].className = currentActive[0].className.replace(" active","");
        var allProducts = document.getElementById("all-products-link");
        allProducts.className += " active";
        allProducts.style.borderBottom = "2px solid #fff";
    }
    else if (editPath === "/products/?category/") {
        editPath += searchQueryArr[1]
        if(editPath === "/products/?category/New%20Arrivals") {
            var currentActive = document.getElementsByClassName("active");
            currentActive[0].className = currentActive[0].className.replace(" active","");
            var special = document.getElementById("specials-link");
            special.className += " active";
            special.style.borderBottom = "2px solid #fff";
        }
        else {
            var currentActive = document.getElementsByClassName("active");
            currentActive[0].className = currentActive[0].className.replace(" active","");
            var bookLink = document.getElementById("all-products-links");
            bookLink.className += " active";
            bookLink.style.borderBottom = "2px solid #fff";
        }
    }
    else if (window.location.pathname === "/contactus/") {
        var currentActive = document.getElementsByClassName("active");
        currentActive[0].className = currentActive[0].className.replace(" active","");
        var contactus = document.getElementById("contactus");
        contactus.className += " active"
        contactus.style.borderBottom = "2px solid #fff";

    }
});
