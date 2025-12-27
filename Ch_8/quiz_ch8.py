#=====================Chapter 8 Functions==================================
from functions import build_profile

#8-1. Message

def display_message():
    print ("This lesson is teaching me about functions.")

display_message()



#8-2. Favorite Book

def fav_book(book):
    print (f"{book.title()} is your favorite book. Cool.")

prompt = input ("What is your favorite book? ") #I added the prompt for flavor

fav_book(prompt)



#8-3. T-Shirt

def make_shirt(size, text):
    print (f'Make a {size} sized shirt with "{text}" written on it.')

#8-3 a call with positional arguments
make_shirt('large', 'Who farted?')
#8-3 b call with keyword arguments
make_shirt(text="I've lost my marbles", size = "medium")


#8-4 Modify make_shirts
def make_shirts(text = 'I love Python', size = "large"):
    print (f"\Make {size} sized shirts with '{text.upper()}' written on it")

make_shirts()
make_shirts(size = "medium")
make_shirts(text = "I'm with Stoopid. ==>")



#8-5 Describe City
def describe_city (city, country = "the USA"):
    print(f"\t{city.title()} is in {country}.")

describe_city('houston')
describe_city('seattle')
describe_city('london', country = "England.")




# 8-6. City names

def city_country (city, country):
    city_country = f"{city.title} {country}"
    return city_country

while True:
    print("Tell me about your location.")
    print ('Press "q" to quit.')

    city = input ("What is your city? ")
    if city == 'q':
        print ("ok see you later")
        break
    country = input ("What country is that in? ")
    if country == 'q':
        print ("Ok see you later.")
        break
    
    print (f"Cool. You lince in {city.title()} which is in the contry of"
           f" {country.title()}")

# 8.7 & 8  ____ Album & User Album______
#I'm combining these since I've been adding while loops to these questions and I didn't need to

def make_album (artist, album):
    artist_name = f"{artist.title()}"
    album_name = f"{album.title()}"
    album_dict = {'artist': artist_name, 'album': album_name}
    return album_dict

while True:
    print ("Lets talk music, shall we?")
    print ("Press 'q' to quit")

    artist = input ("Tell me an artist/band name: ")
    if artist == 'q':
        break
    album = input("What is one of their albums? ")
    if album == 'q':
        break

    response = make_album (artist, album)
    print (f"Here is the dictionary: {response}")






# 8-9 Messages


txt_msgs = ["Hello! Havardi?", "BRB", "See you in 10", "DUCK YOU!!!"]

def show_messages (messages):
    for msg in messages:
        print (msg)


show_messages (txt_msgs)




# 8-10 Sending Messages


txt_msgs = ["Hello! Havardi?", "BRB", "See you in 10", "DUCK YOU!!!"]
sent_msgs = []
print (f"Here is txt_msgs: {txt_msgs}")
print (f"Here is sent_msgs: {sent_msgs}")


def send_messages (messages):
    for msg in messages:
        print (msg)

    while messages:
        text_message = txt_msgs.pop()
        sending_notification = f"Sending {text_message} to its destination."
        sent_msgs.append(text_message)

send_messages (txt_msgs)



print (f"Here is txt_msgs: {txt_msgs}")
print (f"Here is sent_msgs: {sent_msgs}")






# 8-10 / 8-11 Sending Messages


txt_msgs = ["Hello! Havardi?", "BRB", "See you in 10", "DUCK YOU!!!"]
sent_msgs = []
print (f"Here is txt_msgs: {txt_msgs}")
print (f"Here is sent_msgs: {sent_msgs}")


def show_messages (messages):
    for msg in messages:
        print (msg)


    while messages:
        text_message = messages.pop()
        sending_notification = f"Sending {text_message} to its destination."
        sent_msgs.append(text_message)

show_messages (txt_msgs[:])



print (f"Here is txt_msgs: {txt_msgs}")
print (f"Here is sent_msgs: {sent_msgs}")





# 8-12 Sandwiches

def sandwich_maker (bread, *ingredients):
    print (f"Making your {bread.title()} sandwich with: ")
    for ingredient in ingredients:
        print (f"\t-{ingredient.upper()}")


order1 = sandwich_maker('white', 'tuna', 'dill relish', 'cheddar cheese')
order2 = sandwich_maker('rye', 'pastrami', 'saurkraut', 'provolone cheese', 'swiss cheese')




# 8-13. User Profile +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def build_profile (first, last, **user_info):
    user_info ['First'] = first
    user_info ["Last"] = last
    return user_info


user_profile = build_profile ('kyle', 'stoney', state ='washington', job ='arff', aspiration ='game design',
                              current_activity = 'testing', not_that_but = 'this', it_is = 'out of here!')
print (user_profile)



# 8-14 Cars

def cars (make, model, **features):
    features ['Make'] = make
    features ["Model"] = model
    return features

my_car = cars ('subaru', 'crosstrek', color = 'grey', trim = "Limited", sunroof = False,
               remote_start = True)

print (my_car)























































