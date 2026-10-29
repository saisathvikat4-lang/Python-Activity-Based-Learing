quantity = int(input("Enter production quantity: "))
material = float(input("Enter material cost per unit (Rs): "))
labour = float(input("Enter labour cost per unit (Rs): "))
wastage = float(input("Enter wastage percentage: "))
machine = float(input("Enter total machine cost (Rs): "))
selling_price = float(input("Enter selling price per unit (Rs): "))
target = float(input("Enter target profit percentage: "))

if (quantity <= 0 or material < 0 or labour < 0
        or machine < 0 or selling_price < 0
        or not 0 <= wastage <= 100 or target < 0):
    print("Invalid input.")
else:
    material_total = quantity * material
    wastage_cost = material_total * wastage / 100
    labour_total = quantity * labour

    total_cost = material_total + wastage_cost + labour_total + machine
    revenue = quantity * selling_price
    profit = revenue - total_cost

    if total_cost > 0:
        profit_percent = profit / total_cost * 100
    else:
        profit_percent = 0

    print("\n--- Manufacturing Report ---")
    print("Material Cost: Rs", round(material_total, 2))
    print("Wastage Cost: Rs", round(wastage_cost, 2))
    print("Labour Cost: Rs", round(labour_total, 2))
    print("Machine Cost: Rs", round(machine, 2))
    print("Total Manufacturing Cost: Rs", round(total_cost, 2))
    print("Total Revenue: Rs", round(revenue, 2))
    print("Profit/Loss: Rs", round(profit, 2))
    print("Profit Percentage:", round(profit_percent, 2), "%")

    if profit_percent >= target:
        print("Status: Target Achieved")
    else:
        print("Status: Target Not Achieved")

