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






























































































