water = 400
milk = 540
beans = 120
cups = 9
cash = 550


def change_qt(w=0, m=0, b=0, cp=0, csh=0):
    global water, milk, beans, cups, cash
    water += w
    milk += m
    beans += b
    cups += cp
    cash += csh


def print_stat():
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(beans, "of coffee beans")
    print(cups, "of disposable cups")
    if cash == 0:
        print(cash, "of money")
    else:
        print("$", cash, "of money")
    print()
    start()


def buy_coffee():
    print()
    types_of_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n ")
    if types_of_coffee == "1":
        if water < 250 or beans < 16 or cups == 0:
            print("Sorry, not enough water!")
            print()
            start()
        else:
            print("I have enough resources, making you a coffee!")
            change_qt(w=-250, m=0, b=-16, cp=-1, csh=4)
            print()
            start()
    if types_of_coffee == "2":
        if water < 350 or milk < 75 or beans < 20 or cups == 0:
            print("Sorry, not enough water!")
            print()
            start()
        else:
            print("I have enough resources, making you a coffee!")
            change_qt(w=-350, m=-75, b=-20, cp=-1, csh=7)
            print()
            start()
    if types_of_coffee == "3":
        if water < 200 or milk < 100 or beans < 12 or cups == 0:
            print("Sorry, not enough water!")
            print()
            start()
        else:
            print("I have enough resources, making you a coffee!")
            change_qt(w=-200, m=-100, b=-12, cp=-1, csh=6)
            print()
            start()
    if types_of_coffee == "back":
        print()
        start()


def fill_machine():
    print()
    change_qt(w=int(input('Write how many ml of water do you want to add:\n ')))
    change_qt(m=int(input('Write how many ml of milk do you want to add:\n ')))
    change_qt(b=int(input('Write how many grams of coffee beans do you want to add:\n ')))
    change_qt(cp=int(input('Write how many disposable cups of coffee do you want to add:\n ')))
    print()
    start()


def remaining():
    print()
    print_stat()


def take_money():
    print()
    print("I gave you $", cash, sep="")
    change_qt(csh=-cash)
    print()
    start()


def start():
    command = input('Write action (buy, fill, take,remaining,exit):\n ')
    if command == "buy":
        buy_coffee()
    elif command == "fill":
        fill_machine()
    elif command == "take":
        take_money()
    elif command == "remaining":
        remaining()
    elif command == "exit":
        exit()


def exit():
    print()
    quit()


start()