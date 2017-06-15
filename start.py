#!/usr/bin/python2


import commands,os,time,sys,socket


print "-------------------------"
print "welcome to the world of hadoop"
print "-------------------------"
print "-------------------------"

time.sleep(2)

user=raw_input("enter user name to access project  ")
password=raw_input("enter password:  ")

if user=='root' and password =='redhat' :
	print "access granted"
	execfile('menu.py')

else :
        print "wrong authentication "
	exit()

