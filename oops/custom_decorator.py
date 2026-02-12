def greet(func):
    def wrapper(*args, **kwargs):
        print("Hello, Good morning")
        result = func(*args, **kwargs)
        print(result)
        print("This function has executed successfully")
    return wrapper

@greet
def calculate_sum(a,b):
    return a+b

calculate_sum(1,2)