#!/usr/bin/env python
import nmap                         # import nmap.py module
import subprocess, re, sys

print "N2N network scanner for specific community by Luca Carrozza v 0.1"
print "================================================================="
if len(sys.argv)<2:
	print 'Please, specify community as argument'
        sys.exit(2)	

community=sys.argv[1]
ps = subprocess.Popen("ps -ef | grep edge | grep "+community+" | grep -v grep",
                             shell=True,
                             stdout=subprocess.PIPE,
                           )
output = ps.communicate()[0]
print "Founded edge process for "+community+" community "
print output[48:]
ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', output )
ip0=ip[0]
network_len=ip0.rfind('.')
network=ip0[0:network_len]+".0/24"
print "Scanning for network ",network
nm = nmap.PortScanner()         # instantiate nmap.PortScanner object
nm.scan(hosts=network, arguments='-sn')
#hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
#for host, status in hosts_list:
#        print('{0}:{1}:{2}'.format(host, hostname, status))
print('----------------------------------------------------')
for host in nm.all_hosts():
        print('%s (%s) %s' % (host, nm[host].hostname(),  nm[host].state() ) )
print('----------------------------------------------------')
