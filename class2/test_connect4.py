from netmiko import ConnectHandler
from getpass import getpass

device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "fast_cli": True,
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())

cmds = [
    "ip name-server 1.1.1.1",
    "ip name-server 1.0.0.1",
    "ip domain-lookup",
]

output =  net_connect.send_config_set(cmds)
output += net_connect.send_command("ping google.com", 
                                    strip_prompt=False, strip_command=False)
print(output)
