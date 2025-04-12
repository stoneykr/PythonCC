#3-1
friends = ['tom', 'dick', 'harry', 'baradun', 'greg', 'bob']
print (friends [0])
print (friends [1])
print (friends [2])
print (friends [3])
print (friends [4])
print (friends [5])

for friend in friends:
    print(friend.upper())


#3-2
for friend in friends:
    print(f"'Ello there, gubbna! Would {friend.upper()} like a spot of tea?")


#3-3
vehicles = ['truck', 'bus', 'motorcycle', 'car']
for vehicle in vehicles:
    print(f"I have had a {vehicle.title()} before.")


#3-4 Dinner guests
guests = ['baradun', 'greg', 'bob', 'bodger']
for guest in guests:
    print(f"Hello, {guest.title()}, come over for dinner.")

canceled = guests.pop(0)
guests.insert(0, 'laythill')
new_guest = guests[0]
print(f"I'm sorry to inform you all, but {canceled.upper()} cannot make it to dinner.")
print(f"However, {new_guest.upper()} will be joining us instead.")
print (guests)



#3-5 Moar guests
guests.insert(0, 'barbara')
guests.insert(3, "tanja")
guests.append('hoodie')
for guest in guests:
    print(f"{guest.title()} Found bigger table, {guests[0]}, {guests[3]}, and {guests[6]} will be joining us.")

print(guests)


#3-8
places = ['grand canyon', 'dolomites', 'antarctica', 'mt. rushmore', 'old faithful']
print(places)

print(sorted(places))

print(places)

places.reverse()
print(places)


places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)






































































