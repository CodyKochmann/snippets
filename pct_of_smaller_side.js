var pct_of_smaller_side = function(dom_e,selected_percent){
    // sizes a dom element to the smaller sized side
    var width = $(window).width();
    var height = $(window).height();
    var important_measurement=0;
    if (width>height){
        important_measurement=height*selected_percent;
    } else {
        important_measurement=width*selected_percent;
    }
    dom_e.height(important_measurement);
    dom_e.width(important_measurement);
}