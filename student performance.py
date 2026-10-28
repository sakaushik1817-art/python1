Algorithm
1. Start.
2. Create a list of subjects.
3. Input marks for each subject in three examinations.
4. Validate that all marks are between 0 and 100.
5. Calculate the final examination average.
6. For each subject, compare Exam 3 marks with Exam 1 marks.
7. If marks increased, display improvement; if they decreased, display decline; otherwise, display no change.
8. If the final marks are below 40, identify the subject as weak.
9. Classify overall performance:
   - 75 or above: Excellent
   - 60–74.99: Good
   - 40–59.99: Average
   - Below 40: Needs Improvement
10. Display the performance report.
11. Stop.
4. Flowchart
START

Input subject marks for three examinations
Marks between 0 and 100?

No → Display invalid marks
Calculate average and compare Exam 3 with Exam 1
Marks increased?

YES
Display improvement

NO
Display decline or no change


Identify subjects below 40 marks
Classify overall performance using average
Display performance report
STOP

subjects = ["Python", "Maths", "English"]

exam1 = []
exam2 = []
exam3 = []

for subject in subjects:
    print("\nEnter marks for", subject)
    exam1.append(float(input("Exam 1 marks: ")))
    exam2.append(float(input("Exam 2 marks: ")))
    exam3.append(float(input("Exam 3 marks: ")))

if any(mark < 0 or mark > 100
       for marks in [exam1, exam2, exam3]
       for mark in marks):
    print("Invalid marks")

else:
    print("\n--- PERFORMANCE TREND REPORT ---")

    total = sum(exam3)
    average = total / len(subjects)

    for i in range(len(subjects)):
        change = exam3[i] - exam1[i]

        print("\nSubject:", subjects[i])
        print("Exam 1:", exam1[i])
        print("Exam 2:", exam2[i])
        print("Exam 3:", exam3[i])

        if change > 0:
            print("Improvement:", change, "marks")
        elif change < 0:
            print("Decline:", abs(change), "marks")
        else:
            print("No change")

        if exam3[i] < 40:
            print("Weak subject")

    print("\nFinal Average =", round(average, 2))

    if average >= 75:
        print("Performance: Excellent")
    elif average >= 60:
        print("Performance: Good")
    elif average >= 40:
        print("Performance: Average")
    else:
        print("Performance: Needs Improvement")

Enter marks for Python
Exam 1 marks: 60
Exam 2 marks: 70
Exam 3 marks: 85

Enter marks for Maths
Exam 1 marks: 50
Exam 2 marks: 45
Exam 3 marks: 35

Enter marks for English
Exam 1 marks: 70
Exam 2 marks: 75
Exam 3 marks: 80

--- PERFORMANCE TREND REPORT ---

Subject: Python
Exam 1: 60.0
Exam 2: 70.0
Exam 3: 85.0
Improvement: 25.0 marks

Subject: Maths
Exam 1: 50.0
Exam 2: 45.0
Exam 3: 35.0
Decline: 15.0 marks
Weak subject

Subject: English
Exam 1: 70.0
Exam 2: 75.0
Exam 3: 80.0
Improvement: 10.0 marks

Final Average = 66.67
Performance: Good        