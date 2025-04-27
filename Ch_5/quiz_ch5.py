
#5.1
car = 'subaru'
print("Is car == 'subaru'? I predict: True.")
print (car=='subaru')

sandwich = 'Ruben'
print('Is sandwich == ruben? I say: True!')
print (sandwich.lower() == 'ruben')


sport = 'hockey'
sports = ["hockey", "basketball", "golf"]
if sport not in sports:
    print(f"Sorry, but we don't consider {sport.upper()} a real sport.")
else:
    print(f"Congrats! We consider {sport.upper()} to be a real sport!")


#5.3 Alien Colors 1
alien_color = 'Green'
if alien_color.lower() == 'green':
    print("5 Points")

alien_color = "Purple"
if alien_color.lower() == 'yellow':
    print ("60 Points")
else:
    print ("Ship ain't Purple, my dude.")


# 5.4 Alien Colors 2:
alien_color = "Green"
if alien_color == "Green":
    print ("5 Points!")
elif alien_color != "Green":
    print ("Wrong Ship, Playa!")


alien_color = "Purple"
if alien_color == "Green":
    print ("5 Points!")
elif alien_color != "Green":
    print ("Wrong Ship, Playa!")


#5.4 Alien Colors 3:
alien_color = input ("Input alien color (Green, Yellow, Red): ")
alien_color = alien_color.title()
if alien_color == "Green":
    print ("5 Points!")
elif alien_color == "Yellow":
    print("30 Points")
elif alien_color == "Red":
    print("100 Points")





# 5.6 Stages of Life:
age = input ("Enter your age: ")
age = int(age)
if age < 2:
    print ("You are a baby.")
elif age <4:
    print ("You are a toddler")
elif age <19:
    print ("You are a Teenager")
elif age <65:
    print ("You are an adult")
elif age >= 65:
    print ("You are a senior. Congratulations. You made it. Much honor uppon you. (BOW)")


#5-7 Favorite Fruit
favorite_fruits = ['apple', 'pear', 'plumb']
if 'apple' in favorite_fruits:
    print ("Man, you really love apples.")
if 'pear' in favorite_fruits:
    print ("Boy! You sure do like pears!")
if 'plumb' in favorite_fruits:
    print ("Shoot! I din't know you loved dems plumbs!")

#import random section not in book
import random
random_agent = random.randint (0,6)

agents = ['gadget', 'oper', 'crane', 'cat', 'slither', 'fade', 'burrow']

print(f"Your random agent is: {random_agent}!")
print(f"For your next mission, you will work with agent {agents[random_agent].title()}!")

print ("Your name is " + input("What is your name? "))

# 5.8 Hello admin
users = ['chatles', 'barbararah', 'fat tony', 'admin', 'arthulio']
for user in users:
    if user == "admin":
        print(f"Good morning, {user.title()}! How would you like to proceed.")
    else:
        print(f"Hello {user.upper()}.")

#5.8.1 Using randomg enerator to take a random admin to print a greeting (not in book)
import random
random_user = random.randint (0,4)
users = ['chatles', 'barbararah', 'fat tony', 'admin', 'arthulio']
print (f"Your random user is: {users[random_user]}")
if users[random_user] == 'admin':
    print(f"\n\tHello {users[random_user].upper()}! It's good to see you again!")
else:
    print(f"\n\tOh, {users[random_user].title()}. It's you again.")


# 5.9
new_users = []
if new_users == []:
    print ("We need new users")

# 5.10 Checking User Names
current_users = ['penguinkilla02', 'gb0mB5', 'Al_Chemie', 'Mur_curie', 'alphalPhapug99']
new_users = ['Eyma5kamma', 'penguinkilla02', 'Al_Chemie', 'dopel_gangher','fartfignewton']
current_users_lower = []

for item in current_users:
    current_users_lower.append(item.lower())

print (current_users_lower)



for new_user in new_users:
    if new_user.lower() not in current_users_lower:
        print(f"Welcome to the club {new_user}!")
    else:
        print (f"We're sorry, but {new_user} is already taken.")


#5.11 Ordinal Numbers
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for number in numbers:
    if number == '1':
        print(f"{number}st")
    elif number == '2':
        print(f"{number}nd")
    elif number == '3':
        print(f"{number}rd")
    else:
        print(f"{number}th")


