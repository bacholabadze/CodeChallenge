MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def process_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies?: "))
    return 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies


def is_transaction_successful(money_inserted, item):
    if item['cost'] <= money_inserted:
        resources['money'] += item['cost']
        change = money_inserted - item['cost']
        if change:
            change_formatted = "{:.2f}".format(change)
            print(f"Here is ${change_formatted} dollars in change.")
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded {money_inserted}.")
        return False


def make_coffee(coffee):
    for item in coffee['ingredients']:
        resources[item] -= coffee['ingredients'][item]


is_machine_on = True

while is_machine_on:
    print('\n\n\nHello!')
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_machine_on = False
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            money = process_coins()
            if is_transaction_successful(money, drink):
                make_coffee(drink)
                print(f'Here is your {choice} ☕. Enjoy!')
