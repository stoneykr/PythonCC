magicians = ["Houdini", "Penn & teller", "david blaine", "david copperfield"]
for magician in magicians:
    print(f"\n\t{magician}")
print (magicians)

#sort the list then print again

magicians.sort()#Not working. List maintains order
for magician in magicians:
    print (f"\n\t\t{magician.title()}")

print (magicians)
#IDK why .sort() doesn't work but .sort(reverse=True) does??? Oh well.

for magician in magicians:
    print(f"\t{magician.title()}, that was a great trick!")
    print(f"\tI can't wait to see {magician.title()}'s next trick!\n")

print ("Thanks all for playing!")


#Numbers: Off by one

for value in range (-2, 5):
    print (value)
    print(f"\t {value}")

for value in range(5):
    print(value)


numbers = list(range(65, 70))
#Two different types of ouputs:
# 1:
print(numbers)

# 2:
for number in numbers:
    print (number)

#number lists (first=start, second=end, third=multiple)
evens = list(range(2, 22, 2)) 
#If second is 20, output is 18. If 21 or 22, output is 20 *OFF BY 1!
print (evens)
thirds = list(range(3, 31, 3))
print (thirds)
for third in thirds:
    print(f"\n\t{third}")

#generating numbers into list
squares = ['Empty Squares List']
print(squares)
del squares[0]
for value in range(1, 11):
   square = value **2
   squares.append(square)
   print(square)

print(squares)


#List comprehension does the same thing more efficiently
cubes = [value **3 for value in range(1, 11)] #<--- list comprehension
print(f"\t {cubes}")
for cube in cubes:
    print(f"\t{cube}")



#Slicing a list
players=["chahtles", 'mellisa', 'tandy', 'carol', 'erica', 'dingoatemybaby']
print(players[4:])
print(players[:3])
print(players[1:6:2])
print(players[:-2])
print(players[-2:])
for player in players[:-3]:
    print(player.title())
for player in players[-3:]:
    print (player.upper())


#Copying a list:
#       #The following code associates two variable names to the same list.
#       #If you append one, you append the other, etc.
team_a = players
print (team_a)

players.append("Obideskie")
print(players)
print (team_a)

        #However to copy and create a SEPARATE list, do the following
        #using the '[:]' copies players to team_a as a new list
team_a = players[:]
        #printing them makes the same list
print("\n\nThe lists are the same for now.")
print (f"\n\t{team_a}")
print (f"\t{players}")
players.append("Magic Mike")
team_a.append("Kal Hoon")
        #BUT when we append each list differently then print to see the results, we see each list is different
            #Same-same... but different!
print("\nThe lists have been appended differently to show they are separate lists:")
print (f"\n\t{team_a}")
print (f"\t{players}")


















































