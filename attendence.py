Algorithm
1. Start.
2. Input total classes held, classes attended, and eligibility percentage.
3. Validate the input values.
4. Calculate current attendance percentage.
5. If current attendance meets the threshold, display that the student is eligible.
6. Otherwise, initialize the required number of extra classes to zero.
7. Increase the extra classes by one until the attendance percentage reaches the threshold.
8. Display the minimum extra classes and the new attendance percentage.
9. Stop.
Flowchart
START

Input classes held, attended classes and eligibility threshold
Validate input and calculate current attendance
Attendance ≥ Threshold?

YES
Already eligible; extra classes = 0

NO
Increase extra classes until threshold is reached


Display required classes and new attendance
STOP

held = int(input("Enter total classes held: "))
attended = int(input("Enter classes attended: "))
threshold = float(input("Enter eligibility percentage: "))

if held <= 0 or attended < 0 or attended > held or threshold <= 0 or threshold > 100:
    print("Invalid input")

else:
    percentage = attended / held * 100

    print("Current Attendance =", round(percentage, 2), "%")

    if percentage >= threshold:
        print("You are already eligible")
        print("Extra classes required = 0")

    else:
        required = 0

        while (attended + required) / (held + required) * 100 < threshold:
            required += 1

        print("Minimum consecutive classes to attend =", required)
        print("Attendance after recovery =",
              round((attended + required) / (held + required) * 100, 2), "%")

Enter total classes held: 100
Enter classes attended: 60
Enter eligibility percentage: 75

Current Attendance = 60.0 %
Minimum consecutive classes to attend = 60
Attendance after recovery = 75.0 %        