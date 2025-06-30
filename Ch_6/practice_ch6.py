""""
Chapter 6 Dictionaries
"""
alien_0 = {'color': 'green', 'points': 5, 'speed': "slow"}

print (alien_0['color'])
print (alien_0['points'])
print (alien_0['speed'])

alien_0_color = alien_0['color']
alien_0_points = alien_0['points']
print(f"You just shot down a {alien_0_color} alien ship! {alien_0_points} to Griffendor!")


"""Adding Key Value Pairs DesiredDictionary['Key'] = 'Value' """

print (alien_0)

alien_0 ['x-position'] = 4
alien_0 ['y-position'] = 25

print (alien_0)


"""Starting with blank Dictionary"""
alien_1 = {} #Start with empty dictionary 
#MUST INCLUDE = SIGN!!!

print (alien_1)

alien_1 ['color'] = 'Blue'
alien_1 ['points'] = 10
alien_1 ['speed'] = 'Medium'

print(alien_1) #Dictionary now full





"""Changing Key's Values"""

alien_0 = {'color': 'green', 'points': 5, 'speed': 'medium', 'x-position': 4, 'y-position': 25}
print (f"Your alien is at X-Position: {alien_0['x-position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0 ['speed'] == 'medium':
    x_increment = 5
else:
    x_increment = 10

alien_0 ['x-position'] = alien_0 ['x-position'] + x_increment

print(f"Now your alien is at X-Position: {alien_0['x-position']}")




"""Deleting KVP's"""

print (alien_0)

del alien_0['speed']

print (alien_0)

#Add it back in
alien_0 ['speed']='fast'

print(alien_0)



"""Dictionaries to store one kind of inforamtion about many objects"""

favorite_languages = {
    'jen':'python', # Remember the COMMA ,
    'kyle': 'rust',
    'sarah': 'C++',
    'jacoby': 'ruby', #He's a bit weird
}
print(favorite_languages)
print (f"Sarah's favorite language is {favorite_languages['sarah']}.")

"""Attempt to add to favorite_languages"""
favorite_languages ['emily'] = 'rust'
print(favorite_languages)

favorite_languages ['david'] = 'python'
print(favorite_languages)



"""Using get() to access values if you thinkg that the Key/Value might not exist"""

spin_factor = alien_0.get('spin factor', 'No spin factor assigned')
print (spin_factor)

"""This avoids errors^^^"""


color = alien_0 ['color']
print (color)



"""Looping Through a Dictionary"""

for name, language in favorite_languages.items():
    print(f"\n {name.title()}'s favorite language is {language.title()}.")
    print(name.upper())
    print(language.upper())




"""Looping through all the Keys""" #Use.keys() or nothting instead of .items()
#looping through just the keys is the default so '.keys()' isn't necessary.... but do it anyway.

for key in favorite_languages.keys():
    print(key.title())

super_friends= ['kyle', 'emily']

for friend in favorite_languages.keys():
    print (friend.upper())
    if friend in super_friends:
        language= favorite_languages [name].title()
        print(f"Oh hi {name.title()}, I see your favorite language is {language.title()}!")




"""Looping through a dictionary's keys in a particular order"""
#Use the sorted() fxn and add the dictionary within the parenthesis 


for name in sorted(favorite_languages.keys()):
    print (f"{name.title()}, thank you for taking the poll!")




"""Looping through all the Values in a dictionary"""
#Use the .values() method

print("The following languages have been mentioned by our pollees:")
for value in favorite_languages.values():
    print(value.upper())


#Use .set() instead of .values() if you don't want to see repeats of the same values

print("The following languages have been mentioned by our pollees:")
for value in set(favorite_languages.values()):
    print(value.upper())













































































