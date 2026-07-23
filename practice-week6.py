# grade_report.py

# List of student dictionaries
students = [
    {"name": "Amara", "maths": 85, "english": 78, "science": 92},
    {"name": "Sipho", "maths": 67, "english": 74, "science": 61},
    {"name": "Lerato", "maths": 45, "english": 52, "science": 48},
    {"name": "Thabo", "maths": 91, "english": 88, "science": 95},
    {"name": "Naledi", "maths": 38, "english": 44, "science": 35}
]

# List to store processed results
results = []

# Variables for class statistics
all_marks = []

# Process each student
for student in students:

    # Calculate average
    average = (
        student["maths"]
        + student["english"]
        + student["science"]
    ) / 3

    average = round(average, 2)

    # Grade logic
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # Status logic
    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    # Add result to results list
    results.append({
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    })

    # Add all marks for class statistics
    all_marks.append(student["maths"])
    all_marks.append(student["english"])
    all_marks.append(student["science"])


# Calculate class statistics
class_average = sum(
    result["average"] for result in results
) / len(results)

class_average = round(class_average, 2)

highest_mark = max(all_marks)
lowest_mark = min(all_marks)


# Display class report
print("\n" + "=" * 60)
print("                 CLASS GRADE REPORT")
print("=" * 60)

for result in results:
    print(
        f"Name: {result['name']:<10} "
        f"Average: {result['average']:>6.2f}% | "
        f"Grade: {result['grade']} | "
        f"Status: {result['status']}"
    )

print("-" * 60)
print(f"Class Average: {class_average:.2f}%")
print(f"Highest Mark:  {highest_mark}%")
print(f"Lowest Mark:   {lowest_mark}%")
print("=" * 60)


# Student search system
while True:

    search_name = input(
        "\nEnter a student name to search "
        "(or type 'exit' to quit): "
    )

    if search_name.strip().lower() == "exit":
        print("Search ended. Goodbye!")
        break

    found = False

    for result in results:

        if result["name"].lower() == search_name.strip().lower():

            print("\nStudent Found:")
            print(f"Name:    {result['name']}")
            print(f"Average: {result['average']:.2f}%")
            print(f"Grade:   {result['grade']}")
            print(f"Status:  {result['status']}")

            found = True
            break

    if not found:
        print("Student not found. Please try again.")