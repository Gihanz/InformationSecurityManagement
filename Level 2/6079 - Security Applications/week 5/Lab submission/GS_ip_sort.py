# =========================================================
# NAME:		GIHAN SHAMIKE LIYANAGE
# DATE:		SUMMER WEEK 5 2023
# Function	Lab 5 Code Solution
#		Python 3.11.3
#		WING Personal 9
# =========================================================

sh_list_file = "ipaddress_shuffled_list.txt"
sh_list_bin_file = "ipaddress_shuffled_list_bin.txt"
sorted_file = "GS_ipaddress_sorted.txt"

ipaddress_list =[]

# read ip addresses from ipaddress_shuffled_list.txt file and append to ipaddress_list
with open(sh_list_file,"r") as f:
    for line in f:
        ipaddress_list.append(line[:-1])
        
print("IP addresses of ipaddress_shuffled_list.txt added to ipaddress_list")

# read ip addresses from ipaddress_shuffled_list_bin.txt file and append to ipaddress_list        
with open(sh_list_bin_file, "r") as g:
    for line in g:
        b_ip_list = line[:-1].split(".")
        decimal_val_list = []
        
        for octet in b_ip_list:
            decimal_val_list.append(str(int(octet, 2))) # convert binary octets to decimal values and store in decimal_val_list
            
        decimal_ip = ".".join(decimal_val_list)      
        ipaddress_list.append(decimal_ip)
        
print("IP addresses of ipaddress_shuffled_list_bin.txt added to ipaddress_list")

# create GS_ipaddress_sorted.txt file and add File created by
with open(sorted_file, "w") as h:
    h.write("File created by Gihan Shamike Liyanage \n")
    
print("GS_ipaddress_sorted.txt file created")
    
# sort the list of ip addresses
ipaddress_list.sort()
print("Combined ipaddress_list sorted")

# write sorted ip addresses to GS_ipaddress_sorted.txt file
with open(sorted_file, "a") as h:
    for ipaddresses in ipaddress_list:
        h.write(ipaddresses + "\n")
        
print("Sorted ip addresses appened to GS_ipaddress_sorted.txt")