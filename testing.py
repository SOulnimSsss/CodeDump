import csv
from classes import Item

item1 = Item("Bazooka", 200, 12)
item2 = Item("Uzi", 1000, 15)
item3 = Item("Rocket", 500, 5)
item4 = Item("Banana", 150, 23)
item5 = Item("Kambing", 2000, 5)

Item.instantiateFromCSV()
