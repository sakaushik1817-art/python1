1. Algorithm
1. Start.
2. Create two empty lists: months and bills.
3. Enter the number of months n.
4. Repeat the following steps for each month:
   - Enter electricity units consumed.
   - If units are less than or equal to 100, calculate the bill at ₹2 per unit.
   - If units are between 101 and 200, charge ₹2 for the first 100 units and ₹3 for the remaining units.
   - If units exceed 200, charge ₹2 for the first 100 units, ₹3 for the next 100 units, and ₹5 for the remaining units.
   - Add the fixed charge of ₹50.
   - Calculate and add a 5% surcharge.
   - If the bill is below ₹500, calculate and subtract a 5% rebate.
   - Store the month and final bill in the lists.
   - Display the electricity bill.
5. Display the monthly bills.
6. For each month after the first month:
   - Calculate the increase by subtracting the previous bill from the current bill.
   - If the increase is greater than 20% of the previous bill, display "Unusual increase detected!".
   - Otherwise, display whether the bill increased, decreased, or remained unchanged.
7. Stop.
2. Flowchart
START

Create empty lists months and bills; input n


YES ↓
Input electricity units

YES
Bill = units × 2

NO
Check units ≤ 200
Yes: first 100 at ₹2, remaining at ₹3
No: first 200 by slabs, remaining at ₹5


Add ₹50 fixed charge and 5% surcharge

YES
Subtract 5% rebate

NO
Keep bill unchanged


Store and display final bill; repeat for next month
Display monthly bills and compare consecutive months

YES
Print "Unusual increase detected!"

NO
Print increased, decreased, or unchanged


STOP
months = []
bills = []

n = int(input("Enter number of months: "))

for i in range(n):
    print("\nMonth", i + 1)

    units = int(input("Enter electricity units: "))

    # Progressive slab charges
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    # Fixed charge
    bill = bill + 50

    # Surcharge: 5% of bill
    surcharge = bill * 5 / 100
    bill = bill + surcharge

    # Rebate: 5% for bills below 500
    if bill < 500:
        rebate = bill * 5 / 100
        bill = bill - rebate

    months.append("Month " + str(i + 1))
    bills.append(bill)

    print("Electricity Bill =", round(bill, 2))

print("\nMonthly Bill Comparison")

for i in range(n):
    print(months[i], "=", round(bills[i], 2))

    if i > 0:
        increase = bills[i] - bills[i - 1]

        if increase > bills[i - 1] * 0.20:
            print("Unusual increase detected!")
        elif increase > 0:
            print("Bill increased")
        elif increase < 0:
            print("Bill decreased")
        else:
            print("Bill unchanged")

ouput:
Enter number of months: 3

Month 1
Enter electricity units: 80
Electricity Bill = 205.2

Month 2
Enter electricity units: 120
Electricity Bill = 429.45

Month 3
Enter electricity units: 250
Electricity Bill = 1071.0

Monthly Bill Comparison
Month 1 = 205.2
Month 2 = 429.45
Unusual increase detected!
Month 3 = 1071.0
Unusual increase detected!