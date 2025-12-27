#=====================Chapter 8 Functions==================================

#________________Defining a Function________________
#Greet User

def greet_user():
    """Display a simple greeting"""
    print("Sup, playa.")

greet_user()

#Greet Specific user

def greet_specific(username):
    print(f"Sup, {username.title()}!")

greet_user()
greet_specific('sTONEY')#since this fxn has a paramater the call needs an arguement



#_________________Passing Arguments__________________
# Positional Arguemtns
def describe_pet(type, name):
    print (f"I have a(n) {type.upper()}.")
    print (f"My {type.title()}'s name is {name.title()}.")


describe_pet ("snake", "plissssskin")

#-----Code below jsut for flavor (flavor code)-----#
naming_pet = True

while naming_pet:
    animal = input("What type of animal do you have? ")
    name = input ("What is its name? ")

    describe_pet (animal, name)

    repeat = input("Do you have any more pets? y/n ")
    if repeat == 'n':
        naming_pet = False

print("\n\tThe naming loop has ended and this statment is proof.")




#_________________Keyword Arguments__________________

#no need to rewrite the function! Cool!

describe_pet (type = "snake", name = 'plissssskin')
 
#mess with order

describe_pet (name = "oscar", type = 'pig')







#_________________Default Valuses___________________

def describe_pet (name, type = 'dog'): #Type needs to be last bc of its default value
    print (f"I have a {type.upper()} and its name is {name.title()}.")
#ANY parameter with a default value MUST be last in the function. ie 'type' is now after 'name'

describe_pet ("charlie") #no type is needed

#================Flavor Code=========================
describe_pet ("rutherford", "cat") #type is needed because its a cat

#Messing with the order:
describe_pet(type = 'bird', name = "Harry")
#Order doesnt matter if using keyword arguments


#__________________Equivalent Function Calls____________________
# See previous Flavor Code








#+++++++++++++++++++RETURN VALUES++++++++++++++++++++

#---Returning a simple Value---

def get_formatted_name (first_name, last_name):
    full_name = f"{first_name.title()} {last_name.title()}" #needs to be in f-string w/o parenthesis bc it's not a print call
    return full_name.title()
    

formatted_name = get_formatted_name('kyle', 'stoney')
#functions with a returned value must have a variable to be assigned to (in this case 'formatted_name)
print (formatted_name)


#+_+_+_+_+_+_+_+_+_FLAVOR CODE_+_+_+_+_+_+_+_+_


new_users = {}
print (f"\n\tThis is the New Users Dictionary: {new_users}")

gathering = True
while gathering:
    first_input = input("\nType your FIRST name in lower case or upper case: ")
    last_input = input("Type your LAST name in upper or lower case: ")
    new_name = get_formatted_name (first_input, last_input)
    print (new_name)
#now lets try to add first and last name to a dictionary "new_users"
    first_title = first_input.title()
    last_title = last_input.title()
    new_users [last_title] = first_title


    repeat = input("Anyone else there? y/n ")
    if repeat == 'n':
        gathering = False

print (f"\n\tThis is the New Users List: {new_users}")

print ("This code is here to show that the previous code was successful.")



#+++++++++++++++++Making an Argument Optional++++++++++++++++++++

def get_formatted_name (first_name, last_name, middle_name =''):
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
        return full_name

    else:
        full_name = f"{first_name.title()} {last_name.title()}"
        return full_name

muscian = get_formatted_name ('harry', "hornswallow the third", 'hoosierdaddy')
print (muscian)

muscian = get_formatted_name ('patty', 'mc buttox')
#This is to show middle_name is optional
print(muscian)









#+++++++++++++++++++++ Returning a Dictionary +++++++++++++++++++++++++
#I tried to do this earlier. This way is less convoluted.
person = {'last': 'stoney', 'first': 'kyle'}
name ={}

print (f"\n\n\tThis is the Person list: {person}")
print (f"\tThis is the NAME list: {name}")


def build_person_dictionary (last_name, first_name):
    person = {'last':last_name.title(), 'first':first_name.title()}
    return person
name = build_person_dictionary('buttercup', 'ballsey')


print (f"\n\n\tThis is the NEW PERSON dictionary: {person}")
print (f"\tThis is the NEW NAME dictionary: {name}")

#____________Try to build a Dictionary with inputs______________

favorite_animal_dictionary= {}
print(f"This is proof favorite_animal_dictionary is empty: {favorite_animal_dictionary}")

