
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# print(MENU["espresso"]["cost"])
def compare():
    print("Please insert coins.")
    quarter = int(input("How mnany quarters? : "))
    dime = int(input("How mnany Dime? : "))
    penny = int(input("How mnany Penny? : "))
    nickel = int(input("How mnany Nickel? : "))

    quarter *= 0.25
    dime *= 0.10
    penny *= 0.01
    nickel *= 0.05
    return(quarter+dime+penny+nickel)

  


choose = input("What would you like? (espresso/latte/cappuccino): ").lower()

if choose == "espresso":
    total=compare()
    # print(total)
    coffe_cost = (MENU["espresso"]["cost"])
    if total > coffe_cost:
        print(f"Here is ${total - coffe_cost} in change")
        print("Here is your espresso. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")

elif choose == "latte":
    total=compare()
    # print(total)
    coffe_cost = (MENU["latte"]["cost"])
    if total > coffe_cost:
        print(f"Here is ${total - coffe_cost} in change")
        print("Here is your latte. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")

elif choose == "cappuccino":
    total=compare()
    # print(total)
    coffe_cost = (MENU["cappuccino"]["cost"])
    if total > coffe_cost:
        print(f"Here is ${total - coffe_cost} in change")
        print("Here is your cappuccino. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")



