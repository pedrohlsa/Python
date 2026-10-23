products = {
    "Door": {"price": 100.72, "size": "100x72", "quantity": 30},
    "Keyboard": {"price": 67.11, "size": "60%", "quantity": 11}
}

products["Mouse"] = {"price": 59.90, "size": "small", "quantity": 15}

print(f"{products}\n ==========\n")

products["Door"]["quantity"] += 10

print(f"{products}\n ==========\n")

products["Keyboard"]["quantity"] -= 3

print(f"{products}\n ==========\n")

products["Mouse"]["price"] = 59.90

print(f"{products}\n ==========\n")

for name, info in products.items():
    print(f"{name}: preço R${info['price']}) | tamanho: {info['size']:.2f} | quantity: {info['quantity']} ")