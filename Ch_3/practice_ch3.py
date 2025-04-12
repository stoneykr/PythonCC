bicycles = ['trek', 'mongoose', 'schwinn', 'redline', 'cannondale']
print (bicycles)

for bike in bicycles:
    print (f"\n\t {bike.title()}")

print(bicycles [0].title() )

print(bicycles [-1].upper())

message = f"I always wanted a {bicycles[1].title()}, but my mom couldn't afford it. Also, It was a waste of money."

print(message)

poop_mc_dinglefart = f"{bicycles[2].upper()} is a good bike, too, though."
print (poop_mc_dinglefart)



motorcycles = ['ducati', 'yamaha', 'kawasaki']
print (motorcycles)

motorcycles.append("suzuki")
print (motorcycles)

motorcycles.insert(3,"buel") #Insert NEEDS the position argument.
print(motorcycles)

popped_motorcycle = motorcycles.pop(2)
print (motorcycles)
print (popped_motorcycle)

motorcycles.insert(2, popped_motorcycle)
print(motorcycles)


first_owned = motorcycles.pop(1)
print(f"The first motorcycle I owned was a {first_owned.upper()}")
print (motorcycles)
motorcycles.insert(1, first_owned)
print(motorcycles)


cars = ['ram', "bmw", 'audi', 'honda', 'toyota', 'ford', 'dodge']
print (cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)




print("Here's the OG list:")
cars = ['ram', "bmw", 'audi', 'honda', 'toyota', 'ford', 'dodge']
print(cars)

print("Here's the sortED list\n")

print(sorted(cars))

print("Back to OG:\n")
print(cars)

print("Reverse = True list:\n")
print(sorted(cars, reverse=True))

print(cars)

cars.reverse()
print(cars)

cars.reverse()
print (cars)

print(len(cars))








































