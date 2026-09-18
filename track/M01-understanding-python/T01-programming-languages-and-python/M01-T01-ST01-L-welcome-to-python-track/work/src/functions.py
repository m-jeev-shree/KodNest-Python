
def add_numbers():
    a = 101
    b = 234
    c = a + b
    print("The sum of the numbers is:", c) # Output: The sum of the numbers is: 335
# call function using object 
obj = add_numbers()

# square of a number
def sqaureNumbers(a):
    return a*a
obj1 = sqaureNumbers(5)
print("The square of the number is:", obj1) # Output: The square of the number is: 25

def largestOf2no(a,b):
    if a > b:
        return a
    else:
        return b
obj2 = largestOf2no(10,20)
print("The largest number is:", obj2) # Output: The largest number is:

# functions for different types of arguments
# write a function to find the square of a number 

# no arguments and no return value
def square():
    a = 6
    print("The square of the number is:", a*a) # Output: The square of the number is: 1225

square() # calling the function

# no arguments and return value
def square1():
    a = 5
    return a*a
obj = square1()
print("The square of the number is:", obj) # Output: The square of the number is: 1225 

# arguments and no return value
def square2(a):
    print("The square of the number is:", a*a) # Output: The square of the number is: 1225

res = square2(95) # calling the function

# arguments and return value
def square3(a):
    return a*a
obj = square3(7)
print("The square of the number is:", obj) # Output: The square of the number is: 1225  

