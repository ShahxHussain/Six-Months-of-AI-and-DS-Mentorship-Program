# You can pass data, known as parameters, into a function.
# Functions can return data as a result.
# In Python, a function is defined using the def keyword.
# lets define a fuinction
def greet_user() :
    print ("Hello, User!")
greet_user()


# def aoa() :
#     print("Asalam O Alaekum, All the way from London" )
# aoa()


def aoa (name):
    print(f"Asalam O Alaekum, {name}!, Kaifa Haluk?")
# aoa ("Aammar")

def aoa (name = "Meray Payaray Bhai"):
    print(f"Asalam O Alaekum, {name}!, Kaifa Haluk?")
aoa ("Azam" )


def square(number):
    return number * number
print(square(9))


#RECURSION

def factorial (n):

    if n == 1:
        return 1
    else:
        return n * factorial (n-1)
    
print("Factorial: ", factorial(6))



#LAMBDA FUNCTION

x = lambda a: a / 10
print(x(10))


x = lambda a, b : a * b
print(x(2,9))


