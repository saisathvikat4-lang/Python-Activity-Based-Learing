

data_needed = float(input("Enter required data (GB): "))
calls_needed = int(input("Enter required call minutes: "))
validity_needed = int(input("Enter required validity (days): "))
budget = float(input("Enter budget (Rs): "))

n = int(input("Enter number of mobile plans: "))
eligible_plans = []

for i in range(n):
    print(f"\nPlan {i + 1}")
    name = input("Plan name: ")
    price = float(input("Plan price (Rs): "))
    data_limit = float(input("Data limit (GB): "))
    call_limit = int(input("Call minutes limit: "))
    validity = int(input("Validity (days): "))
    extra_data_rate = float(input("Extra data charge per GB (Rs): "))
    extra_call_rate = float(input("Extra call charge per minute (Rs): "))

    
    extra_data = max(0, data_needed - data_limit)
    extra_calls = max(0, calls_needed - call_limit)

    extra_cost = (
        extra_data * extra_data_rate
        + extra_calls * extra_call_rate
    )
    total_cost = price + extra_cost

    print("Total cost: Rs", round(total_cost, 2))

    # Check usage, validity, and budget constraints
    if (data_limit >= data_needed
            and call_limit >= calls_needed
            and validity >= validity_needed
            and total_cost <= budget):
        eligible_plans.append((total_cost, name))


print("\n--- Result ---")

if eligible_plans:
    eligible_plans.sort()
    cost, name = eligible_plans[0]

    print("Most economical eligible plan:", name)
    print("Total cost: Rs", round(cost, 2))
else:
    print("No eligible plan found within the given constraints.")

