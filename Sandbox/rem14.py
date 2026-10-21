print("==== STOCK MANAGER ====")

productname = []
productqty = []
productprice = []

datesell = []
idfunc = []
quantitysell = []
totalproduct = []
productsell = []


def ShowProducts():
    for name, qty, price in zip(productname, productqty, productprice):
        print(f"{name} | Qty: {qty} | Price: {price:.2f}")


while True:
    try:
        op = int(
            input(
                "1. Add a Product | 2. Show/Search Products | 3. Sell Product | "
                "4. Sales Report | 5. Exit\n"
            )
        )

        if op == 5:
            break

        elif op == 1:
            qty = int(input("How many products do you want to add? "))

            for n in range(qty):
                print(f"Add your #{n + 1} product: ")

                productn = input("Enter the product name: ").lower()

                if productn == "" or productn in productname:
                    print("Name can't be empty or already in the list!")
                    continue

                productq = int(input("Qty: "))
                productp = float(input("Price: "))

                if productq < 0 or productp < 0:
                    print("Negative values aren't accepted.")
                    continue

                if productq == 0 or productp == 0:
                    print("Are you sure this product has 0 items or a price of 0?")
                    op2 = int(input("1. Continue | 2. Back: "))

                    if op2 == 2:
                        continue
                    elif op2 != 1:
                        print("Only 1 or 2 are accepted.")
                        continue

                productname.append(productn)
                productqty.append(productq)
                productprice.append(productp)

        # ---------------------#

        elif op == 2:
            print("Welcome to the Products page: ")

            try:
                op2 = int(input("1. Check an item | 2. Show all Products \nChoose: "))

                if op2 == 1:
                    consult = input("Enter the product name: ").lower()

                    if consult in productname:
                        for i in range(len(productname)):
                            if productname[i] == consult:
                                print(
                                    f"Name: {productname[i]} | "
                                    f"Qty: {productqty[i]} | "
                                    f"Price: {productprice[i]:.2f}"
                                )
                    else:
                        print("Product doesn't exist!")

                elif op2 == 2:
                    ShowProducts()

            except ValueError:
                print("Only numbers are accepted!")

        # ---------------------#

        elif op == 3:
            print("Welcome to the Sales page")

            try:
                op3 = int(input("1. Sell an item | 2. Show all Items \nChoose: "))

                if op3 == 1:
                    removeitem = input("Enter the item name: ").lower()

                    if removeitem in productname:
                        qtyremove = int(input("How many do you want to sell? "))

                        for i in range(len(productname)):
                            if removeitem == productname[i]:
                                if qtyremove > 0 and productqty[i] >= qtyremove:
                                    idf = int(input("Your ID: "))
                                    dts = input("Date: ")

                                    productqty[i] -= qtyremove
                                    ttp = qtyremove * productprice[i]

                                    idfunc.append(idf)
                                    datesell.append(dts)
                                    totalproduct.append(ttp)
                                    quantitysell.append(qtyremove)
                                    productsell.append(removeitem)

                                    print("Item sold! Added to the sales report.")
                                else:
                                    print("Invalid qty!")
                                break
                    else:
                        print("Product not found!")

                elif op3 == 2:
                    ShowProducts()

            except ValueError:
                print("Only numbers are accepted!")

        # ---------------------#

        elif op == 4:
            print("Sales report!")

            for i in range(len(productsell)):
                print(
                    f"Id: {idfunc[i]} | "
                    f"Date: {datesell[i]} | "
                    f"Product: {productsell[i]} | "
                    f"Qty: {quantitysell[i]} | "
                    f"Total: {totalproduct[i]:.2f}"
                )

        else:
            print("Invalid option.")

    except ValueError:
        print("Only numbers are accepted!")


# *** ===== STOCK MANAGER =====
# 1. Add product
# 2. Show products
# 3. Sell product
# 4. Show sales report
# 5. Exit

# Choose an option:
