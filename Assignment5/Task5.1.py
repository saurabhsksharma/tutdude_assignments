students_marks = {"Alice": 85, "Emma": 92, "Sophia": 78, "Liam": 88, "Olivia": 95}

student = input("Enter the student's name: ")
if student in students_marks:
    print(f"{student}'s marks: {students_marks[student]}")
else:
    print("Student not found.")