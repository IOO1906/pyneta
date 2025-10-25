from netmiko import ConnectHandler
from getpass import getpass

device = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
cmds = [
    "show version",
    "show lldp neighbors"
]
output = {cmd: net_connect.send_command(cmd, use_textfsm=True) for cmd in cmds}
print(f"On ", output["show version"][0]["hostname"], ", the remote device's interface is: ", output["show lldp neighbors"][0]["neighbor_interface"])
