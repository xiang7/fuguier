$(window).ready(function (){
    var scrollOffset = $("#sticky-nav").height();
    var workOffset = $("#work").position().top - scrollOffset;
    var aboutOffset = -1;
    
    $("#work-link").click(function (){
        $("#wrapper").animate({
            scrollTop: workOffset
        }, 500);
    });
    
    $('[data-uk-grid]').on('afterupdate.uk.grid', function(e, children) {
        aboutOffset = $("#about").offset().top-$("#home-image-top").offset().top;
        $("#about-link").click(function (){
            $("#wrapper").animate({
                scrollTop: aboutOffset
            }, 500);
        }); 
    });
});