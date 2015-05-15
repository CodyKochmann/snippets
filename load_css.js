var load_css = function(input_url){
    // loads a stylesheet into the page head
    // by: Cody Kochmann
    var l = document.createElement("link");
    l.src=input_url;
    l.rel="stylesheet";
    l.type="text/css";
    document.getElementsByTagName("head")[0].appendChild(l);        
}