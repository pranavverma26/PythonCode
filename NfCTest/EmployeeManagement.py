
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Developer(Employee):
    def __init__(self, emp_id, name, salary, language):
        super().__init__(emp_id, name, salary)
        self.language = language

    def display(self):
        super().display()
        print("Language:", self.language)


class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def run(self):
        while True:
            print("\n1. Add Employee")
            print("2. Add Developer")
            print("3. View Employees")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.add_developer()
            elif choice == "3":
                self.view_employees()
            elif choice == "4":
                break
            else:
                print("Invalid choice!")

    def add_employee(self):
        emp_id = input("Enter employee ID: ")
        name = input("Enter name: ")
        salary = float(input("Enter salary: "))

        emp = Employee(emp_id, name, salary)
        self.employees.append(emp)

        print("Employee added!")

    def add_developer(self):
        emp_id = input("Enter developer ID: ")
        name = input("Enter name: ")
        salary = float(input("Enter salary: "))
        language = input("Enter programming language: ")

        dev = Developer(emp_id, name, salary, language)
        self.employees.append(dev)

        print("Developer added!")

    def view_employees(self):
        if len(self.employees) == 0:
            print("No employees found!")
            return

        for emp in self.employees:
            emp.display()
            print("----------------")




app = EmployeeManagement()
app.run()
