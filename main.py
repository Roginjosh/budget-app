from decimal import Decimal, InvalidOperation
def get_amount(prompt="Enter amount: "):
    while True:
        try:
            return Decimal(input(prompt))
        except InvalidOperation:
            print("Invalid number, try again.")

def prompt(text):
    while True:
        try:
            return Decimal(input(text))
        except InvalidOperation:
            print("That's not a valid number format, please try again.")

class Budget:
    def __init__(self):
        self.income = {}
        self.needs = {}
        self.wants = {}

    def add_income(self):
        print("Lets add an income source.")
        name = input("Enter a name for this income source:\n")
        occurances = prompt("How many times per year do you receive this money?\n")
        amount = prompt("How much?\n")
        self.income[name] = {
            "occurances":occurances,
            "amount":amount,
        }

    def update(self):
        self.net_income = 0
        for key in self.income:
            self.net_income += self.income[key]["amount"] * self.income[key]["occurances"]
    
    def __str__(self):
        self.update()
        rtn = f"+++++ Your Budget +++++\nTotal Income: {self.net_income:.2f}\n"
        for key in self.income:
            rtn += key + " : " + str(self.income[key]["amount"]) + "\n"
        return rtn



if __name__ == "__main__":
    myBudget = Budget()
    while True:
        op = input(
            "\
What operation would you like to do?\n\
Send 1 for adding income.\n\
Send 2 for adding expenses.\n\
Send 3 to see the state of your budget.\n"
        )
        op = int(op)
        if op == 1:
            myBudget.add_income()
        if op == 3:
            print(myBudget)

    """
    print("Hello, lets create your budget!\n")
    yearly = prompt("Yearly Income: \n",type(40000))
    monthly = yearly / 12
    print(f"Great! That's {monthly:.2f} a month!")
    """