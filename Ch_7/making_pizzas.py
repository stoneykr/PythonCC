
def make_pizza (size, crust,  *toppings):
    print (f"Making {size.upper()} {crust.upper()}-crust pizza with:")
    for topping in toppings:
        print (f"-{topping.title()}")
