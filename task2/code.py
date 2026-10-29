

n = int(input("Enter number of months: "))
bills = []
previous = 0

for i in range(n):
    print("\nMonth", i + 1)
    units = int(input("Enter units consumed: "))

    if units < 0:
        print("Invalid units")
        break

    
    if units <= 100:
        charge = units * 2
    elif units <= 200:
        charge = 100 * 2 + (units - 100) * 3
    else:
        charge = 100 * 2 + 100 * 3 + (units - 200) * 5

    bill = charge + 50

    
    if units > 300:
        bill = bill * 1.05
    elif units <= 100:
        bill = bill * 0.90

    bills.append(bill)
    print("Bill: Rs.", round(bill, 2))

    if i > 0 and bill > previous * 1.30:
        print("Alert: Unusual bill increase!")

    previous = bill

print("\nMonthly Bill Summary")
for i, amount in enumerate(bills):
    print("Month", i + 1, ": Rs.", round(amount, 2))
