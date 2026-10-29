distance = float(input("Enter journey distance (km): "))
n = int(input("Enter number of passengers: "))

if distance <= 0 or n <= 0:
    print("Invalid distance or passenger count.")
else:
    # Distance-based fare per km
    if distance <= 100:
        base_rate = 1.0
    elif distance <= 500:
        base_rate = 1.5
    else:
        base_rate = 2.0

    class_rates = {
        "Sleeper": 1.0,
        "AC3": 2.0,
        "AC2": 3.0
    }

    reservation_fee = 40
    total_amount = 0

    for i in range(n):
        print(f"\nPassenger {i + 1}")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        travel_class = input(
            "Enter class (Sleeper/AC3/AC2): "
        ).strip()

        if age < 0 or travel_class not in class_rates:
            print("Invalid age or class. Passenger skipped.")
            continue

        base_fare = distance * base_rate * class_rates[travel_class
      
        if age < 5:
            concession = base_fare  # Free base fare
        elif age >= 60:
            concession = base_fare * 0.40
        else:
            concession = 0

        fare = base_fare - concession + reservation_fee

        cancelled = input("Cancel ticket? (yes/no): ").lower()

        print("\n--- Passenger Bill ---")
        print("Name:", name)
        print("Base fare: Rs", round(base_fare, 2))
        print("Concession: Rs", round(concession, 2))
        print("Reservation fee: Rs", reservation_fee)

        if cancelled == "yes":
            penalty = fare * 0.25
            refund = fare - penalty
            print("Cancellation penalty: Rs", round(penalty, 2))
            print("Refund amount: Rs", round(refund, 2))
            print("Status: Cancelled")
            total_amount += refund
        else:
            print("Final fare: Rs", round(fare, 2))
            print("Status: Confirmed")
            total_amount += fare

    print("\nTotal amount after cancellations: Rs",
          round(total_amount, 2))

