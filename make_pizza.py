def make_pizza(*toppings):
    print("here are your orders in pizza : ")
    for topping in toppings:
        print("you order : "+topping)
def user_info(**users):
    for v,k in users.items():
        print(v+" "+k)