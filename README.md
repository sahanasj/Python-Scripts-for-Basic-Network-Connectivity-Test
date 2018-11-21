# Sahana's Python Scripts for Smoke Testing (Basic Network Connectivity, Servers status Tests..)

## Verified Python Scripts

| Script | Description |
|--------|-------------|

| [ping-test-using-csv.py](https://github.com/sahanasj/Python-Scripts-for-Basic-Network-Connectivity-Test-Smoke-Test-Scripts-/blob/master/ping-test-using-csv.py)<br> | Import the list of IP-address/Hosts from CSV file and then check the list of servers for network reachability using PING tool |
| [1-ping-test-using-csv-output.PNG](https://github.com/sahanasj/Python-Scripts-for-Basic-Network-Connectivity-Test-Smoke-Test-Scripts-/blob/master/Python-Scripts-Example-Outputs/1-ping-test-using-csv-output.PNG)<br> | Example output of ping test using csv file import|

| [generic-ping-test.py](https://github.com/sahanasj/Python-Scripts-for-Basic-Network-Connectivity-Test-Smoke-Test-Scripts-/blob/master/generic-ping-test.py)<br> | Check for the list of servers to ensure the server is up and running and network reachability using PING tool based on the platform dependent! |
| [2-list-of-servers-ping-test-output.PNG](https://github.com/sahanasj/Python-Scripts-for-Basic-Network-Connectivity-Test-Smoke-Test-Scripts-/blob/master/Python-Scripts-Example-Outputs/2-list-of-servers-ping-test-output.PNG)<br> | Example output of ping test using python dictionary|

| [ping-test-using-dict.py](https://github.com/sahanasj/Python-Scripts-for-Basic-Network-Connectivity-Test-Smoke-Test-Scripts-/blob/master/ping-test-using-dict.py)<br> | Check the list of servers from python Dictionary for network reachability using PING tool |
| [3-ping-test-using-dict-output.PNG](https://github.com/sahanasj/Python-Scripts-for-Basic-Network-Connectivity-Test-Smoke-Test-Scripts-/blob/master/Python-Scripts-Example-Outputs/3-ping-test-using-dict-output.PNG)<br> | Example output of ping test|

| [socket-program-for-server-status-check.py](https://github.com/sahanasj/Python-Scripts-for-Basic-Network-Connectivity-Test-Smoke-Test-Scripts-/blob/master/socket-program-for-server-status-check.py)<br> | Socket programming for connecting two nodes/servers on a network to communicate with each other. |
| [4-socket-program-output.PNG](https://github.com/sahanasj/Python-Scripts-for-Basic-Network-Connectivity-Test-Smoke-Test-Scripts-/blob/master/Python-Scripts-Example-Outputs/4-socket-program-output.PNG)<br> | Example output of socket program to check server ALIVE|


# Getting Started
<details>
<summary>Quick Install</summary>

```
*** Install dependencies (with virtualenv) ***
$ sudo apt-get -y install virtualenv or sudo yum install virtualenv
$ virtualenv smoke-test
$ source smoke-test/bin/activate

*** Create a Python Script ***
$ server-status-check.py  #example

*** Run the Python Script ***
$ python server-status-check.py

or

*** Run the Python Script and store output in text file ***
$ python server-status-check.py >> output.txt
```
</details>

# Cloud Custodian Important Resources
[Python socket network programming](https://pythontips.com/2013/08/06/python-socket-network-programming/)<br>
[Default Port Numbers You Need to Know as an Administrator](https://geekflare.com/default-port-numbers/)<br>
[TCP/IP Ports and Sockets Explained](http://www.steves-internet-guide.com/tcpip-ports-sockets/)<br>
[Python Socket Programming – Server, Client Example](https://www.journaldev.com/15906/python-socket-programming-server-client)<br>
[Socket Programming in Python (Guide)](https://realpython.com/python-sockets/)<br>



