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
output = net_connect.send_command("ping", expect_string=r'ip')
output += net_connect.send_command("\r", expect_string=r'address')
output += net_connect.send_command("8.8.8.8", expect_string=r'count')
output += net_connect.send_command("\r", expect_string=r'size')
output += net_connect.send_command("\r", expect_string=r'seconds')
output += net_connect.send_command("\r", expect_string=r'commands')
output += net_connect.send_command("\r", expect_string=r'sizes')
output += net_connect.send_command("\r", expect_string=r'Sending')
print(output)
