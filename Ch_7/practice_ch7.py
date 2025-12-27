message = input("Tell me something and I'll repeat it back to you. ")
print (message)


name = input("What is your name? ")
print (f"Hello, {name.title()}! How are you?")



prompt = ("If you tell me where you're from, I'll send you a greeting. ")
prompt+= ("What city are you in? ")

city = input (prompt)
print (f"Helooooo {city.upper()}!!! What's dooin'? What's hap'nin?!")

prompt2 = ("Now, tell me how old you are. ")
age = input(prompt2)
age = int(age)
if age >20:
    print(f"YO! You can drink, {name.title()}!")
else:
    print(f"Too bad you can't drink, {name.title()}.")





#Introducing WHILE LOOPS! p.117

current_number = 1
while current_number <= 5:
    print (current_number)
    current_number += 1




#Letting the user choose when to quit: p.118 


prompt ='\nTell me something, and I will repeat it back to you: '
prompt +="\n Enter 'Red' when you are finished "
message = ""
while message != "Red":
    message = input(prompt)
    if message != "Red": #Add this if statment so that "QUIT" is not printed when "QUIT" is inputted.
        print (message)

if message == "Red":
    print ("Thank you. Come again.")





#Using a Flag p. 120
#added a response to the prompt. Had to create var.'reply' to make ==quit work
#Then added another condition 'fart' and 'qwert'. This simulates various other ways to make a game end or do somethingelse


prompt = "\n\t What kind of guns do you like? "
prompt += "\n\t Type 'quit' to quit. "

active = True
while active:
    reply = input(prompt)
    message = (f"\n WOW! I love {reply.title()}s, too!")
    message1 = ("I'm on to you. GAME OVER, MAN!!!")
    if reply == 'quit':
        active = False
    elif reply == 'fart':
        print(message1)
    elif reply == 'qwert':
        active = False
    else:
        print (message)




#Using a BREAK to exit a loop p.121

prompt = "What is a city you have been to? "
prompt += "\n press 'fade' to quit. "

while True:
    city = input (prompt)

    if city == 'fade':
        break
    else:
        print (f"Wow. {city.title()} seems cool!")





#Using CONTINUE in a loop p.122

current_number = 0 # = 0 NOT == 0

while current_number < 10:
    current_number += 1 #add the counter here to count b4 if stmnt.

    if current_number % 2 == 0:
        continue #add 'continue here
   
    print (current_number)



#============USING A WHILE LOOP WITH LISTS AND DICTIONARIES===================


#Moving items from one list to another p.124
#-----Start with users list and a list for them to go into:

new_users = ['tom', 'dick', 'harry']
verified_users = []


#print for proof
print(f"\nNew users list: {new_users}")
print(f"Verified users {verified_users}")

new_name = "fartification" #appended the list
new_users.append(new_name)#must append b4 while loop otherwise it wont run. See line 142

print(new_users)

#verify each user and put in verified_users list
while new_users:
    verifying_users = new_users.pop().title()
    print(f"\n\tVerifying user: {verifying_users}")
    verified_users.append(verifying_users)

#print proof of list change
print(f"\nNew users list: {new_users}")
print("The follwoing users have been confirmed:")
for user in verified_users:
    print (user.title())
#Loop won't function if you append here



#----Filling a Dictionary with a user input
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat's your name? ")
    quest = input ("What is your quest? ")

    responses[name] = quest


    say_again = input("\n Are there more in your party, yes/no ")
    if say_again == "no":
        polling_active = False

print("\n\t=====Poling Results=====")
for name, quest in responses.items():
    print(f"{name.title()}'s quest is to {quest}. Good luck!!!")

















































