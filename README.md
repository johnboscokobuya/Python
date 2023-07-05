# Python For Automation
Prequisite
Linux mint, github account, github branch
install  python3.10, pip3, netmiko, git, vscode

#Cisco Sandbobox for Cisco lab 
Assigned into the account and reserved sandbox
Used Cisco Anyconnect for VPN
Used Netmiko COnnectHandler to remotely connect Cisco CSR IOS XE 8000 and display ip status interface 

##Output of show ip int brief using netmiko
john@JohnBosco:~/netmiko_Python3$ python3 main.py 
p int brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up      
GigabitEthernet2       unassigned      YES NVRAM  administratively down down    
GigabitEthernet3       unassigned      YES NVRAM  administratively down down    
john@JohnBosco:~/netmiko_Python3$ python3 main.py 
