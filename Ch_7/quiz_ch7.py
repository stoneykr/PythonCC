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






















































































