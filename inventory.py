inventory=["sword","shield","armor","potion"]
choice=input("Do you want to add an item to your inventory? (yes/no). ")
if choice.lower()=="yes":
    new_item=input("Enter the name of the item you want to add: ")
    inventory.append(new_item)
print("Your inventory contains:")
for item in inventory:
    print("- " + item)
