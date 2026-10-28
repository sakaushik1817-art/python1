Algorithm
1. Start.
2. Read employee name.
3. Read basic pay, allowances, overtime pay, and incentives.
4. Check whether any salary value is negative.
5. If any value is negative, display “Invalid salary details.”
6. Otherwise, calculate gross salary by adding all four salary components.
7. If gross salary is less than or equal to ₹10,000, set deduction to zero.
8. Else, if gross salary is less than or equal to ₹20,000, calculate 5% deduction on the amount above ₹10,000.
9. Otherwise, calculate 5% on ₹10,000 plus 10% on the amount above ₹20,000.
10. Calculate net salary by subtracting deduction from gross salary.
11. Display the formatted salary statement.
12. Stop.
4. Flowchart
START

Read employee name, basic pay, allowances, overtime and incentives
Any salary value negative?

YES
Display invalid salary details

NO
Calculate gross salary
Check gross salary

≤ ₹10,000: 0% deduction

₹10,001–₹20,000: 5% on excess over ₹10,000

> ₹20,000: 5% on ₹10,000 + 10% on excess over ₹20,000
Calculate net salary
Print salary statement


STOP

name = input("Enter employee name: ")

basic = float(input("Enter basic pay: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))

if basic < 0 or allowances < 0 or overtime < 0 or incentives < 0:
    print("Invalid salary details")

else:
    gross = basic + allowances + overtime + incentives

    if gross <= 10000:
        deduction = 0
    elif gross <= 20000:
        deduction = (gross - 10000) * 0.05
    else:
        deduction = 10000 * 0.05 + (gross - 20000) * 0.10

    net_salary = gross - deduction

    print("\n------ SALARY STATEMENT ------")
    print("Employee Name :", name)
    print("Basic Pay     : Rs.", basic)
    print("Allowances    : Rs.", allowances)
    print("Overtime Pay  : Rs.", overtime)
    print("Incentives    : Rs.", incentives)
    print("------------------------------")
    print("Gross Salary  : Rs.", gross)
    print("Deduction     : Rs.", deduction)
    print("Net Salary    : Rs.", net_salary)
    print("------------------------------")

Enter employee name: Rahul
Enter basic pay: 18000
Enter allowances: 3000
Enter overtime pay: 2000
Enter incentives: 1000

------ SALARY STATEMENT ------
Employee Name : Rahul
Basic Pay     : Rs. 18000.0
Allowances    : Rs. 3000.0
Overtime Pay  : Rs. 2000.0
Incentives    : Rs. 1000.0
------------------------------
Gross Salary  : Rs. 24000.0
Deduction     : Rs. 900.0
Net Salary    : Rs. 23100.0
------------------------------    