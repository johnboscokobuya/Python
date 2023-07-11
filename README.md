# Python For Automation
Prequisite
Linux mint, github account, github branch
install  python3.10, pip3, netmiko, git, vscode

#Cisco Sandbobox for Cisco lab 
Assigned into the account and reserved sandbox
Used Cisco Anyconnect for VPN
Used Netmiko COnnectHandler to remotely connect Cisco CSR IOS XE 8000 and display ip status interface 

##Prompt user to enter username and password of remote without exposing SSH details
 -Import getpass from netmiko, ConnectHandler
 -Define username using python input, password and username under device paramaters
 -Use try and exception to capture error
