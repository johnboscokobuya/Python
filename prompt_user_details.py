from netmiko import ConnectHandler
from getpass import  getpass

# Prompt the user for logging credentials
username = input("Username: ")
password = getpass("Password: ")

# Define the device details
device = {
    'device_type': 'cisco_ios',
    'ip': '10.10.20.48',
    'username': username,
    'password': password,
}

# Connect to the device
try:
    connection = ConnectHandler(**device)
    # Perform your operations here
    print("Successfully connected to the device.")
    connection.disconnect()
except Exception as e:
    print("An error occurred:", str(e))
