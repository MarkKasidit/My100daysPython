from utils import menu as mn
resources = mn.resources
menus = mn.MENU
is_on = True
profit = 0

def check_sources():
    for ing, val in required.items():
        if resources[ing] < val:
            print(f"Sorry there is not enough {ing}.")
            return False
    return True

def process_coin():
    quarters = int(input("How much quarters?: "))
    dimes = int(input("How much dimes?: "))
    nickles = int(input("How much nickles?: "))
    pennies = int(input("How much pennies?: "))
    return quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01

def make_coffee():
    for ing, val in required.items():
        resources[ing] -= val
    print(f"Here is your {choice}. Enjoy!")

def charge_back(pay, cost):
    change = pay - cost
    if change > 0:
        print(f"Here is ${change} dollars in change.")

while is_on:
    choice = input("“What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")

    elif choice in menus:
        required = menus[choice]["ingredients"]
        if not check_sources():
            continue
        print("Please insert coin...")
        pay = process_coin()
        if pay < menus[choice]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            continue
        make_coffee()
        charge_back(pay, menus[choice]["cost"])
        profit += menus[choice]["cost"]
