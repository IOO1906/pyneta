from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
output = net_connect.send_command_timing("ping")
output += net_connect.send_command_timing("\r")
output += net_connect.send_command_timing("8.8.8.8")
output += net_connect.send_command_timing("\r")
output += net_connect.send_command_timing("\r")
output += net_connect.send_command_timing("\r")
output += net_connect.send_command_timing("\r")
output += net_connect.send_command_timing("\r")
print(output)
