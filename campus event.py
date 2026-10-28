Algorithm
1. Start.
2. Read venue, equipment, transport, catering, and certificate costs.
3. Read expected participants, sponsorship amount, and registration fee.
4. Validate the inputs.
5. Calculate fixed cost by adding venue, equipment, and transport costs.
6. Calculate total event cost using fixed and per-participant costs.
7. Calculate sponsorship shortfall.
8. Calculate the contribution needed per participant.
9. Calculate the minimum registrations needed to break even, considering the registration fee and variable cost per participant.
10. Display the event financial report.
11. Check whether expected registration income plus sponsorship covers the total event cost.
12. Stop.
Flowchart
START

Input event costs, participants, sponsorship and registration fee
Validate inputs
Calculate fixed cost and total event cost
Calculate sponsorship shortfall and participant contribution
Calculate minimum break-even registrations
Income + Sponsorship ≥ Cost?

YES
Financially feasible

NO
Additional funds required


STOP

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per participant: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost per participant: "))
participants = int(input("Enter expected participants: "))
sponsorship = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per participant: "))

if (venue < 0 or equipment < 0 or catering < 0 or
    transport < 0 or certificate < 0 or
    participants < 0 or sponsorship < 0 or fee < 0):
    print("Invalid input")

else:
    fixed_cost = venue + equipment + transport
    variable_cost = catering + certificate
    total_cost = fixed_cost + variable_cost * participants

    shortfall = max(0, total_cost - sponsorship)
    contribution = shortfall / participants if participants > 0 else 0

    if fee > variable_cost:
        minimum = max(0, int((fixed_cost - sponsorship) /
                             (fee - variable_cost)) + 1)
        if (fixed_cost - sponsorship) <= 0:
            minimum = 0
    else:
        minimum = 0 if sponsorship >= fixed_cost else -1

    print("\n--- Campus Event Report ---")
    print("Fixed Cost =", fixed_cost)
    print("Total Event Cost =", total_cost)
    print("Sponsorship =", sponsorship)
    print("Sponsorship Shortfall =", shortfall)
    print("Contribution Needed Per Participant =", round(contribution, 2))

    if minimum == -1:
        print("Break-even not possible at this registration fee")
    else:
        print("Minimum Registrations to Break Even =", minimum)

    if participants * fee + sponsorship >= total_cost:
        print("Event is financially feasible")
    else:
        print("Additional funds are required")

Enter venue cost: 10000
Enter equipment cost: 5000
Enter catering cost per participant: 200
Enter transport cost: 3000
Enter certificate cost per participant: 50
Enter expected participants: 100
Enter sponsorship amount: 8000
Enter registration fee per participant: 400

--- Campus Event Report ---
Fixed Cost = 18000.0
Total Event Cost = 43000.0
Sponsorship = 8000.0
Sponsorship Shortfall = 35000.0
Contribution Needed Per Participant = 350.0
Minimum Registrations to Break Even = 31
Event is financially feasible        