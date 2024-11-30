#   Author    Fanshawe
#   Date      February 2020 Week 7
#             Example001.py
#   -------------------------------------
#   import module
import ipaddress

#functions
def network_info(ip_address, subnet):
    ip_sub = ip_address + "/" + subnet
    sub = ipaddress.IPv4Network(ip_sub)
    return sub

def get_hosts(subnet):
    hosts = list(ipaddress.IPv4Network(subnet).hosts())
    return hosts

sub = network_info('10.10.0.0','24')
print(sub)
print("Network ID : " ,sub.network_address)
print("Broadcast : " , sub.broadcast_address)
print("Netmask : " , sub.netmask)
host = get_hosts(sub)
print("Hosts : " , end=" ")
for ip in host:
    if ip == host[-1]:
        print(ip)
    else:
        print(ip , end=", ") 
