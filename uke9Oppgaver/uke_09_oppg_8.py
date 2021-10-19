# inventory.py
#stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
        print(value, key)
        item_total += inventory.get(key)
    return item_total

# check
#print(displayInventory(stuff))
