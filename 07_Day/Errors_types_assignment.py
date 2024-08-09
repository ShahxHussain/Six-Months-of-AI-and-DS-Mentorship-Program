# Trying to use a variable that hasn't been defined
try:
    print(non_existent_variable)
except NameError as e:
    print(e)  # Output: name 'non_existent_variable' is not defined


# Trying to add a string to an integer
try:
    result = 5 + "10"
except TypeError as e:
    print(e)  # Output: unsupported operand type(s) for +: 'int' and 'str'


# Trying to convert an invalid string to an integer
try:
    number = int("not_a_number")
except ValueError as e:
    print(e)  # Output: invalid literal for int() with base 10: 'not_a_number'


# Accessing an out-of-range index in a list
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print(e)  # Output: list index out of range


# Accessing a non-existent key in a dictionary
try:
    my_dict = {'a': 1, 'b': 2}
    print(my_dict['c'])
except KeyError as e:
    print(e)  # Output: 'c'


# Accessing a non-existent attribute of an object
try:
    class MyClass:
        pass
    obj = MyClass()
    print(obj.non_existent_attribute)
except AttributeError as e:
    print(e)  # Output: 'MyClass' object has no attribute 'non_existent_attribute'


# Division by zero
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(e)  # Output: division by zero


# Trying to open a non-existent file
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print(e)  # Output: [Errno 2] No such file or directory: 'non_existent_file.txt'


# Importing a non-existent module
try:
    import non_existent_module
except ImportError as e:
    print(e)  # Output: No module named 'non_existent_module'


# Creating an extremely large list (not practical to execute, just for illustration)
try:
    large_list = [1] * (10**10)
except MemoryError as e:
    print(e)  # Output: (depends on system, typically indicates memory error)


# Simulating a timeout error (typically raised by low-level system functions)
import socket

try:
    socket.setdefaulttimeout(0.01)
    s = socket.socket()
    s.connect(("www.example.com", 80))
except TimeoutError as e:
    print(e)  # Output: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond


