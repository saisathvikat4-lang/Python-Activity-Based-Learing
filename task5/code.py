

quantity = int(input("Enter production quantity: "))
material_cost = float(input("Enter material cost per unit (Rs): "))
labour_cost = float(input("Enter labour cost per unit (Rs): "))
wastage_percent = float(input("Enter wastage percentage: "))
machine_cost = float(input("Enter total machine cost (Rs): "))
selling_price = float(input("Enter selling price per unit (Rs): "))
target_profit = float(input("Enter target profit percentage: "))

if (quantity <= 0 or material_cost < 0 or labour_cost < 0
        or machine_cost < 0 or selling_price < 0
        or not 0 <= wastage_percent <= 100
        or target_profit < 0):
    print("Invalid input. Enter valid non-negative values.")
else
    material_total = quantity * material_cost
    wastage_cost = material_total * wastage_percent / 100
    labour_total = quantity * labour_cost
    total_cost = material_total + wastage_cost + labour_total + machine_cost

  
    revenue = quantity * selling_price
    profit = revenue - total_cost

    if total_cost > 0:
        profit_percent = (profit / total_cost) * 100
    else:
        profit_percent = 0


    print("\n--- Manufacturing Report ---")
    print("Material Cost: Rs", round(material_total, 2))
    print("Wastage Cost: Rs", round(wastage_cost, 2))
    print("Labour Cost: Rs", round(labour_total, 2))
    print("Machine Cost: Rs", round(machine_cost, 2))
    print("Total Manufacturing Cost: Rs", round(total_cost, 2))
    print("Total Revenue: Rs", round(revenue, 2))
    print("Profit/Loss: Rs", round(profit, 2))
    print("Profit Percentage:", round(profit_percent, 2), "%")

    if profit_percent >= target_profit:
        print("Status: Target Achieved")
    else:
        print("Status: Target Not Achieved")

