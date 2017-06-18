# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

import operator
import csv

# Displays the inventory.
def display_inventory(inventory):
    total = 0
    print("Inventory: ")
    for keys, values in inventory.items():
        print(values, keys)
        total += values

print("Total number of items: %d" % total)


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, addedItems):
    for i in range(len(addedItems)):
        inventory.setdefault(addedItems[i], 0)
        inventory[addedItems[i]] = inventory[addedItems[i]] + 1
    return inventory


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory):
    print("Inventory:")
    print("{:>3} {:>11}".format("count", "item name",))
    print("-----------------")
    item_total = 0
    for key, value in inventory.items():
        print("{:>3}".format(str(value)) + "{:>14}".format(str(key)))
        item_total += value
    print("-----------------")
    print("Total number of items: " + str(item_total))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, import_i="import_inventory.csv"):
    with open(import_i, "r") as import_inventory:
        reader = csv.reader(import_inventory)
        your_list = list(reader)
        for i in your_list:
            addToInventory(inventory, i)
    return inventory


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv", multirows=False):
    with open(filename, "w") as f:
        w = csv.writer(f, inventory.keys(), delimiter=',')
        items = []
        for k in inventory.keys():
            count = inventory[k]
            for i in range(0, count):
                items.append(k)
        w.writerow(items)
