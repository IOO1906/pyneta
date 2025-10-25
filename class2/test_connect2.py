from netmiko import ConnectHandler
from getpass import getpass

device = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
cmd = "show lldp neighbors detail"
output = net_connect.send_command(cmd)
print(output)
