"""def greet():
    print("Hello Priyanshu")

say_hello = greet           #Store a function in a variable
say_hello()"""

"""def say_name():
    print("Priyanshu")
def run_function(function):
    function()
run_function(say_name)  """        #Pass a function as an argument

"""
def greet():
    print("Hello Priyanshu")
def add_message(function):
    def wrapper():
        print("Starting...")
        function()
    return wrapper
new_greet = add_message(greet)
new_greet()
"""
#INSTEAD OF ABOVE CODE, WE CAN USE @ SYNTAX (ACTUAL USE OF DECORATOR)
#ALSO ADDED *ARGS
"""def add_message(function):
    def wrapper(*args, **kwargs):
        print("Starting...")
        function(*args, **kwargs)
    return wrapper
@add_message
def greet(name = "Aman"):
    print("Hello", name)

greet()
greet("Priyanshu")
"""


#CHALLENGE
def log_function(function):
    def wrapper(*args, **kwargs):
        print("Executing function")
        return function(*args, **kwargs)
    return wrapper

@log_function
def add(a, b):
    return a + b

result = add(10, 20)
print(result)