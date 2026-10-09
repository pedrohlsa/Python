shopping_list = []

def showlist(items):
    for index, item in enumerate(items, start=1):
         print(f"{index}. {item}")

while True:
    print("\n--- SHOPPING LIST ---")
    print("1 - Add item")
    print("2 - Remove item")
    print("3 - Show list")
    print("4 - Exit")

    option = input("Choose: ")

    if option == "4":
        break

    elif option == "1": 
        add = input("What do you want to add ? ").strip()
        
        if add in shopping_list:
            print("This item is already in shopping list.")
        
        elif add == "":
            print("Empty items are not Allowed.")
        
        else:
            print(f"add on list: {add}")
            shopping_list.append(add)
    
    elif option == "2":
        rem = input("What do you want to remove ?").strip()
        
        if rem in shopping_list:
            shopping_list.remove(rem)
        else:
            print("Item not found on list")
            
    elif option == "3":
        if not shopping_list:
            print("Shopping list is empty.")
        else:
            showlist(shopping_list)
    else:
        print("Invalid option!")