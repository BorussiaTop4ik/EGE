from ipaddress import *
for m in range(33):
    net = ip_network(f'154.201.208.17/{m}', 0)
    if '154.201.192.0' in str(net):
        print(net.netmask)

