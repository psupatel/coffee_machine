from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine_obj = MoneyMachine()
coffee_maker_obj = CoffeeMaker()
menu_obj = Menu()


is_on = True
while is_on:
    choice = menu_obj.get_items()
    order = input(f"What would you like? {choice}: ")
    if order == "off":
        is_on = False
    if order == "report":
        coffee_maker_obj.report()
        money_machine_obj.report()
    else:
        drink = menu_obj.find_drink(order)
        if coffee_maker_obj.is_resource_sufficient(drink) and money_machine_obj.make_payment(drink.cost):
            coffee_maker_obj.make_coffee(drink)