

name = input("Enter patient name: ")

consultation = float(input("Enter consultation charges: Rs "))
diagnostic = float(input("Enter diagnostic charges: Rs "))
treatment = float(input("Enter treatment charges: Rs "))

if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Error: Charges cannot be negative.")

else:
    total = consultation + diagnostic + treatment


    if total >= 10000:
        concession = total * 0.10
    else:
        concession = 0

    final_bill = total - concession
    if final_bill < 5000:
        category = "Low"
    elif final_bill < 15000:
        category = "Medium"
    else:
        category = "High"
    print("\n--- Hospital Bill ---")
    print("Patient Name:", name)
    print("Consultation Charges: Rs", consultation)
    print("Diagnostic Charges: Rs", diagnostic)
    print("Treatment Charges: Rs", treatment)
    print("Total Bill: Rs", round(total, 2))
    print("Concession: Rs", round(concession, 2))
    print("Final Bill: Rs", round(final_bill, 2))
    print("Patient Classification:", category)

