from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

device1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    #"fast_cli": True,
}

device2 = {
   "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    #"fast_cli": True,
}

devices = [
    device1,
    device2,
]

for device in devices:
    net_connect = ConnectHandler(**device)
    result = net_connect.send_command("show vlan br", use_textfsm=False,
                                       strip_prompt=False, strip_command=False)
    print("----------------------------")
    print("Result before config changes")
    pprint(result)
    print("----------------------------")
    net_connect.send_config_from_file(config_file="config_commands.txt")
    net_connect.save_config()
    result = net_connect.send_command("show vlan br", use_textfsm=False, 
                                       strip_prompt=False, strip_command=False)
    print("----------------------------")
    print("Result after config changes")
    pprint(result)
    print("----------------------------")
