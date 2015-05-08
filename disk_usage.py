#!/usr/bin/env python
# shell script for getting stats on the primary disk
# example data available = ['/dev/disk0s2', '328Gi', '315Gi', '13Gi', '97%', '82518570', '3418928', '96%', '/\n']

import os

disk = os.popen("df -h | grep '/dev/disk0s2'").read().split(' ')

for i in list(disk):
  if len(i) is 0:
    disk.remove(i)

disk = {'used':disk[2][:-1],'free':disk[3][:-1],'percent':disk[4]}
disk['free_pct']=str(100-int(disk['percent'][:-1]))+'%'

print "Disk:"+disk['free_pct']+"\n",disk['used']+"/"+disk['free']
#print "\nDisk Space\n",disk['free'],"/",disk['free_pct']
