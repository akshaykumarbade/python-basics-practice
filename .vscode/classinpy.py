'''
This program explains a class, constructor and method in a class
'''


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def getStudent(self):
        print("Student Name: "+self.name+" Age: " +
              str(self.age)+" Course Name: "+self.course)


student = Student("Nina", 25, "Python")
# student.getStudent()


class Nina(Student):
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def getInfo(self):
        print("Student Name:" + self.name)


nina = Nina("Nina", 24, "Data Science")
nina.getInfo()
nina.getStudent()  # inheritance
