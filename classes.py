import csv


class Item:
    payRate = 0.8

    all = []

    def __init__(self, name: str, price: float, quantity: int):
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Price {quantity} is not greater than zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    def calculateTotalPrice(self):
        return self.price * self.quantity

    def applyDiscount(self):
        self.price = self.price * Item.payRate

    @classmethod
    def instantiateFromCSV():
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(Item)

    def __repr__(self):
        return f"Item({self.name},{self.price},{self.quantity})"
