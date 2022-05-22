# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f'You called {function.__name__}{args}')
        print(f'Output: {function(*args)}')
    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(n1, n2, n3):
    # pass
    return n1 + n2 + n3


a_function(2, 3, 4)

