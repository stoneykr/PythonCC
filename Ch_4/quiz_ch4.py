# 4-1 Pizza...favorite pizza
favorite_pizza = ['hawaiian', "bacon, pepperoni, and olive", 'sausage']
for pizza in favorite_pizza:
    print(f"I often order {pizza} pizza.")
print('\tI really love pizza')

# 4-2 Animals
animals = ['cat', 'dog', 'chicken']
for animal in animals:
    print (f"A {animal} is an animal you'd find on a farm, typically.")
print("\tI have been attacked by each of them at one point in time in my life.")



#4-3 counting to 20
twenty = [value +1 for value in range(0, 20)]
print(twenty)
for digit in twenty:
    print(digit)


#4-4 Million. Will block this off to keep file small
million = range(0, 1000000)
#for digit in million:
    #print (digit)


#4-5 summing million
print (f'The minimum in a list from 0 to one million is {min(million)}')
print (f"The maximum in a list from 0 to one million is {max(million)}")
print (f"The SUM of numbers from 0 to one million is {sum(million)}!")

# 4-6
thirds = (range(1, 20, 3))
for third in thirds:
    print (third)

# 4-7
threes = [value*3 for value in range(1, 11)]
for third in threes:
    print(f"\t {third}")

# 4-8/9
cubes =[value**3 for value in range(1, 11)]
for cube in cubes:
    print (cube)



# 4-10 Slicing through a previous list:
favorite_pizza = ["hawaiian", "bacon, pepperoni, and olive", "sausage", "jalapenos", "bell peppers", "onion"]
print(f"The first three items of my fav pizza are: ")
print(favorite_pizza [0:3])

print("The middle items in my pizza list are:")
print(favorite_pizza[2:4])

print("the last items on my pizza list are:")
print(favorite_pizza[4:6])

# 4-11
friends_pizza = favorite_pizza[:]
del friends_pizza[1:3]
friends_pizza.append('anchovies')
print("\nThis is my pizza list:")
print(f"\t{favorite_pizza}")
print("\nThis is my friends pizza list:")
print(f"\t{friends_pizza}")


# 4-12 For loop for a list
for pizza in favorite_pizza:
    print(f"\t{pizza.upper()}")


























































