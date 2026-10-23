def onlynums():
    print("Please, use only numbers!")
def minqty():
    print("Insert at least 1!")


def ask_int(message):
    while True:
        try:
            return int(input(message))
        
        except ValueError:
            onlynums()
            

def ask_float(message):
    while True:
        try:
            return float(input(message))
        
        except ValueError:
            onlynums()

        
products = {}

def add_product():
    print("==== Add page ====")

    
    op = ask_int("1. Add | 2. Exit")
    
    if op == 2:
        return

    elif op == 1:
        
        op2 = ask_int("How many product(s) do you want to add?")

        if op2 <= 0:
            minqty()
        else: 
            for i in range(op2):
                
                while True:
                    print(f"Insert your #{i + 1}")
                    name = input("Name: ")

                    if name in products:
                        print("Product already exists!")
                    else:
                        break
                    
                while True:
                
                    quantity = ask_int("Quantity: ")
                    
                    if quantity > 0:
                        break
                    
                    op3 = ask_int("Are you sure that you add a product with 0 stock?\n 1. Y | 2. N")

                    if op3 == 1:
                        break
                    
                
                while True:
                    
                    price = ask_float("Price: ")
                    if price > 0:
                        break
                    
                    op4 = ask_int("Are you sure the price will be 0? 1. Y | 2. N")

                    if op4 == 1:
                        break
    
                products[name] = {
                    "qty": quantity,
                    "price": price
                }

    else:
        print("Choose 1 or 2")
    

def show_product(products):
    for name, info in products.items():
        print(f"Name: {name} | R$ {info['price']:.2f} | {info['qty']} units")

salereport = {}

def sell_product():
    print("==== Sale page ====")

    sell = input(("Type name of what you selling: "))

    if sell in products:
        
       while True:
            sell_qty = ask_int("Quantity sell: ")

            if sell_qty <= 0:
                minqty()
            
            elif sell_qty > products[sell]['qty']:
                print("Not enough items in stock!")
                break

            else:
                products[sell]["qty"] -= sell_qty
                print("Sucessfuly")

                idsell = len(salereport) + 1
                sellname = sell
                sellqty = sell_qty
                sellprice = products[sell]["price"] * sell_qty

                salereport[idsell] = {
                    "name": sellname,
                    "qty": sellqty,
                    "price": sellprice 
                }
                
                break
    else:
        print("Product not exists!")           


def show_salereports(salereport):
    for name, info in salereport.items():
        print(f"ID: {name} | Name: {info['name']} | Quantity: {info['qty']:.2f} | Price: {info['price']}")

print("====== Stock Manager ======")

while True:
    op5 = ask_int("1. Add product\n2. Show products\n3. Sell product\n4. Show sales report\n5. Exit")

    if op5 == 5:
        break
    
    elif op5 == 1:
        add_product()
    
    elif op5 == 2:

        if products == {}:
            print("No products!")
        else:
            show_product(products)
    
    elif op5 == 3:
        sell_product()

    elif op5 == 4:
        if salereport == {}:
            print("No products!")
        else:
            show_salereports(salereport)