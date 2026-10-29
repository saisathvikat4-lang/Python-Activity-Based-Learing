venue = float(input("Enter venue cost (Rs): "))
equipment = float(input("Enter equipment cost (Rs): "))
catering_per_person = float(input("Enter catering cost per person (Rs): "))
transport_per_person = float(input("Enter transport cost per person (Rs): "))
certificate_per_person = float(input("Enter certificate cost per person (Rs): "))

participants = int(input("Enter expected participants: "))
sponsorship = float(input("Enter sponsorship amount (Rs): "))
registration_fee = float(input("Enter registration fee per person (Rs): "))

if (venue < 0 or equipment < 0 or catering_per_person < 0
        or transport_per_person < 0 or certificate_per_person < 0
        or participants < 0 or sponsorship < 0
        or registration_fee < 0):
    print("Invalid input. Values cannot be negative.")
else:
    fixed_cost = venue + equipment

    variable_cost_per_person = (
        catering_per_person
        + transport_per_person
        + certificate_per_person
    )

    total_cost = fixed_cost + variable_cost_per_person * participants
    total_sponsorship = sponsorship

    sponsorship_shortfall = max(0, total_cost - total_sponsorship)

    participant_contribution = registration_fee * participants
    total_funding = total_sponsorship + participant_contribution

    contribution_per_person = registration_fee - variable_cost_per_person

    if contribution_per_person > 0:
        required_registrations = max(
            0,
            int((fixed_cost - sponsorship + contribution_per_person - 1)
                // contribution_per_person)
        )
        import math
        required_registrations = max(
            0, math.ceil((fixed_cost - sponsorship) / contribution_per_person)
        )
    elif fixed_cost <= sponsorship:
        required_registrations = 0
    else:
        required_registrations = None

    print("\n--- Campus Event Financial Report ---")
    print("Fixed costs: Rs", round(fixed_cost, 2))
    print("Variable cost per participant: Rs",
          round(variable_cost_per_person, 2))
    print("Total event cost: Rs", round(total_cost, 2))
    print("Sponsorship: Rs", round(sponsorship, 2))
    print("Participant contribution: Rs",
          round(participant_contribution, 2))
    print("Sponsorship shortfall: Rs",
          round(sponsorship_shortfall, 2))
    print("Total funding: Rs", round(total_funding, 2))

    if required_registrations is not None:
        print("Minimum registrations to break even:",
              required_registrations)
    else:
        print("Break-even is not possible with the current fee and sponsorship.")

    if total_funding >= total_cost:
        print("Status: Event budget covered")
    else:
        print("Status: Additional funding required: Rs",
              round(total_cost - total_funding, 2))
