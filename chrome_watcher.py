#!/usr/bin/env python
# shell script to collect the links visited on Google Chrome
# by: Cody Kochmann

import os, time

def current_links():
    try:
        chrome_link=os.popen("""osascript -e 'tell application "Google Chrome" to return URL of active tab of front window'""").read().split("\n")[0]
        return chrome_link
    except:
        pass

link_history=[]
while True:
    time.sleep(0.25)
    current_link=current_links()
    if current_link not in link_history:
        link_history.append(current_link)
        print current_link