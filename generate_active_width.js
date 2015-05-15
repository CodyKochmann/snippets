var generate_active_width = function(dom_id,min_inches,flexing_percentage,max_inches){
    // pre-renders media specific rules for a div in order to keep it a constant width without needing to
    // worry about the stability of "margin:0 auto" in certain situations.
    // by: Cody Kochmann
    var inject_css = function(a) {
        var b = document.createElement("style");
        b.innerHTML = a;
        b.type = "text/css";
        document.getElementsByTagName("head")[0].appendChild(b)
    }
    var current_inches = 0;
    var iterations = 0.2;
    var up_to_x_inches = 34;
    var str = function(s){return(s.toString())};
    var print = function(s){console.log(s)};
    var output = "";
    output+=("#"+dom_id+"{min-width:"+str(min_inches)+"in}");
    for (var i = 0; i < parseInt(up_to_x_inches/iterations); i++) {
        var current = iterations*i;
        if (current >= min_inches && current < max_inches){
            output+=("@media (min-width: "+str(current)+"in) and (max-width: "+str(current+iterations)+"in) {#"+dom_id+" {width: "+flexing_percentage+"%;margin:0 "+((100-flexing_percentage)*0.5)+"%;}}");
        } else if (current >= max_inches){
            var new_width = flexing_percentage*max_inches/current
            output+=("@media (min-width: "+str(current)+"in) and (max-width: "+str(current+iterations)+"in) {#"+dom_id+" {width: "+str(new_width).substr(0,6)+"%;margin:0 "+str((100-new_width)*0.5).substr(0,6)+"%;}}");
        }
    };
    inject_css(output);
}
generate_active_width("bug_report",3,90,6,32);