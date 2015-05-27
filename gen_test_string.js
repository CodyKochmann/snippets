var gen_test_string = function(len){ // generates a random string to test against
    var test = "ab cd efg hij klm nop qrs tuvwx yzA B CD EFG HIJ KLM NOPQ RSTUV WXY Z 123 4567 8 90"
    for (var i = 0; i < len; i++) {
        test += test.charAt(Math.floor(Math.random() * test.length));
    };
}
