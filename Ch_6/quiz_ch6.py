# 6-1 Person
emily = {'city': 'hong kong', 'last name': 'sardinola', 'age': '36'} 
print (emily)

#6-2 Favorite Numbers
favorite_numbers= {
    'kyle': 25,
    'kelly': 42,
    'jimmy': 21,
    'djeoph': 9,
    'mc geehee': 13,
}

print(f"Kyle's favorite number is {favorite_numbers['kyle']}")
print(f"Kelly's favrite number is {favorite_numbers['kelly']}")

# 6-3 Dictionary glossary
glosary= {'API': 'Application Programming Interface', 'Request': 'allows a Python program to easily requst information from a website an examine the response'}

print(f"One term I learned is API. It stands for {glosary['API']}.")
print (f" \n Another term I learned is 'Request' which {glosary['Request']}.")



# 6-4 Glossary 2
glossary_2= {'big': 'small', 'black': 'white', 'left': 'right', 'fish': 'bird', 'fire': 'water', 'up': 'down', 'a': 'b'}

for key in glossary_2.keys():
    print(key.title())

for term in glossary_2.values():
    print(f"\t {term.upper()}")


# 6-5 Rivers

rivers= {'nile':'egypt', 'mississippi': 'usa', 'amazon': 'brazil', 'colorado': 'usa'}
for k,v in rivers.items():
    print(f"\nThe {k.title()} river runs in {v.title()}.")

for river in rivers.keys():
    print(river.title())

for country in set(rivers.values()):
    if country == 'usa':
        print (country.upper())
    else:
        print(country.title())


# 6-6 People who SHOULD take the poll:
people_poll= ['emily', 'kyle', 'kelly', 'jimmy', 'mc geehee', 'djeoph', 'carl', 'orville']

for person in people_poll:
    if person in favorite_numbers.keys():
        print(f"\nThank you, {person.title()} for taking the poll. Your number was recorded.")
    else:
        print(f"\nHow about you go fuck yourself, {person.title()}! Next time take the fucking poll.")




































































