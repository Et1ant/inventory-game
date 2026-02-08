# База данных предметов: Название -> Вес
ITEM_DATABASE = {
    "меч": 3.0,
    "щит": 5.0,
    "зелье": 0.5,
    "лук": 2.0,
    "золото": 0.1
}

inventory = []
max_weight = 10.0
current_weight = 0.0

print(f"--- Добро пожаловать в RPG Инвентарь! ---")
print(f"Доступные предметы: {', '.join(ITEM_DATABASE.keys())}")
print(f"Лимит веса: {max_weight} кг\n")

while True:
    print(f"\nВаш рюкзак: {inventory}")
    print(f"Занято: {current_weight}/{max_weight} кг")
    
    action = input("\nЧто сделать? (добавить / удалить / выход): ").lower().strip()

    if action == "выход":
        print("До встречи, герой!")
        break

    elif action == "добавить":
        item = input("Что вы нашли? ").lower().strip()
        
        if item in ITEM_DATABASE:
            weight = ITEM_DATABASE[item]
            if current_weight + weight <= max_weight:
                inventory.append(item)
                current_weight += weight
                print(f" {item} добавлен (+{weight} кг)")
            else:
                print(f" Слишком тяжело! Нужно выкинуть что-то весом хотя бы {current_weight + weight - max_weight} кг")
        else:
            print(" Я не знаю, что это за предмет. Попробуйте: меч, щит, зелье, лук или золото.")

    elif action == "удалить":
        item = input("Что выкидываем? ").lower().strip()
        
        if item in inventory:
            inventory.remove(item)
            current_weight -= ITEM_DATABASE[item]
            print(f" {item} выброшен. Стало легче на {ITEM_DATABASE[item]} кг")
        else:
            print(" У вас нет такого предмета!")

    else:
        print("Команда не распознана. Используйте: добавить, удалить или выход.")