from netmiko import ConnectHandler
from getpass import getpass
import time

device = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "secret": getpass("Secret:"),
    "session_log": "my_output.txt",
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
net_connect.config_mode()
print(net_connect.find_prompt())
net_connect.exit_config_mode()
print(net_connect.find_prompt())
net_connect.write_channel("disable\r")
time.sleep(2)
print(net_connect.read_channel())
net_connect.enable()
print(net_connect.find_prompt())
