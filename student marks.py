Algorithm
1. Start.
2. Store student names, subject names, and marks in a 2D list.
3. Display the marks matrix.
4. For each student, calculate total marks and average marks.
5. Store each student's average.
6. Find and display the student with the highest average.
7. For each subject, calculate the total marks across all students.
8. Calculate the average for each subject.
9. If a subject's average is below 60, display it as a low-average subject.
10. Stop.
4. Flowchart
START

Store student names, subject names and marks matrix
Calculate each student's total and average
Find and display the top performer
Calculate each subject's average
Subject average below 60?

YES
Display low-average subject

NO
Continue analysis


STOP

students = ["Rahul", "Priya", "Arun"]
subjects = ["Python", "Maths", "English"]

marks = [
    [80, 90, 70],
    [60, 50, 40],
    [90, 85, 95]
]

print("--- STUDENT MARKS MATRIX ---")

for row in marks:
    print(row)

print("\n--- ROW-WISE ANALYSIS ---")

averages = []

for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)
    averages.append(average)

    print("Student:", students[i])
    print("Total =", total)
    print("Average =", round(average, 2))

top_index = averages.index(max(averages))

print("\nTop Performer =", students[top_index])
print("Highest Average =", round(averages[top_index], 2))

print("\n--- COLUMN-WISE ANALYSIS ---")

for j in range(len(subjects)):
    column_total = 0

    for i in range(len(students)):
        column_total += marks[i][j]

    subject_average = column_total / len(students)

    print(subjects[j], "Average =", round(subject_average, 2))

    if subject_average < 60:
        print("Low average subject:", subjects[j])

--- STUDENT MARKS MATRIX ---
[80, 90, 70]
[60, 50, 40]
[90, 85, 95]

--- ROW-WISE ANALYSIS ---
Student: Rahul
Total = 240
Average = 80.0
Student: Priya
Total = 150
Average = 50.0
Student: Arun
Total = 270
Average = 90.0

Top Performer = Arun
Highest Average = 90.0

--- COLUMN-WISE ANALYSIS ---
Python Average = 76.67
Maths Average = 75.0
English Average = 68.33        