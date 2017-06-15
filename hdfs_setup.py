#!/usr/bin/python2


import commands,os,time,sys,socket


options="""
-------------------------
press 1 to manual setup hadoop cluster
press 2 to automatic setup hadoop cluster
-------------------------
"""
print options
ch=raw_input()

if ch=='1' :
	print "find all the ip of all system"
	execfile('ip_cpu.py')

else :
	print "bad choice"
	execfile('menu.py')
