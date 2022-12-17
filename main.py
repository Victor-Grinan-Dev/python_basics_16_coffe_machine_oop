from day_16_coffee_machine_OOP.menu import Menu, MenuItem
from day_16_coffee_machine_OOP.coffee_maker import CoffeeMaker
from day_16_coffee_machine_OOP.money_machine import MoneyMachine


def coffee_machine():
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()

    while True:
        choice = input(f"choose a damned coffee {menu.get_items()}")
        coffee = menu.find_drink(choice)
        if choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif choice == 'off':
            return

        elif choice in menu.get_items():
            if coffee_maker.is_resource_sufficient(coffee):
                if money_machine.make_payment(coffee.cost):
                    coffee_maker.make_coffee(coffee)
            else:
                print("insuficient resources")
        else:
            print("⚠️choice not found! Please", end=" ")


if __name__ == "__main__":
    coffee_machine()
