
class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Marks:", self.marks)


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter ID: ")
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))

        s = Student(student_id, name, marks)
        self.students.append(s)

        print("Student added successfully!")

    def view_students(self):
        if len(self.students) == 0:
            print("No students found!")
            return

        for s in self.students:
            s.display()
            print("----------------")

    def search_student(self):
        student_id = input("Enter ID to search: ")

        for s in self.students:
            if s.student_id == student_id:
                s.display()
                return

        print("Student not found!")

    def delete_student(self):
        student_id = input("Enter ID to delete: ")

        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                print("Student deleted!")
                return

        print("Student not found!")

    def run(self):
        while True:
            print("\n1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.delete_student()
            elif choice == "5":
                print("Program closed!")
                break
            else:
                print("Invalid choice!")


app = StudentManagement()
app.run()
