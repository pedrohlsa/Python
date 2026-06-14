buy_list = []
buy_qty = int(input("How many items do you want to buy? "))

for i in range(buy_qty):  
    item = input(f"Item #{i+1}: ")
    buy_list.append(item)

print(f"\nYour list: {buy_list}")

op = input("\nWant to modify your list? (1 = Yes | 0 = No): ")

if op == "1":
    print(f"\nCurrent list: {buy_list}")
    
    op1 = input("Want to add or remove? (1 = Add | 0 = Remove): ")
    
    if op1 == "1":
        new_item = input("What do you want to add? ")
        buy_list.append(new_item)
        print(f"'{new_item}' added!")
    
    elif op1 == "0":
        item_to_remove = input("What item do you want to remove? ")
        if item_to_remove in buy_list:
            buy_list.remove(item_to_remove)
            print(f"'{item_to_remove}' removed!")
        else:
            print(f"'{item_to_remove}' not found in your list!")
    
    else:
        print("Invalid option!")

    print(f"\n✅ FINAL LIST: {buy_list}")

else:
    print("Program closed. Bye!")
