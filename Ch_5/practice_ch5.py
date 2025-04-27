cars = ['ram', 'bmw', 'dodge', 'toyota', 'honda']

cars.sort()

for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car== 'ram':
        print("rAAAAm-a-lamma-ding-dong")
    else:
        print (car.title())


toppings = ['mushrom', 'peperoni', 'sausage', 'bacon']
for topping in toppings:
    if topping != "anchovies":
        print(f"Add {topping.title()}")

if "anchovies" not in toppings:
    print("\tHold the anchovies!!!")

answer = 1
if answer == 19:
    print("Great job!")
else:
    print("What a loser! Try again!")




banned_users = ['phillip', 'james', 'price']
user = "marjorie"
if user not in banned_users:
    print(f"{user.title()}, you may enter the chat.")




#age = input("Enter your age : ") I turned this off to test run without interruption.
#age = int(age)
age = 69
if age < 4:
    price = 0.00
elif age < 19:
    price = 18.00
elif age <65:
    price = 28.00
elif age >= 65:
   price = 0.00

print (f"Your admission cost is ${price}. Have a great time!")


pizza_toppings = []
if pizza_toppings:
    for topping in pizza_toppings:
        print (f"Adding {topping.title()}")
    print("End of Topping List")
else:
    print("Is you sure you want a plain pizza?")



requested_toppings = ['bacon', 'ham', 'extra cheese', 'pineapple']

available_toppings = ["peperoni", "jalapenos", "ham", "bacon", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping.title()}")
    else:
        print(f"Sorry, we do not have {requested_topping.title()}.")
print("Done making your crappy pizza!")

'''
Is this a comment, too?
We'll see
'''
'''Yes it is a comment!'''









































































