products = []

n = int(input("Enter number of products: "))

if n <= 0:
    print("Invalid number of products.")
else:
    for i in range(n):
        print(f"\nProduct {i + 1}")
        name = input("Product name: ")
        category = input(
            "Category (food/clothing/electronics): "
        ).lower()
        price = float(input("Price per unit (Rs): "))
        quantity = int(input("Quantity: "))

        if price < 0 or quantity <= 0:
            print("Invalid price or quantity. Product skipped.")
            continue

        tax_rates = {
            "food": 0.05,
            "clothing": 0.05,
            "electronics": 0.18
        }

        if category not in tax_rates:
            print("Invalid category. Product skipped.")
            continue

        subtotal = price * quantity
        tax = subtotal * tax_rates[category]

        products.append({
            "name": name,
            "category": category,
            "quantity": quantity,
            "subtotal": subtotal,
            "tax": tax
        })

    subtotal_total = sum(p["subtotal"] for p in products)
    tax_total = sum(p["tax"] for p in products)

    threshold = 5000
    discount_rate = 0.10
    max_discount = 1000

    if subtotal_total >= threshold:
        discount = min(
            subtotal_total * discount_rate,
            max_discount
        )
    else:
        discount = 0

    final_bill = subtotal_total + tax_total - discount

    print("\n========== RETAIL INVOICE ==========")
    print("Product       Qty   Subtotal   Tax")

    for p in products:
        print(
            f"{p['name']:<14}"
            f"{p['quantity']:<6}"
            f"Rs {p['subtotal']:<8.2f}"
            f"Rs {p['tax']:.2f}"
        )

    print("------------------------------------")
    print("Subtotal: Rs", round(subtotal_total, 2))
    print("Total Tax: Rs", round(tax_total, 2))
    print("Discount: Rs", round(discount, 2))
    print("Final Bill: Rs", round(final_bill, 2))
    print("====================================")
