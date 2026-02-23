ITEM_DATABASE = {
    "sword": 3.0, "shield": 5.0, "potion": 0.5, "onion": 2.0, "gold": 0.1
}
MAX_WEIGHT = 10.0
inventory = []
current_weight = 0.0
print(f"--- RPG Inventory System ---")
print(f"Items: {', '.join(ITEM_DATABASE.keys())} | Limit: {MAX_WEIGHT} kg\n")
while True:
    print(f"\nInventory: {inventory} ({current_weight}/{MAX_WEIGHT} kg)")
    action = input("Action (add / remove / exit): ").lower().strip()
    if action == "exit":
        break
    elif action == "add":
        item = input("Find item: ").lower().strip()
        weight = ITEM_DATABASE.get(item)
        if weight is None:
            print("Unknown item!")
        elif current_weight + weight > MAX_WEIGHT:
            print(f"Too heavy! Need to drop {current_weight + weight - MAX_WEIGHT:.1f} kg")
        else:
            inventory.append(item)
            current_weight += weight
            print(f"Added {item} (+{weight} kg)")
    elif action == "remove":
        item = input("Drop item: ").lower().strip()
        if item in inventory:
            inventory.remove(item)
            current_weight -= ITEM_DATABASE[item]
            print(f"Dropped {item} (-{ITEM_DATABASE[item]} kg)")
        else:
            print("Item not found in backpack!")
    else:
        print("Invalid command!")