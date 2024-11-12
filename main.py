from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
money_machine.report()
coffee_maker.report()
menu = Menu()
is_on = True
while is_on:
    option = menu.get_items()
    choice = input(f"what do you like: {option}")
    if choice == "off":
        is_on = "False"
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if(coffee_maker.is_resource_sufficient(drink)) and (money_machine.make_payment(drink.cost)):
            print(coffee_maker.make_coffee(drink))
