"""
/* Developer: SahanaJayaram, email: sjayaramu@eplus.com */
"""

import os
servers = {"10.1.185.71", "10.1.185.66", "10.1.185.89"}

for vm in servers:
    print "---- Trying to Ping a Server with IPAddress ----", vm
    # Check for Windows and Linux Platforms
    if plat == "Windows":
        response = os.system("ping -n 1 " + vm)
        pass

    elif plat == "Linux":
        response = os.system("ping -c 1 -W 3 " + vm)
        pass

    #and then check the response...
    if response == 0:
        print "***********************************"
        print(vm, 'is UP!')
        print "***********************************"
        print "\n"
    elif response == 2 or 256 or 512:
        print "***********************************"
        print(vm, 'is DOWN and No response from Server!')
        print "***********************************"
        print "\n"
    else:
        print "***********************************"
        print(vm, 'is DOWN!')
        print "***********************************"
        print "\n"
