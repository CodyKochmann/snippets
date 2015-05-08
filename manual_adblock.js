(function() {
    // covers the screen with a touch interphase that can be used to delete
    // elements in the way. This is purposed to be a manual type of adblock
    // author: Cody Kochmann
    var div = document.createElement("div");
    div.id = 'page_cleaner544';
    div.innerHTML = "<div id='click_remover' style='width:" + window.outerWidth.toString() + "px; height:" + window.outerHeight.toString() + "px; background : rgba(50,50,50,0.1); position:fixed; z-index:2147483646; top:0; left:0;'></div>";
    div.innerHTML += "<style>#close_cleaner{position:fixed;height:auto;padding:0.15in 0;width:2in;bottom:0.5in;left:0.5in;background:rgba(250,250,250,0.85);-webkit-touch-callout: none;-webkit-user-select: none;-khtml-user-select: none;-moz-user-select: none;-ms-user-select: none;user-select: none;color:rgba(50,50,50,0.65);text-align:center;z-index:2147483647;}</style><p id='close_cleaner'>Done</p>";
    document.body.appendChild(div);
    var click_remover = document.getElementById('click_remover');
    click_remover.addEventListener('click', function(e) {
        try{
            var old_height = click_remover.style.height;
            click_remover.style.height = "0px";
            var target = document.elementFromPoint(e.pageX, e.pageY);
            target.style.transitionDuration = "0.5s";
            target.style.opacity=0;
            click_remover.style.height = old_height;
            setTimeout(function(target){
                target.parentNode.removeChild(target);
            }, 500, target);
        } catch(e){
            var o=0;
        }
    }, false);
    var close_cleaner = document.getElementById('close_cleaner');
    close_cleaner.addEventListener('click', function(e) {
        try{
            var t = document.getElementById("page_cleaner544");
            t.innerHTML='';
        } catch(e){
            var o=0;
        }
    }, false);
})();
