Algorithm
1. Start.
2. Read the travel budget, exchange rate, conversion fee percentage, and expenses.
3. Validate the inputs.
4. Convert each expense into INR using the exchange rate.
5. Add all converted expenses.
6. Calculate the conversion fee.
7. Calculate final spending by adding the fee to total expenses.
8. Identify the largest expense category.
9. Compare final spending with the budget.
10. Display the report and budget status.
11. Stop.
Flowchart
START

Input budget, exchange rate, fee and expenses
Validate inputs and convert expenses into INR
Calculate total expenses + conversion fee
Find the largest expense category
Spending ≤ Budget?

YES
Within budget

NO
Budget exceeded


STOP

budget = float(input("Enter travel budget in INR: "))
rate = float(input("Enter exchange rate (INR per foreign unit): "))
fee_rate = float(input("Enter conversion fee percentage: "))

hotel = float(input("Enter hotel expense in foreign currency: "))
food = float(input("Enter food expense in foreign currency: "))
transport = float(input("Enter transport expense in foreign currency: "))
shopping = float(input("Enter shopping expense in foreign currency: "))

values = [budget, rate, fee_rate, hotel, food, transport, shopping]

if any(value < 0 for value in values) or rate == 0:
    print("Invalid input")
else:
    expenses = {
        "Hotel": hotel * rate,
        "Food": food * rate,
        "Transport": transport * rate,
        "Shopping": shopping * rate
    }

    total = sum(expenses.values())
    fee = total * fee_rate / 100
    final_total = total + fee

    largest = max(expenses, key=expenses.get)

    print("\n--- Travel Budget Report ---")
    print("Expenses in INR:", expenses)
    print("Total Expenses =", round(total, 2))
    print("Conversion Fee =", round(fee, 2))
    print("Final Spending =", round(final_total, 2))
    print("Largest Expense =", largest)

    if final_total <= budget:
        print("Within Budget")
    else:
        print("Budget Exceeded")
        print("Extra Amount =", round(final_total - budget, 2))

Enter travel budget in INR: 50000
Enter exchange rate (INR per foreign unit): 90
Enter conversion fee percentage: 2
Enter hotel expense in foreign currency: 200
Enter food expense in foreign currency: 100
Enter transport expense in foreign currency: 50
Enter shopping expense in foreign currency: 100

--- Travel Budget Report ---
Expenses in INR: {'Hotel': 18000.0, 'Food': 9000.0, 'Transport': 4500.0, 'Shopping': 9000.0}
Total Expenses = 40500.0
Conversion Fee = 810.0
Final Spending = 41310.0
Largest Expense = Hotel
Within Budget        