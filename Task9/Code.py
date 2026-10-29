budget = float(input("Enter travel budget in home currency (Rs): "))
n = int(input("Enter number of expense categories: "))

expenses = []

if budget < 0 or n <= 0:
    print("Invalid budget or number of categories.")
else:
    for i in range(n):
        print(f"\nExpense {i + 1}")
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        rate = float(input("Enter exchange rate (Rs per unit): "))
        fee_percent = float(input("Enter conversion fee (%): "))

        if amount < 0 or rate <= 0 or fee_percent < 0:
            print("Invalid values. Expense skipped.")
            continue

        converted = amount * rate
        fee = converted * fee_percent / 100
        total = converted + fee

        expenses.append({
            "category": category,
            "converted": converted,
            "fee": fee,
            "total": total
        })

    if expenses:
        total_spending = sum(e["total"] for e in expenses)
        largest = max(expenses, key=lambda e: e["total"])

        print("\n--- Travel Budget Report ---")
        for e in expenses:
            print("\nCategory:", e["category"])
            print("Converted amount: Rs", round(e["converted"], 2))
            print("Conversion fee: Rs", round(e["fee"], 2))
            print("Total expense: Rs", round(e["total"], 2))

        print("\nTotal spending: Rs", round(total_spending, 2))
        print("Travel budget: Rs", round(budget, 2))
        print("Largest expense category:", largest["category"])

        if total_spending <= budget:
            print("Status: Within budget")
            print("Remaining budget: Rs",
                  round(budget - total_spending, 2))
        else:
            print("Status: Budget exceeded")
            print("Amount exceeded: Rs",
                  round(total_spending - budget, 2))
    else:
        print("No valid expenses entered.")

