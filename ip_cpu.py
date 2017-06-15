#!/usr/bin/python2


import commands,os,time,sys,socket


ip_list=[]
ipaddr="192.168.50."

for i in range(50)[-6:] :
	check=commands.getstatusoutput('ping -c 1 192.168.50.'+str(i))
	if check[0]==0 :
		ip_list.append(ipaddr+str(i))
	else :
		print "IP Address "+str(i)+ " unreachable"

print "scanned ip"
time.sleep(2)
print ip_list

#checking cpu cores
cpu_ip=[]
cpu_ipvalue=[]
cpu_check="lscpu | grep -i 'CPU(s)' | head -1 | cut -d: -f2"

for i in ip_list:
	cpu_core=commands.getoutput('ssh root@'+i+" "+cpu_check)
	cpu_ip.append(i+str(cpu_core))
	cpu_ipvalue=cpu_ip

print cpu_ipvalue

#checking ram
cpu_ipr=[]
cpu_memcheck="cat /proc/meminfo | grep -i MemTotal | cut -d: -f2 "
for i in ip_list:
	cpu_ram=commands.getoutput('ssh root@'+i+" "+cpu_memcheck)
for i in cpu_ipvalue :
	cpu_ipr.append(i+cpu_ram)

print cpu_ipr


