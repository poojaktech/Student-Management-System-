```python
students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        students.append({"name": name, "roll_no": roll_no})
        print("Student added successfully!")

    elif choice == "2":
        print("\nStudent List:")

        for student in students:
            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
```
