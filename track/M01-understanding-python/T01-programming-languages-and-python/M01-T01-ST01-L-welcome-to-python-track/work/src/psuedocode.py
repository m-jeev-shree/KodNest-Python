#print hello world 
print("Hello World")

#check whether the number is even or odd
number = 10
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#check whether the number is positive, negative or zero
number = -5
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

#to find the largest of three numbers
num1 = 10
num2 = 20
num3 = 15
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number is", largest) 