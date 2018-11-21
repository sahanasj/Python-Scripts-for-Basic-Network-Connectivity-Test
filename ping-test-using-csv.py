"""
/* Developer: SahanaJayaram, email: sjayaramu@eplus.com */
"""

import csv
import os
import platform

plat = platform.system()

#server = "localhost"     #example for single host
#servers = {"10.1.185.71", "10.1.185.66", "10.1.185.89"}     # example of Host/IPaddress using Dictionary

# Import the list of hosts/servers/ipaddress from CSV file
with open('ipaddress-list.csv', 'r') as servers_list:
    servers = csv.DictReader(servers_list)
    for vm in servers_list:
        print "---- Trying to Ping a Server with IPAddress ----", vm
        
        # Check for Windows and Linux Platforms
        if plat == "Windows":
            response = os.system("ping -n 1 " + vm)
            pass

        elif plat == "Linux":
            response = os.system("ping -c 1 -W 3 " + vm)
            pass

        # Check for response status code
        if response == 0:
                print "********************************************************************"
                print(vm, 'is UP and reachable!')
                print "********************************************************************"
                print "\n"
        elif response == 2 or 256 or 512:
                print "********************************************************************"
                print(vm, 'is DOWN and No response from Server!')
                print "********************************************************************"
                print "\n"
        else:
                print "*********************************************************************"
                print(vm, 'is DOWN and Host Unreachable!')
                print "*********************************************************************"
                print "\n"
