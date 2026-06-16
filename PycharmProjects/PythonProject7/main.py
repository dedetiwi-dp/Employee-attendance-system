import csv
import os

def add_employee():
    employee_id = input("Employee ID: ")
    name = input("Employee Name: ")

    file_exists = os.path.isfile("employees.csv")

    with open("employees.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["ID", "Name"])

        writer.writerow([employee_id, name])

    print("Employee added successfully!")

def view_employees():
    try:
        with open("employees.csv", "r") as file:
            reader = csv.reader(file)

            print("\n===== EMPLOYEE LIST =====")

            for row in reader:
                print(" | ".join(row))

    except FileNotFoundError:
        print("No employee data found.")

while True:
    print("\n===== EMPLOYEE ATTENDANCE SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Check In")
    print("4. Check Out")
    print("5. Exit")

    choice = input("Choose menu: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        print("Check In")

    elif choice == "4":
        print("Check Out")

    elif choice == "5":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")