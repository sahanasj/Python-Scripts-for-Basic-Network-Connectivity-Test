# Sahana's Python Scripts for Smoke Testing (Basic Network Connectivity, Servers status Tests..)

## Verified Python Scripts

| Script | Description |
|--------|-------------|
| [ping-to-hosts.py](https://github.com/sahanasj/cloudcustodian-policies/blob/master/mailer.yml)<br> | Check the list of servers for network reachability using PING tool |

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
```
</details>

# Cloud Custodian Important Resources
[Python socket network programming](https://pythontips.com/2013/08/06/python-socket-network-programming/)<br>
[Default Port Numbers You Need to Know as an Administrator](https://geekflare.com/default-port-numbers/)<br>
[TCP/IP Ports and Sockets Explained](http://www.steves-internet-guide.com/tcpip-ports-sockets/)<br>
[Python Socket Programming – Server, Client Example](https://www.journaldev.com/15906/python-socket-programming-server-client)<br>
[Socket Programming in Python (Guide)](https://realpython.com/python-sockets/)<br>



