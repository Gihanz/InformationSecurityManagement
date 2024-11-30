#   Author    Fanshawe
#   Date      February 2020 Week 7
#             Example003.py
#   -------------------------------------
#   import module
from ipaddress import IPv4Network

#functions
def network_info(ip_address, subnet):
    ip_sub = ip_address + "/" + subnet
    #sub = ipaddress.IPv4Network(ip_sub)
    sub = IPv4Network(ip_sub)
    return sub

def get_hosts(subnet):
    #hosts = list(ipaddress.IPv4Network(subnet).hosts())
    hosts = list(IPv4Network(subnet).hosts())
    return hosts