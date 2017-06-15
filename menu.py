#!/usr/bin/python2


import commands,os,time,sys,socket
options="""
-------------------------
press 1 to setup hadoop cluster:
press 2 to setup MR:
press 3 to setup HIVE:
-------------------------
"""

print options

ch=raw_input()
if ch=='1' :
	print "nice choice lets start process"
	execfile('hdfs_setup.py')
elif ch=='2' :
	print "make sure you have enough amount to cpu stores"
	execfile('mr_setup.py')
else :
	print "wrong option"
	execfile('start.py')
