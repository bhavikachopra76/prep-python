class Student:
    college_name = "Chitkara University"
    def __init__(self, name, age, percentage):
        self.name = name
        self.age = age
        self.percentage = percentage
    def greeting(self):
        print(f"Hi, {self.name}!")

def func(sd):
    print(f"Student name : {sd.name}, Age : {sd.age}, Percentage : {sd.percentage}, College_name : {sd.college_name}")
    sd.greeting()

s1 = Student("Bhavika", 21, 98.5)
func(s1)