inputting_active = True
while inputting_active:
    first_name = input("What is your first name? ")
    favorite_animal = input("What is your favorite animal? ")
    print (f"....adding {first_name} and {favorite_animal} to dictionary.")

    first_title = first_name.title()
    animal_title = favorite_animal.title()
    favorite_animal_dictionary [first_title] = animal_title

    deflag = input ("Any other inputs? y/n ")
    if deflag == 'n':
        inputting_active = False

print(f"Here's the new dictionary: {favorite_animal_dictionary}")


#++++++++++++++++++ Using "NONE" ++++++++++++++++++++++++++++++

def person_info (first_name, last_name, poodeepoo = None):
    """Return a dictionary about a person (Age optional)"""
    person = {'first':first_name.title(), 'last':last_name.title()}
    if poodeepoo:
        person ['Age'] = poodeepoo
    return person

musician = person_info ('kyle', 'stoney', 42)
print (musician)
musician_II = person_info ('max', 'noise')
print (musician_II)

#+++++++++++++++++ Using a function with a while loop +++++++++++++++++++

def get_user_info (first_name, last_name, quest):
    formatted_user_info = f"{first_name.title()}, {last_name.title()}, {quest}"
    return formatted_user_info

while True:
    print("Tell me about yourself, adventurer.")
    print('Press "q" to quit')

    f_name = input ("What is your first name? ") 
    if f_name == 'q':
        print("Thank you adventurer. Off you go.")
        break

    l_name = input ("What is your clan name? ")
    if l_name == 'q':
        print("Thank you adventurer. Off you go.")
        break

    quest = input ("What is your quest? ")
    if quest == 'q':
        print("Thank you adventurer. Off you go.")
        break
    
    name_quest = get_user_info (f_name, l_name, quest)
    print (f"Greetings, {name_quest}!")
    print (f"\nSalutations, {f_name} of the {l_name} clan! {quest.title()} "
           "is a noble quest indeed!")

#+++++++++++++++++ Passing a List +++++++++++++++++++++++

def greet_users (names):
    '''print as simple greeting to the users on this list'''
    for name in names:
        msg = f"Greetings adventurer, {name.title()}, fancy a pint?"
        print (msg)

user_names = ['hanna boltarion','jarnathon flapabilly', 'mortimere mysterio', 'vlax the wild']
greet_users (user_names)




#+++++++++++++++++++ Modifying a List in a Function ++++++++++++++++++++++++++++
"""Pass items from one list to another"""

def printed_models (unprinted_designs, completed_models):
    while unprinted_designs:
        printing = unprinted_designs.pop()
        print (f"\tPrinting '{printing.title()}' design, now")
        completed_models.append(printing)


def show_completed_models (completed_models):
    for model in completed_models:
        msg = (f"\t\tFinished printing model: {model.upper()}")
        print (msg)



unprinted_designs = ['airplane', 'trumpet', 'telephone', 'tree']
completed_models = []

"""Here are the lists before"""
print (f'\n Here are the unprinted_design items: {unprinted_designs}')
print (f"And here are the completed_models items: {completed_models}")


"""Here are the calls"""
printed_models (unprinted_designs, completed_models)
show_completed_models (completed_models)


"""Here are the lists AFTER"""
print (f'\n Here are the unprinted_design items: {unprinted_designs}')
print (f"And here are the completed_models items: {completed_models}")




#+++++++++++++++++ Passing an Arbitrary Number of Arguments ++++++++++++++++++++

def make_pizza (*toppings):
    print ('Now adding the following toppings:')
    for topping in toppings:
        print (f"\t-{topping.upper()}")


make_pizza ('cheese', 'pepperoni')
make_pizza ("cheese", "ham", 'bacon', 'pineapple', 'jalapeno', 'extra cheese')




#+++++++++++++++++++ Mixing Positional and Arbitrary Arguements ++++++++++++++++

def make_pizza (size, crust,  *toppings):
    print (f"Making {size.upper()} {crust.upper()}-crust pizza with:")
    for topping in toppings:
        print (f"-{topping.title()}")


make_pizza ('large', 'stuffed', 'cheese', 'extra bacon', 'jalapeno')
make_pizza ("medium", 'pan', 'peperoni', 'olives', 'bacon', 'fetta')



#++++++++++++++++++++++++ Using Arbitrary Keyword Arguments ++++++++++++++++++++

def build_profile (first, last, **user_info):
    user_info ['First'] = first
    user_info ["Last"] = last
    return user_info


user_profile = build_profile ('kyle', 'stoney', state ='washington', job ='arff', aspiration ='game design',
                              current_activity = 'testing', not_that_but = 'this', it_is = 'out of here!')
print (user_profile)
















































































































