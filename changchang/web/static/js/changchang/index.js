$(window).ready(function (){ 
    var shouldClickAboutLink = false;
    var gridUpdateOnPageloadCount = 0;
                                              
    $("#work-link").click(function (){
        var workOffset = $("#work").offset().top - $("#home-image-top").offset().top;
        $("#wrapper").animate({
            scrollTop: workOffset
        }, 500);
    });
    
    $("#about-link").click(function (){
        var aboutOffset = $("#about").offset().top-$("#home-image-top").offset().top;
        $("#wrapper").animate({
            scrollTop: aboutOffset
        }, 500);
    });
    
    $('[data-uk-grid]').on('afterupdate.uk.grid', function(e, children) {
        // after update is called twice on a page load
        // Since we click base-filter on page load, 3 calls are expected
        gridUpdateOnPageloadCount += 1;
        if (shouldClickAboutLink && gridUpdateOnPageloadCount == 3) {
            shouldClickAboutLink = false;
            setTimeout(function() {
               $("#about-link").click(); 
            }, 10);
        }
    });
    
    // Project pages uses non-existant anchors so index page can catch them and scroll to proper offset.
    hash = window.location.hash;
    if (hash == '#work-from-project') {
        $("#work-link").click();
    } else if (hash == '#about-from-project') {
        shouldClickAboutLink = true;
    }
    
    $('#see-more').click(function() {
        // Decision was not to show the filters
//        $('#work-filter-div').show();
        $('#see-more-button').hide();
        $('#all-filter-a').click();
    });
    
    $('#about-see-more-link').click(function() {
        $('#about-see-more-link').hide();
        $('#about-detail-image').show();
    });
    
    setTimeout(function() {
        $('#base-filter-a').click();
    },10);
});