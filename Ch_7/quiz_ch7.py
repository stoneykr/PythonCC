#7-1. Rental Car 
prompt = ("What kind of car are you thinking about renting? ")

rental = input(prompt)
print(f"Let me see if I have a {rental.title()}.")


#7-2. Restaurant Seating
party = input ("How many people are in your party? ")
party = int(party)

if party > 7:
    print(f"You'll have to wait 40 minutes for a party of {party}.")
else:
    print (f"Since you only have {party} in your party, we can seat you right away.")


#7.3 Multiples of ten:
tenprompt = input("Tell me a number and I'll see if it's divisible by ten. ")
tenprompt = int(tenprompt)
if tenprompt % 10 == 0:
    print(f"{tenprompt} is indeed a multiple of 10.")
else:
    print (f"{tenprompt} is, infact, NOT a multiple of ten. You idiot.")


#7-4. Pizza Toppings: 

pizzatops =  "What'll I add to your pizza? "
pizzatops += 'Write "fed" to quit. '  

while True:
    topping = input(pizzatops)

    if topping == 'fed':
        break
    else:
        print (f"Adding {topping.upper()} to your pizza!")



#7-5. Movie Tickets

prompt = "\nTell me your age, and I'll state the price of admission. "
prompt += "Type '999' when done "

while True: 

    inpt_age = input(prompt)
    age = int(inpt_age)
#These prompts needed to be inside the while loop. The book has them outside
# without them being inside the loop, the loop infinately loops
    if age == 999:
        break
    elif age < 3:
        price = "Free"
        print (f"Your ticket is {price}.")
        
    elif age < 12:
        price = "$10"
        print (f"Your ticket is {price}.")
    else:
        price = "$15"
        print (f"Your ticket is {price}.")
    


#7-6. 3 versions of 7-5 or 7-4
#I've already done most of these in my previous code above. I will not repeat
#Use an "active" variable is the one I haven't done yet.


prompt = "\n Who goes there? "
prompt += "\n Type 'stop' to stop. "
active=True
while active:
    adventurer = input(prompt)
    
    if adventurer == "stop":
        active = False
    else:
        print(f"\n\tWelcome, {adventurer.title()}. Your journey awaits!")



#7-7. Endless loop press Ctl-C
#code blocked out for ease of running but remove "#" and you'll see it works.


#number = 1

#while True:
    #print (number)
    #number += 1






#7-8.
sandwich_orders = ['pastrami', 'ham and cheese', 'tuna', 'ruben', 'pastrami', 'chicken', 'pastrami', 'italian']
finished_sandwiches =[]

#remove pastrami with a message:
if 'pastrami' in sandwich_orders:
    print("----Sorry, no pastrami. Please make a new order----")

while 'pastrami'in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print(f"\n\t I'm making your {making_sandwich.title()} sandwich!")

    finished_sandwiches.append(making_sandwich)

print ("\n ========Here are the Finished Sandwiches===========")
for sandwich in finished_sandwiches:
    print(f"I have finished making your {sandwich.title()} sandwich. Enjoy!")

        



#7-10 Dream Vacation

vacation_results = {}
vacation_active = True

while vacation_active:

    name = input("What is your name? ")
    vacation = input("Where is your dream vacation? ")

    vacation_results [name] = vacation

    repeat = input("Would anyone else like to go? y/n ")
    if repeat == "n":
      vacation_active = False

for name, vacation in vacation_results.items():
    print(f"\t{name.title()} would like to go to {vacation.title()}")

















































