#!/usr/bin/env python 
# shell script that uses cpulimit to slow down a selfish app

import os, sys, time

if "-stop" in " ".join(sys.argv):
    print "stopping all limiters."
    os.system('killall cpulimit')

target_app = raw_input("What app would you like to limit?\n")
limit = raw_input("Ok we're gonna tie this fucker up!\nHow much leash are you willing to give it? (out of 100% of your cpu)\n")

cpu_threads = int(os.popen("sysctl -a | grep machdep.cpu | tail -c 2").read())
print cpu_threads

def retrieve_all_threads():
    global target_app
    any_video_converters_threads = os.popen('''ps -eo pid,%cpu,comm | grep '''+target_app).read()
    any_video_converters_threads = any_video_converters_threads.split('\n')
    pids = []
    for i in any_video_converters_threads:
        try:
            pids.append(i.split(' ')[0])
        except:
            pass
        if len(pids[-1])<2:
            pids.remove(pids[-1])
    return pids



print limit

def build_command(limit):
    global cpu_threads
    pids = retrieve_all_threads()
    tmp_limit = (int(limit)/len(pids))
    if tmp_limit is 0:
        tmp_limit = 1
    command_limit = str(tmp_limit*cpu_threads)
    tmp_limit = str(tmp_limit)
    command = []
    for i in pids:
        command.append("nohup cpulimit -l %s -p %s & " % (command_limit,i))
    extra_comment = ''
    if len(command) > 4: 
        extra_comment = "Sweet nipples! "
    print extra_comment+"I found "+str(len(command))+" threads from this app!"
    print "We will have to give every thread "+tmp_limit+"% of the cpu." 
    run = raw_input("It's alright, I have the tools to take care of this. \nThink this will work? (y,n)\n"+str(command)+"\n")
    if 'y' in run:
        for i in command:
            try:
                os.system(i)
                print "Opening thread: %s",i
            except:
                pass
build_command(limit)
block="""while True:
    time.sleep(1)"""