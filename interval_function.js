// Generated by CoffeeScript 1.9.2
(function() {
  window.timed_interval = function(main_process, timeout, verbose) {
    var print, self;
    this.main_process = main_process;
    this.timeout = timeout;
    this.verbose = verbose != null ? verbose : true;
    /*
    Author: Cody Kochmann
    Build: 4
    Date Last Modified: Fri Jun 12 09:53:37 PDT 2015

    This is an improved function to the currently used setInterval in javascript.
    It has better Controls towards the control flow of the interval overall. 
    This implementation also prevents function overlapping where is the interval 
      is set too quickly and tries to run again before the previous 
      one has finished, thus making it safe to set interval to 1ms 
      because it will not run again until the previous function is complete.

    For a quick and easy demo, run this in the console:
      var demo = new timed_interval();
      demo.test();

    Built in functions:
      start   -   starts the interval when ready
      stop    -   stops the interval completely
      pause   -   temporarily pauses the interval without deleting it
      resume  -   same functionality as start but available for clean usage.
      test    -   runs a demo for you to get a feel for how it works
  */;
    self = this;
    this.running = false;
    this.has_started = false;
    print = function(s) {
      if (self.verbose) {
        console.log(s);
      }
    };
    this.run = function() {
      setTimeout((function() {
        if (self.running === true) {
          self.main_process();
          self.run();
        }
      }), self.timeout);
    };
    this.stop = function() {
      print("stopping interval");
      self.pause();
    };
    this.pause = function() {
      print("pausing interval");
      self.running = false;
    };
    this.start = function() {
      print("starting interval at " + self.timeout + " ms");
      self.running = true;
      self.run();
      self.has_started = true;
    };
    this.resume = function() {
      print("resuming interval at " + self.timeout + " ms");
      self.run();
      self.running = true;
    };
    this.change_interval = function(new_interval) {
      print("setting new interval from " + self.timeout + " ms to " + new_interval + " ms");
      self.timeout = new_interval;
    };
    this.test = function() {
      var test_string;
      test_string = "// timed_interval ready.\n// running this in the console to test the interphase:\n(function(){\n    var test_func=function(){document.write(\"hello<br>\")};\n    var complete=function(){document.write(\"test complete<br>\")}\n    var t = t = new timed_interval(test_func, 50);\n    var change=function(){t.change_interval(300)};\n    t.start();\n    setTimeout(t.pause, 250);\n    setTimeout(change, 250);\n    setTimeout(t.resume, 1500);\n    setTimeout(t.stop, 3000);\n    setTimeout(complete, 3000);\n})();";
      print(test_string);
      eval(test_string);
    };
  };

}).call(this);
