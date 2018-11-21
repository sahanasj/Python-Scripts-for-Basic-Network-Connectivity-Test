"""
/* Developer:SahanaJayaram, email:sjayaramu@eplus.com */
"""

import socket # for socket
import sys

try:
    """
    Reserve a port on your computer
    Refer for Default Ports: https://geekflare.com/default-port-numbers/
    & http://www.steves-internet-guide.com/tcpip-ports-sockets/
    """
    port = 80 # Port to listen on (non-privileged ports are > 1023)

    # List of Servers/Hosts
    hosts_to_test = [
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.185.66',
        '10.1.185.71',
        '10.1.185.77',
        '10.1.185.78',
        '10.1.185.75'
    ]

    # Iterate the Serevrs/Hosts list
    for hostname in hosts_to_test:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host_ip = socket.gethostbyname(hostname)
        print "Socket successfully created to connect Server: " + host_ip

        # connecting to the server
        s.connect((host_ip,port))

        # binds it to a specific ip and port; listen to incoming requests
        # s.bind(host_ip, port)

        # server to listen to incoming connections
        # s.listen(5)

        # send some data through a socke
        s.sendall(b'Hello, world')

        # receive data from the server
        #data = s.recv(1024)
        while True:
            data = s.recv(1024)
            if not data:
                break
            s.sendall(data)

        #print "The socket has successfully connected to with port == %s" %(host_ip)
        print "A Server is ALIVE! -" ,host_ip
        print "\n"

except socket.error:
    # this means could not resolve the host
    print "** There was an error resolving the host **", host_ip
    print "A Server looks like DOWN!"
    print "\n"
    # sys.exit()

    # close the connection
s.close()
