"""
/* Developer: SahanaJayaram, email: sjayaramu@eplus.com */
"""

import os
servers = {"10.1.185.71", "10.1.185.66", "10.1.185.89"}

for vm in servers:
    print "---- Trying to Ping a Server with IPAddress ----", vm
    response = os.system("ping -c 1 " + vm)
    #and then check the response...
    if response == 0:
        print "***********************************"
        print(vm, 'is UP!')
        print "***********************************"
        print "\n"
    elif response == 2:
        print "***********************************"
        print(vm, 'is DOWN and No response from Server!')
        print "***********************************"
        print "\n"
    else:
        print "***********************************"
        print(vm, 'is DOWN!')
        print "***********************************"
        print "\n"
