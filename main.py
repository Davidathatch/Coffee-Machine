liveResources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 100,
    "money": 2.5,
}


# Used when printing report or exiting to bypass the stock check, whcih comes before saleSession loop
class defaultForm:
    def __init__(self):
        self.name = "default"
        self.water = 0
        self.milk = 0
        self.coffee = 0
        self.cost = 0.0


# Recipe data for each of three drinks
class latteForm:
    def __init__(self):
        self.name = "latte"
        self.water = 200
        self.milk = 150
        self.coffee = 24
        self.cost = 3.0


class espressoForm:
    def __init__(self):
        self.name = "espresso"
        self.water = 50
        self.milk = 0
        self.coffee = 18
        self.cost = 1.5


class cappuccinoForm:
    def __init__(self):
        self.name = "cappuccino"
        self.water = 250
        self.milk = 100
        self.coffee = 24
        self.cost = 2.5


# Prints out liveResources
def resourceReport():
    print(f'Water: {liveResources["water"]} ml')
    print(f'Milk: {liveResources["milk"]} ml')
    print(f'Coffee: {liveResources["coffee"]} g')
    print(f'Money: {liveResources["money"]}')


# Deducts resources from liveResources depending on chosen drink
def resourceDeduct(drinkForm):
    liveResources["water"] -= drinkForm.water
    liveResources["milk"] -= drinkForm.milk
    liveResources["coffee"] -= drinkForm.coffee


# Returns true if in stock, false if not
def resourceCheck(drinkForm):
    if liveResources["water"] >= drinkForm.water and drinkForm.name != "default":
        if liveResources["milk"] >= drinkForm.milk:
            if liveResources["coffee"] >= drinkForm.coffee:
                return True
    return False


# Calculates the change to vend to user and updates liveResources. Returns -1 if not enough money is given
def calcChange(pennyIns, nickelIns, dimeIns, quarterIns, drinkForm):
    total = 0.0
    total += ((pennyIns * .01) + (nickelIns * .05) + (dimeIns * .1) + (quarterIns * .25))
    round(total, 2)
    drinkcost = round(drinkForm.cost, 2)
    if total == drinkForm.cost:
        liveResources["money"] += drinkcost
        return 0.0
    elif total > drinkForm.cost:
        liveResources["money"] += drinkcost
        return round(total - drinkcost, 2)
    else:
        return -1


# While true it will allow you to buy coffee until enter "exit"
cashierMode = True
while cashierMode:
    chosenDrink = input("Enter desired drink (espresso, latte, cappuccino): ")
    chosenDrinkObj = None
    purchaseSession = True
    # Choosing drink, report, or exit
    if chosenDrink == "espresso" or chosenDrink == "Espresso":
        chosenDrinkObj = espressoForm()
    elif chosenDrink == "latte" or chosenDrink == "Latte":
        chosenDrinkObj = latteForm()
    elif chosenDrink == "cappuccino" or chosenDrink == "Cappuccino":
        chosenDrinkObj = cappuccinoForm()
    elif chosenDrink == "report":
        resourceReport()
        purchaseSession = False
        chosenDrinkObj = defaultForm()
    elif chosenDrink == "exit":
        cashierMode = False
        purchaseSession = False
        chosenDrinkObj = defaultForm()

    # Checks if chosen drink is in stock
    if not resourceCheck(chosenDrinkObj):
        print("Sorry, we are out of stock")
        purchaseSession = False

    # If you chose a drink rather than function (report or exit)
    if purchaseSession:
        # Enter in cash paid
        print(f'Selected item costs {chosenDrinkObj.cost}')
        insertPenny = input("Number of pennies: ")
        insertNickel = input("Number of nickels: ")
        insertDime = input("Number of dimes: ")
        insertQuarters = input("Number of quarters: ")
        changeResult = calcChange(float(insertPenny), float(insertNickel), float(insertDime), float(insertQuarters),
                                  chosenDrinkObj)
        # If paid more than price print change returned and coffee ordered
        if changeResult > 0.0:
            print(f'Here is your change: {changeResult}')
            print(f'And here is your {chosenDrinkObj.name} ☕!')
            resourceDeduct(chosenDrinkObj)
        # If paid exact price only print coffee ordered
        elif changeResult == 0.0:
            print(f"Here is your {chosenDrinkObj.name} ☕!")
            resourceDeduct(chosenDrinkObj)
        # If not paid enough print the error
        else:
            print("Sorry, not enough money")
