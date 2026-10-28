1. Algorithm
1. Start.
2. Enter the patient's name and age.
3. Enter the consultation charge, diagnostic charge, and treatment charge.
4. Check whether the age and all charges are valid (non-negative).
5. If any input is invalid, display "Invalid input" and stop.
6. Calculate the total bill:
total = consultation + diagnostic + treatment
7. If the total bill is ₹5,000 or more, apply a 10% concession.
8. Calculate the final bill after the concession.
9. Classify the patient according to the payment policy:
- If the final bill is ₹10,000 or more, display "High Payment Category".
- Otherwise, display "Normal Payment Category".
10. Display the total bill, concession, final bill, and patient category.
11. Stop.
Note: These concession and classification thresholds are example rules for the practical program. You can change them if your question provides a different payment policy.
2. Flowchart
START

Input patient name, age, and charges

YES ↓
Calculate total bill

NO ↓
Print "Invalid input"



YES ↓
Apply 10% concession

NO ↓
Concession = ₹0


Calculate final bill = total − concession

YES ↓
High Payment Category

NO ↓
Normal Payment Category


Display total, concession, final bill, and category
STOP


name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

consultation = float(input("Enter consultation charge: "))
diagnostic = float(input("Enter diagnostic charge: "))
treatment = float(input("Enter treatment charge: "))

# Validate input
if age <= 0 or consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid input")

else:
    # Calculate total bill
    total = consultation + diagnostic + treatment

    # Apply concession
    if total >= 5000:
        concession = total * 10 / 100
    else:
        concession = 0

    # Calculate final bill
    final_bill = total - concession

    # Classify patient
    if final_bill >= 10000:
        category = "High Payment Category"
    else:
        category = "Normal Payment Category"

    # Display bill details
    print("\nPatient Name:", name)
    print("Total Bill =", total)
    print("Concession =", concession)
    print("Final Bill =", final_bill)
    print("Patient Category =", category)


Sample output
Example input:
Enter patient name: Rahul
Enter patient age: 20
Enter consultation charge: 1000
Enter diagnostic charge: 2000
Enter treatment charge: 3000


Output:
Patient Name: Rahul
Total Bill = 6000.0
Concession = 600.0
Final Bill = 5400.0
Patient Category = Normal Payment Category