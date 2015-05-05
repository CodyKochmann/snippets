function grep(theUrl){ /* reference link:http://stackoverflow.com/questions/247483/http-get-request-in-javascript*/
    var xmlHttp = null;
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
