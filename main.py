DATA_FILE = "Record_project.txt"


def load_records():
    records = []
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                employee_data = line.strip().split(",")
                records.append(employee_data)
    except FileNotFoundError:
        print(f"{DATA_FILE} not found. A new file will be created.")
    return records


def save_records(records):
    try:
        with open(DATA_FILE, "w") as file:
            for record in records:
                file.write(",".join(record) + "\n")
    except Exception as error:
        print("Error saving records:", error)


def employee_exists(records, employee_id):
    for record in records:
        if record[0] == str(employee_id):
            return True
    return False


def add_employee(records):
    try:
        employee_id = input("Employee ID: ")
        if employee_exists(records, employee_id):
            print("Employee ID already exists.")
            return

        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        department = input("Department: ")
        position = input("Position: ")
        salary = input("Salary: ")

        new_record = [
            employee_id,
            first_name,
            last_name,
            department,
            position,
            salary,
        ]

        records.append(new_record)
        save_records(records)
        print("Employee added successfully.")
    except Exception as error:
        print("Error adding employee:", error)


def update_employee(records):
    try:
        employee_id = input("Enter Employee ID to update: ")
        for record in records:
            if record[0] == employee_id:
                record[1] = input("First Name: ")
                record[2] = input("Last Name: ")
                record[3] = input("Department: ")
                record[4] = input("Position: ")
                record[5] = input("Salary: ")
                save_records(records)
                print("Employee updated successfully.")
                return
        print("Employee not found.")
    except Exception as error:
        print("Error updating employee:", error)


def delete_employee(records):
    try:
        employee_id = input("Enter Employee ID to delete: ")
        for record in records:
            if record[0] == employee_id:
                records.remove(record)
                save_records(records)
                print("Employee deleted successfully.")
                return
        print("Employee not found.")
    except Exception as error:
        print("Error deleting employee:", error)


def search_employee(records):
    try:
        keyword = input("Enter name keyword: ")
        found = False
        for record in records:
            full_name = f"{record[1]} {record[2]}"
            if keyword.lower() in full_name.lower():
                print(",".join(record))
                found = True
        if not found:
            print("No matching employee found.")
    except Exception as error:
        print("Error searching employee:", error)


def list_employees(records):
    if not records:
        print("No employees found.")
        return
    for record in records:
        print(",".join(record))


def display_menu():
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Search Employee")
    print("5. List All Employees")
    print("6. Exit")


def main():
    records = load_records()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee(records)
        elif choice == "2":
            update_employee(records)
        elif choice == "3":
            delete_employee(records)
        elif choice == "4":
            search_employee(records)
        elif choice == "5":
            list_employees(records)
        elif choice == "6":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
