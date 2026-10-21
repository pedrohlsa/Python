wallet = {
    "owner": "Pedro",
    "balance": 100,
    "currency": "BRL"
}

print(wallet["owner"], wallet["balance"])

wallet["balance"] = 150

print(wallet["balance"])

wallet["balance"] -= 30

print(wallet["balance"])

wallet["active"] = True

print(wallet["active"])

products = {
    "Door": {"price": 100.72, "size": "100x72", "quantity": 30},
    "Keyboard": {"price": 67.11, "size": "60%", "quantity": 11}
}

for p, info in products.items():
    print(f"{p} | Price: {info['price']} | Size: {info['size']} | Qty: {info['quantity']}")

sale_report = [
    {"employee_id": 444, "product": "Door", "total": 254.35, "quantity": 4},
    {"employee_id": 444, "product": "Keyboard", "total": 7234.11, "quantity": 44},
    {"employee_id": 444, "product": "Door", "total": 67.11, "quantity": 1}
]

for s in sale_report:
    print(f"Employee ID: {s['employee_id']} | Product: {s['product']} | Total: {s['total']} | Qty: {s['quantity']}")
