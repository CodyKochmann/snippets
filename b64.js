var b64=function(){
    // small base64 object for easy encoding/decoding with b64.e and b64.d
    // b64.eval() evaluates base64 stored javascript 
    // by: Cody Kochmann
    this.e = function(a){return(window.btoa(unescape(encodeURIComponent(a))))};
    this.d = function(a){return(decodeURIComponent(escape(window.atob(a))))};
    this.eval = function(a){return(eval(decodeURIComponent(escape(window.atob(a)))))};
}
b64=new b64();