#!/usr/bin/env python3

"""Classes
A class is blueprint for creating objects of the same type.
This is "OOP" Object Oriented Programming!
"""


class Person:
    # Constructor: the __init__ method is executed when a new object is created.
    def __init__(self, fname, lname):
        # Attributes: variables in the class
        self.firstname = fname
        self.lastname = lname

    # Methods: functions in the class
    def printname(self):
        print(self.firstname, self.lastname)


# Object instantiation
mydude = Person("Bro", "Dude")
myfriend = Person("Glenn", "Brown")
print(type(mydude))

my_int = 8
print(type(my_int))

# Accessing class attributes and methods through objects
mydude.printname()
myfriend.printname()


# Creating a Child Class that inherits from the parent class
class Student(Person):
    def __init__(self, fname, lname, grade):
        super().__init__(fname, lname)
        self.student_grade = grade

    def printgrade(self):
        print(f"{self.student_grade}%")

    def addpoints(self, points):
        self.student_grade += points


mystudent = Student("Mia", "Perry", 85)
mystudent.printname()
print(mystudent.student_grade)
mystudent.addpoints(10)
mystudent.printgrade()
