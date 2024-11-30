import ipaddress

'''
asking user to enter IPaddress with prefix, Notice there is no spaces.
Yes! We need to create a try, except to make sure it is correct.
If you want to keep asking until correct need to put it in a loop. 
'''
u_address = input("Enter an IPv4 address with cidr (x.x.x.x/cidr): ")
host = ipaddress.IPv4Interface(u_address)

#getting the Network ID of the enterd ip address and cidr 
network = host.network
print(network)

#creating a ipaddress.ip_network  object 
net_object = ipaddress.ip_network(network)

# creating a variable with network ID
network_id = net_object.network_address  
broadcat = net_object.broadcast_address
'''
Getting avalable host address. We use
num_addresses variable wich holds the value
of all the address including network ID and 
Broadcast. This mean we take off 2
'''
usable_host = net_object.num_addresses -2
print("Usable Host:",usable_host)

print("netmask:",net_object.netmask)
print("Broadcast:",net_object.broadcast_address)
print("Network address: ",net_object.network_address)
print("First address: ", net_object[1])
print("Last address:",net_object[-2])