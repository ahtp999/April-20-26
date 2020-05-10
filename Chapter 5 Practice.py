print('inventory:')
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
for k, v in inventory.items():
    print(k+ ' ' +str(v))
itemtotal = sum(inventory.values())
print("Total number of items: " +str(itemtotal))
             
