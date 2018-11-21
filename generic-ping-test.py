"""
/* Developer: SahanaJayaram, email: sjayaramu@eplus.com */
"""

import os
import platform
import subprocess

plat = platform.system()

def ping_return_code(hostname):
    """Use the ping utility to attempt to reach the host. We send 5 packets
    ('-c 5') and wait 3 milliseconds ('-W 3') for a response. The function
    returns the return code from the ping utility.
    """
    try:
        if plat == "Windows":
            # Checking for Windows Servers
            response = subprocess.call(['ping', '-n', '5', '-W', '3', hostname],
                                       stdout=open(os.devnull, 'w'),
                                       stderr=open(os.devnull, 'w'))
        elif plat == "Linux":
            # Checking for Linux Servers
            response = subprocess.call(['ping', '-c', '5', '-W', '3', hostname],
                                       stdout=open(os.devnull, 'w'),
                                       stderr=open(os.devnull, 'w'))


        print "Verify a host" + " " + '"' +  hostname + '"' + " " + "for Network Reachability using PING Tool"
        print "---- Trying to Ping a Server with IPAddress ----", hostname
        # Check for response status code, Ping Success code is '0'
        if response == 0:
            print "********************************************************************"
            print(hostname, 'is UP and reachable!')
            print "********************************************************************"
            print "\n"
        elif response == 1 or 2 or 256 or 512:
            print "********************************************************************"
            print(hostname, 'is DOWN and No response from Server!')
            print "********************************************************************"
            print "\n"
    except Exception:
            print "********************************************************************"
            print(hostname, 'is DOWN and Host Unreachable!')
            print "********************************************************************"
            print "\n"
    return response


def verify_hosts(host_list):
    """For each hostname in the list, attempt to reach it using ping. Returns a
    dict in which the keys are the hostnames, and the values are the return
    codes from ping. Assumes that the hostnames are valid.
    """
    return_codes = dict()
    for hostname in host_list:
        return_codes[hostname] = ping_return_code(hostname)
    return return_codes


def main():
    # List of IP-address/Hosts for Ping test
    hosts_to_test = [
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '192.168.1.159',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.63',
        '10.1.185.64',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.78',
        '10.1.185.80',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.82',
        '10.1.185.83',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.90',
        '10.1.185.92',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.51',
        '10.1.185.52',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.185.53',
        '10.1.185.56',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1',
        '10.1.185.71',
        '10.1.185.62',
    ]
    verify_hosts(hosts_to_test)

if __name__ == '__main__':
    main()
