
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


def compare():
    print("Please insert coins.")
    quarter = int(input("How mnany quarters? : "))*0.25
    dime = int(input("How mnany Dime? : "))*0.10
    penny = int(input("How mnany Penny? : "))*0.01
    nickel = int(input("How mnany Nickel? : "))*0.05
    return(quarter+dime+penny+nickel)

def check_resource(coffe_choice):
        drink = MENU[coffe_choice]["ingredients"]
        for item in drink:
            if drink[item] >= resources[item]:
                print("Sorry that's not enough money. Money refunded.")
    
        total = compare()
        coffe_cost = (MENU[coffe_choice]["cost"])

        if total > coffe_cost:

            print(f"Here is ${round(total - coffe_cost, 2)} in change")
            print(f"Here is your {coffe_choice} . Enjoy!")
    
            


choose = input("What would you like? (espresso/latte/cappuccino): ").lower()


check_resource(choose)
   