var set_view = function(dom_e){
    // sets horizontal or vertical view rules of a dom element
    // by: Cody Kochmann
    var width = $(window).width();
    var height = $(window).height();
    var horizontal=width>height;
    var vertical=!horizontal;
    if (horizontal){
        if(dom_e.hasClass('horizontal')==false){
            dom_e.addClass('horizontal');
        }
        if(dom_e.hasClass('vertical')==true){
            dom_e.addClass('vertical');
        }
    }
    if (vertical){
        if(dom_e.hasClass('vertical')==false){
            dom_e.addClass('vertical');
        }
        if(dom_e.hasClass('horizontal')==true){
            dom_e.addClass('horizontal');
        }
    }
}