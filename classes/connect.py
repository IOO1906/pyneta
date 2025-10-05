from netmiko import ConnectHandler

device = {
    'host' = '1.1.1.1',
    'device_type': 'cisco_ios',
    'username': 'cisco',
    'password': getpass(),
}

net_connect = ConnectHandler(**device)

print(net_connect.find_prompt()

