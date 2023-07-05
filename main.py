from netmiko import ConnectHandler

CSR = {
  "device_type":"cisco_ios",
  "ip":"10.10.20.48",
  "username":"developer",
  "password":"C1sco12345"
}
net_connect = ConnectHandler(**CSR)
net_connect.enable()
output = net_connect.send_command('sh ip int brief')
print(output)

net_connect.disconnect