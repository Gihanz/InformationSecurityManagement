#   Author    Fanshawe
#   Date      February 2020 Week 7
#             Example002.py
#   -------------------------------------
#   import module
import ipaddress as ip

#functions
def network_info(ip_address, subnet):
    ip_sub = ip_address + "/" + subnet
    #sub = ipaddress.IPv4Network(ip_sub)
    sub = ip.IPv4Network(ip_sub)
    return sub

def get_hosts(subnet):
    #hosts = list(ipaddress.IPv4Network(subnet).hosts())
    hosts = list(ip.IPv4Network(subnet).hosts())
    return hosts

