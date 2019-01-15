# create at 01-04 16:29
guests = ["zhangsan", "lisi", "wangwu"]
print(guests)

up_index = 1
no_guest = guests.pop(up_index)
print(no_guest + " can't go to the party")

guests.insert(up_index, "zhaoliu")
print(guests[up_index] + " will joined the party")

print("the new list is " + str(guests))

print("\r\nGood news: we find a bigger dining-table")
guests.insert(0, "laoqi")
guests.insert(2, "laoba")
guests.append("laojiu")
print("the three list is " + str(guests))

print("\rI`m so sorry, the new dining-table cannot be served on time,  We can only invite two \r")
del_guest = guests.pop()
print(del_guest + "will be cancel the invitation \r")
del_guest = guests.pop(-2)
print(del_guest + "will be cancel the invitation \r")
del_guest = guests.pop(-3)
print(del_guest + "will be cancel the invitation \r")

