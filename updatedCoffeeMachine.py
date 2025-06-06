
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resource(elements):
    for item in elements:
        if elements[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
        
    return True
    
def process_coins():

    print("Please insert coin.")
    total = int(input("How many quartes? : "))*0.25
    total += int(input("How many dimes? : "))*0.10
    total += int(input("How many nickels? : "))*0.05
    total += int(input("How many pennies? : "))*0.01
    return total

def transaction(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} to change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry thats not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_elements):
    for item in order_elements:
        resources[item] -= order_elements[item]
    print(f"Here is your {drink_name}.")

is_on = True

while is_on:
    choose = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choose == "off":
        is_on = False
    
    elif choose == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money : ${profit}")

    else:
        drink = MENU[choose]
        if check_resource(drink["ingredients"]):
            payment = process_coins()
            if transaction(payment, drink["cost"]):
                make_coffee(choose, drink["ingredients"])
                


