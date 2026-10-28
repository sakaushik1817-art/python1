Algorithm
1. Start.
2. Read material cost, labour charges, wastage cost, machine cost, selling price, and target profit.
3. Check whether any input is negative. If yes, display invalid input.
4. Calculate total production cost.
5. Calculate profit by subtracting total cost from selling price.
6. Display total cost and profit or loss.
7. If profit is greater than or equal to target profit, display “Profit target achieved.”
8. Otherwise, display “Profit target not achieved.”
9. Stop.
Flowchart
START

Input production costs, selling price and target profit
Validate inputs
Total cost = Material + Labour + Wastage + Machine
Profit = Selling price − Total cost
Profit ≥ Target?

YES
Target achieved

NO
Target not achieved


STOP

material = float(input("Enter material cost: "))
labour = float(input("Enter labour charges: "))
wastage = float(input("Enter wastage cost: "))
machine = float(input("Enter machine cost: "))
selling = float(input("Enter selling price: "))
target = float(input("Enter target profit: "))

if material < 0 or labour < 0 or wastage < 0 or machine < 0 or selling < 0 or target < 0:
    print("Invalid input")
else:
    total_cost = material + labour + wastage + machine
    profit = selling - total_cost

    print("\n--- Manufacturing Report ---")
    print("Total Cost =", total_cost)
    print("Selling Price =", selling)
    print("Profit/Loss =", profit)

    if profit >= target:
        print("Profit target achieved")
    else:
        print("Profit target not achieved")

Enter material cost: 5000
Enter labour charges: 2000
Enter wastage cost: 500
Enter machine cost: 1000
Enter selling price: 11000
Enter target profit: 2000

--- Manufacturing Report ---
Total Cost = 8500.0
Selling Price = 11000.0
Profit/Loss = 2500.0
Profit target achieved        