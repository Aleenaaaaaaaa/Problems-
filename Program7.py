class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}"


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, roll_no, name, marks):
        self.students.append(Student(roll_no, name, marks))
        print("Student added successfully!")

    def view_students(self):
        for student in self.students:
            print(student)

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                print("Student Found:", student)
                return
        print("Student not found!")


# Example
sm = StudentManagement()
sm.add_student(1, "John", 85)
sm.add_student(2, "Alice", 92)
sm.view_students()
sm.search_student(2)
