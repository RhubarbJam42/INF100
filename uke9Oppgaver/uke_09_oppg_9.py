from copy import copy
#inv = {"gold coin": 42, "rope": 1}
#dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby", "dragon's pumpkin", "dragon's pumpkin"]


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
        print(value, key)
        item_total += inventory.get(key)
    return item_total


def addToInventory(inventory, added_items):
    updated_inventory = copy(inventory)
    for item in added_items:
        if item not in updated_inventory:
            updated_inventory.setdefault(item, 1)
        else:
            updated_inventory[item] += 1
    return updated_inventory


#test
#inv = addToInventory(inv, dragonLoot)
#total = displayInventory(inv)
#print("Total number of items:", total)
