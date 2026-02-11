# Basic Try-Except

lst = [1, 2, 3, 4, 5]

try:
    i = int(input("Enter an index: "))
    print(lst[i])
except IndexError:
    print("Index out of range")  # handles invalid index
except ValueError:
    print("Invalid input")  # handles non-integer input
finally:
    print("Execution Completed")  # always executes


# Try-Except with Else

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Division by zero")  # handles division by 0
except ValueError:
    print("Invalid input")  # handles non-integer input
else:
    print(result)  # executes if no exception occurs
finally:
    print("Execution Completed")  # always executes


# Usage of Finally with Function

def func(idx):
    try:
        lst2 = [1, 2, 3, 4, 5]
        n = lst2[idx]
        return n  # return value if valid
    except IndexError:
        print("Index out of range")  # handle invalid index
    finally:
        print("Execution Completed")  # executes even if return happens


idx = int(input("Enter a number: "))
ans = func(idx)
print(ans)
