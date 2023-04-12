import sys

class Item:
    def __init__(self, itemA, itemB):
        self.itemA = itemA
        self.itemB = itemB

    def calculate(self):
        try:
            print(f"Sum: \t\t{self.itemA + self.itemB}")
            print(f"Difference: \t{abs(self.itemA - self.itemB)}")
            print(f"Product: \t{self.itemA * self.itemB}")
            print(f"Quotient: \t{self.itemA / self.itemB}")
            print(f"Reminder: \t{self.itemA % self.itemB}")
        except ZeroDivisionError:
            print(f"Quotient: \tError (division by zero)")
            print(f"Remainder: \tError (modulo by zero)")

if len(sys.argv) == 3:
    try:
        itemA = int(sys.argv[1])
        itemB = int(sys.argv[2])
        item = Item(itemA, itemB)
        item.calculate()
    except ValueError:
        print("AssertionError: only integers.")
elif len(sys.argv) > 3:
    print("AssertionError: too many arguments.")
else:
    print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
