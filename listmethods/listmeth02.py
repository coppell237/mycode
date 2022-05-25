#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print("proto after extend proto2: ", proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print("protoa after append proto2: ", protoa)
# insert an item at a given position list.insert(i, x)
proto.insert(0, "hostname")
# remove the last item on the list
proto.pop()
print("proto after insert to position 0 and remove the last item", proto)

