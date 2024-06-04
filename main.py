menu = {
    "Espresso": {
        "ingredients": {
            "Water": 50,
            "Coffee": 18,
            "Milk": 0,
        },
        "cost": 1.50

    },
    "Latte": {
        "ingredients": {
            "Water": 200,
            "Coffee": 24,
            "Milk": 150
        },
        "cost": 2.50
    },
    "Cappuccino": {
        "ingredients": {
            "Water": 250,
            "Coffee": 24,
            "Milk": 100
        },
        "cost": 3.00
    }
}

resources = {
    "Water": 300,
    "Coffee": 100,
    "Milk": 200
}

penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25
profit = 0


def is_resource_sufficient(par):
    for item in resources:
        if resources[item] < menu[par]["ingredients"][item]:
            print(f"Sorry, there's not enough {item}")
            return False
        else:
            return True


def manage_resources(par):
    global profit
    for item in resources:
        resources[item] -= menu[par]["ingredients"][item]
    profit += menu[par]["cost"]


def print_report():
    for item in resources:
        print(f"{item}: {resources[item]}")
    print(f"Profit: {profit}")
    run_machine()


def run_machine():
    order = input("What would you like to order?(Espresso/ Cappuccino/ Latte): ")

    if order == "off":
        print("Thank you for using the machine! Bye!")
        exit(0)

    elif order == "report":
        print_report()

    elif order not in menu:
        print("We currently do not have that item, please order again: ")
        run_machine()

    else:
        if is_resource_sufficient(order):
            cost = menu[order]["cost"]
            money_in = (quarter * int(input("How many quarters?: ")) + dime * int(input("How many dimes?: ")) +
                        nickel * int(input("How many nickels?: ")) + penny * int(input("How many pennies?: ")))
            if money_in >= cost:
                manage_resources(order)
                change = money_in - cost
                if change > 0:
                    print(f"Here's ${change:.2f} in change.")
                print(f"Here's your {order}, enjoy!")
                yn = input("Would you like to order again?(y/n): ")
                if yn == "y":
                    run_machine()
                else:
                    pass
            else:
                print("Insufficient funds, try again.")
                run_machine()
        else:
            run_machine()


run_machine()
