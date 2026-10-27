1. Algorithm
1. Start.
2. Read the number of electricity units from the user.
3. If units are less than or equal to 100, calculate bill = units × 2.
4. Else, if units are less than or equal to 200, calculate bill = 200 + (units − 100) × 3.
5. Otherwise, calculate bill = 500 + (units − 200) × 5.
6. Display the electricity bill.
7. Stop.
2. 
Flowchart
START

Input electricity units
Units ≤ 100?

YES
bill = units × 2


NO
Units ≤ 200?

YES
200 + (units − 100) × 3


NO
500 + (units − 200) × 5





Display electricity bill
STOP

units = int(input("Enter units: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 200 + (units - 100) * 3
else:
    bill = 500 + (units - 200) * 5

print("Electricity Bill =", bill)

3. Sample output
For an input of 150 units:
Enter units: 150
Electricity Bill = 350
