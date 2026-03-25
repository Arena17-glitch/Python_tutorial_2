"""2) Problem: Employee Salary Management System

Create a program using inheritance to manage employee salaries.

🔹 Base Class: Employee
Attributes

emp_id

name

base_salary

Methods

display_employee()

Display employee details.

annual_salary()

Return yearly salary:

base_salary × 12
🔹 Derived Class: Manager

Additional attributes:

department

bonus

Methods

total_salary()

Calculate total annual salary:

(base_salary × 12) + bonus

display_manager()

Display all manager details including department and total salary.

🔹 Tasks

Create multiple manager objects.

Store them in a list (array) of objects.

Display all managers' details."""
class Employee:
    def __init__(self, emp_id: int, name: str, base_salary: float):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def display_employee(self) -> None:
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Base Salary: {self.base_salary}")

    def annual_salary(self) -> float:
        return self.base_salary * 12


class Manager(Employee):
    def __init__(self, emp_id: int, name: str, base_salary: float, department: str, bonus: float):
        super().__init__(emp_id, name, base_salary)
        self.department = department
        self.bonus = bonus

    def total_salary(self) -> float:
        return self.annual_salary() + self.bonus

    def display_manager(self) -> None:
        self.display_employee()
        print(f"Department: {self.department}")
        print(f"Total Salary: {self.total_salary()}")
        print()


# --- test code -----------------------------------------------------
if __name__ == "__main__":
    managers = [
        Manager(101, "Alice", 5000, "HR", 10000),
        Manager(102, "Bob", 6000, "IT", 15000),
        Manager(103, "Charlie", 5500, "Finance", 12000),
    ]

    for manager in managers:
        manager.display_manager()
