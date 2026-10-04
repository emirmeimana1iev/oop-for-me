class Person:
    def __init__(self, name, full_name, is_married):
        self.name = name
        self.full_name = full_name
        self.is_married = is_married

    def introduce_myself(self):
        if self.is_married:
            marry = "i am married"
        else:
            marry = "i am not not married"
        return "My name is {}, and my full name is {}, and {}".format(self.name, self.full_name, marry)

class Student(Person):
    def __init__(self, name, full_name, is_married, marks):
        super().__init__(name, full_name, is_married)
        self.marks = marks
    def average_marks(self):
        print(round(sum(self.marks.values()) / len(self.marks), 2))

class Teacher(Person):
    def __init__(self, name, full_name, is_married, experience):
        super().__init__(name, full_name, is_married)
        self.experience = experience

    base_salary = 30000

    def get_salary(self):
        salary = Teacher.base_salary
        if self.experience < 3:
            print(salary)
        else:
            for _ in range(self.experience - 3):
                salary *= 1.05
            print(round(salary, 2))

teacher = Teacher("Beren", "Mom", True, 10)
print(teacher.introduce_myself(), "and my salary is: ", end="")
teacher.get_salary()

def create_student(student1, student2, student3):
    return [student1, student2, student3]

student_1 = Student("John", "Smith", True, {"Math":5, "English": 5, "kyrgyz":4})
student_2 = Student("Emir", "Mei", False, {"geometric":5, "russian":3})
student_3 = Student("Ali", "Jyl", False, {"Math":4, "biology":3, "chemistry":5, "physics":5})

for info in create_student(student_1, student_2, student_3):
    print(info.introduce_myself(), "and my average marks is: ", end="")
    info.average_marks()