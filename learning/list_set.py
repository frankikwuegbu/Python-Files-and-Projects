#LISTS: syntax and operations
devices_list = ["router", "switch", "firewall"]
print(devices_list)
print(devices_list[1])  #lists allow for subscription, which allows you isolate any of its elements using index

#looping through a list
for devices in devices_list:
    print(devices)

#adds elements to a list
devices_list.append("router")
print(devices_list)

#removes the firs occurence of an element from a list
devices_list.remove("router")
print(devices_list)

#converting a list to a set
list_to_set = set(devices_list)
print(list_to_set)



#SETS: syntax and operations
devices_set = {"router", "switch", "firewall"}
print(devices_set)
for device in devices_set:
    print(device)

#add elements to a set
devices_set.add("pcs")
print(devices_set)

#remove element from a set
devices_set.remove("switch")
print(devices_set)