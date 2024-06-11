# Defining functions using 'def'
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else 'Cannot divide by zero'

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def is_even(x):
    return x % 2 == 0

def is_odd(x):
    return x % 2 != 0

def max_value(x, y):
    return x if x > y else y

def min_value(x, y):
    return x if x < y else y

# Defining functions using lambda expressions
add_lambda = lambda x, y: x + y
subtract_lambda = lambda x, y: x - y
multiply_lambda = lambda x, y: x * y
divide_lambda = lambda x, y: x / y if y != 0 else 'Cannot divide by zero'
power_lambda = lambda x, y: x ** y
modulus_lambda = lambda x, y: x % y
is_even_lambda = lambda x: x % 2 == 0
is_odd_lambda = lambda x: x % 2 != 0
max_value_lambda = lambda x, y: x if x > y else y
min_value_lambda = lambda x, y: x if x < y else y

# Testing the functions
print(add(5, 3), add_lambda(5, 3))
print(subtract(5, 3), subtract_lambda(5, 3))
print(multiply(5, 3), multiply_lambda(5, 3))
print(divide(5, 3), divide_lambda(5, 3))
print(power(5, 3), power_lambda(5, 3))
print(modulus(5, 3), modulus_lambda(5, 3))
print(is_even(5), is_even_lambda(5))
print(is_odd(5), is_odd_lambda(5))
print(max_value(5, 3), max_value_lambda(5, 3))
print(min_value(5, 3), min_value_lambda(5, 3))
