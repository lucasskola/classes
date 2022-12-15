
# 1
class Student:
    def __init__(self, name, release_date, cost):
        self.name = name
        self.release_date = release_date
        self.cost = cost


    def grade(self, grade):
        return self.grade
# 2 
class Course:
    def __init__(self, name, max_studets):
        self.name = name
        self.max_studets = max_studets
        self.students = []
    def add_student(self, student):
        if len(self.students) < self.max_studets:
            self.students.append(student)
            return True
        return False


    def grade(self, grade):
        return self.grade

# 3 
class School:
    def __init__(self, name, year_founded):
        self.name = name
        self.year_founded = year_founded
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def get_student_names(self):
        return [student.name for student in self.students]
    
    def get_number_of_students(self):
        return len(self.students)

# 4
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_school = School("My School", 1990)

student1 = Student("John", 15)
student2 = Student("Jane", 16)

my_school.add_student(student1)
my_school.add_student(student2)

print(my_school.get_student_names())  # ["John", "Jane"]
print(my_school.get_number_of_students())  # 2
