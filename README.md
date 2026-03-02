# Employee Management System

A simple console-based Employee Management System built in Python using file handling and procedural programming principles.

This system allows users to manage employee records stored in a text file.

---

## Features

* Add new employee
* Update employee details
* Delete employee
* Search employee by name
* List all employees
* Persistent file storage using `.txt` file
* Exception handling for stability

---

## Technologies Used

* Python
* File Handling
* Procedural Programming

---

## Project Structure

```
EmployeeManagementSystem/
│
├── main.py
└── Record_project.txt
```

---

## How It Works

Employee records are stored in `Record_project.txt` in comma-separated format:

```
EmployeeID,FirstName,LastName,Department,Position,Salary
```

The system reads from this file at startup and updates it after every modification.

---

## How to Run

Make sure Python is installed.

Run:

```
python main.py
```

Follow the menu instructions:

```
1. Add Employee
2. Update Employee
3. Delete Employee
4. Search Employee
5. List All Employees
6. Exit
```

---

## Example Record

```
101,Ahmad,Karasi,IT,Developer,8000
```

---

## Academic Context

Developed as part of a university computing science lab assignment to demonstrate:

* Function usage
* Conditional logic
* Loops
* Exception handling
* File-based data persistence

---
