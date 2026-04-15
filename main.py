from decimal import Decimal, InvalidOperation
def get_amount(prompt="Enter amount: "):
    while True:
        try:
            return Decimal(input(prompt))
        except InvalidOperation:
            print("Invalid number, try again.")

def prompt(text, pType):
    while True:
        try:
            return Decimal(input(text))
        except InvalidOperation:
            print("That's not a valid number format, please try again.")

if __name__ == "__main__":
    print("Hello, lets create your budget!\n")
    yearly = prompt("Yearly Income: \n",type(40000))
    monthly = yearly / 12
    print(f"Great! That's {monthly:.2f} a month!")