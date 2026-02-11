#we can define our custom error
class NegativeNumberError(Exception):
    pass

def square_root(num):
    try:
        if num < 0:
            raise NegativeNumberError("Cannot take negative number")
    except NegativeNumberError as e:
        print(e)
    else:
        return num ** 0.5

print(square_root(-5))

#for example, we are storing salary of users
class SalaryError(Exception):
    pass

salary = int(input("Enter your salary: "))
try:
    if salary < 20000:
        raise SalaryError("Salary too low")
except SalaryError as e:
    print(e)
else:
    print(salary)
