# Create a Student class with name, age, percentage and a greeting method.
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


# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class StudentInfo:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average_marks(self):
        add = sum(self.marks)
        avg = add/len(self.marks)
        return avg

stu1 = StudentInfo("Bhavika", [80,90,95])
print(stu1.name)
print(stu1.marks)
print(stu1.average_marks())

# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.
class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit_money(self, amount):
        self.balance = self.balance - amount
        print(f"₹{amount} Debited from account no. {self.account_no} ")

    def credit_money(self, amount):
        self.balance = self.balance + amount
        print(f"₹{amount} Credited to account no. {self.account_no} ")

    def get_balance(self):
        print(f"Balance in your Account: ₹{self.balance}")

Account1 = Account(1000, 855)
Account1.get_balance()
Account1.debit_money(100)
Account1.credit_money(200)
Account1.get_balance()