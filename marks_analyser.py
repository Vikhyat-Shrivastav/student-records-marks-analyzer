
subjects = ("Python", "Maths", "DBMS")


students = {}

student_ids = []

print("===== STUDENT RECORDS MANAGER =====")
print("Subjects:", subjects)


while True:
    try:
        n = int(input("How many students? "))
        if n > 0:
            break
        print("Enter at least 1 student.")
    except ValueError:
        print("Please enter a valid number.")


for i in range(n):

    print("\nEnter details of student", i + 1)

    while True:
        sid = input("Student ID: ").strip()

        if sid == "":
            print("ID cannot be empty.")
        elif sid in students:
            print("Student ID already exists!")
        else:
            break

    name = input("Student Name: ")


    marks = []

    for subject in subjects:
        while True:
            try:
                mark = float(input(subject + " marks: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Enter a valid number.")

    students[sid] = {
        "name": name,
        "marks": marks
    }

    student_ids.append(sid)



print("\n===== SEARCH STUDENT =====")

search_id = input("Enter student ID to search: ")

if search_id in students:
    print("Name:", students[search_id]["name"])
    print("Marks:", students[search_id]["marks"])
else:
    print("Student not found.")



print("\nFirst two student IDs:", student_ids[:2])

if student_ids:
    first_id = student_ids[0]
    print("First student's Python marks:",
          students[first_id]["marks"][0])



print("\n===== UPDATE MARKS =====")

update_id = input("Enter student ID to update: ")

if update_id in students:

    print("Subjects:")
    for i in range(len(subjects)):
        print(i, "-", subjects[i])

    try:
        position = int(input("Enter subject position (0-2): "))

        if 0 <= position < len(subjects):

            while True:
                new_mark = float(input("Enter new marks: "))

                if 0 <= new_mark <= 100:
                    
                    students[update_id]["marks"][position] = new_mark
                    print("Marks updated successfully!")
                    break
                else:
                    print("Marks must be between 0 and 100.")

        else:
            print("Invalid subject position.")

    except ValueError:
        print("Invalid input.")

else:
    print("Student not found.")


print("\n===== STUDENT REPORT =====")

averages = []

for sid, details in students.items():

    marks = details["marks"]

    total = sum(marks)
    average = total / len(subjects)

    averages.append(average)

    if average >= 75:
        result = "Distinction"
    elif average >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print("\nStudent ID:", sid)
    print("Name:", details["name"])

    for i in range(len(subjects)):
        print(subjects[i], ":", marks[i])

    print("Total:", total)
    print("Average:", round(average, 2))
    print("Result:", result)


print("\n===== SET ANALYSIS =====")

passed_by_student = {}

for sid, details in students.items():

    passed = set()

    for i in range(len(subjects)):
  
        if details["marks"][i] >= 40:
            passed.add(subjects[i])

    passed_by_student[sid] = passed

unique_passed = set()

for passed in passed_by_student.values():
    unique_passed = unique_passed.union(passed)

print("Subjects passed by at least one student:",
      sorted(unique_passed))


if len(student_ids) >= 2:

    print("\nAvailable IDs:", student_ids)

    id1 = input("Enter first student ID: ")
    id2 = input("Enter second student ID: ")

    if id1 in passed_by_student and id2 in passed_by_student:

        set1 = passed_by_student[id1]
        set2 = passed_by_student[id2]

        print("Union:", sorted(set1 | set2))
        print("Intersection:", sorted(set1 & set2))
        print("Difference:", sorted(set1 - set2))
        print("Symmetric Difference:", sorted(set1 ^ set2))

    else:
        print("Invalid student ID.")

else:
    print("Two students are required for set comparison.")


print("\n===== CLASS SUMMARY =====")

print("Total students:", len(students))

if averages:
    print("Class average:", round(sum(averages) / len(averages), 2))
    print("Highest average:", max(averages))
    print("Lowest average:", min(averages))

print("\n===== PROGRAM ENDED =====")