"""Functions to keep track and alter inventory."""


def create_inventory(items):
    inventory = {}
    for itm in items:
        inventory[itm] = items.count(itm)
    return inventory



def add_items(inventory, items):
    for itm in items:
        if itm in inventory:
            inventory[itm] = inventory[itm] + 1
        else:
            inventory[itm] =+ 1
    return inventory


def decrement_items(inventory, items):
    for itm in items:
        if inventory.get(itm) is None:
            continue
        inventory[itm] = max(0, inventory[itm] - 1)
    return inventory



def remove_item(inventory, item):
    if inventory.get(item) is not None:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    arr = []
    for key in inventory:
        if inventory[key] != 0:
            arr.append((key, inventory[key]))
    return arr




# to print out the return value.

Create_Inventory = create_inventory(["wood", "iron", "iron", "diamond", "diamond"])
Add_Items = add_items({"wood": 2, "gold": 1, "diamond": 3}, ["wood", "iron", "iron", "diamond", "diamond"])
Decrement_Items = decrement_items({"iron": 5, "gold": 2}, ["wood", "iron", "wood", "iron", "diamond"])
Remove_Item = remove_item({"iron": 5, "gold": 2}, "iron")
List_Inventory = list_inventory({"wood": 2, "gold": 1, "diamond": 3})


# Output
print('|Create an Inventory:', Create_Inventory, 
      '| Add Items to Inventory:', Add_Items, 
      '| Decrement Item number:', Decrement_Items, 
      '| Remove Item:', Remove_Item, 
      '| List out Inventory:', List_Inventory)