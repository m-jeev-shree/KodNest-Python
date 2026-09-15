x = ["apple" , "banana", "cherry"]
y = ["apple" , "banana", "cherry"]
z = x
print(x is z) 
print(x is y) 
print(x == y) # False, because x and y are different objects

x = [1,2,3]
y = [1,2,3]
print(x is y) # False, because x and y are different objects
print(x == y) # True, because x and y have the same values

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # True, because "banana" is in the list

fruits = ["apple", "banana", "cherry"]
print("orange" not in fruits) # True, because "orange" is not in the list

text = "Hello, World!"
print("hello" in text) # True, because "Hello" is in the string
print("Python" not in text) # True, because "Python" is not in the string
print("H" in text) # True, because "H" is in the string

num = 5
result = "even" if num % 2 == 0 else "odd"
print(result) # Output: odd, because 5 is not divisible by 2

#wap to find the largest number among three numbers using ternary operator
a = 998
b = 206
c = 57
largest = a if (a > b and a > c) else (b if b > c and b > a else c)
print("The largest number is:", largest) # Output: The largest number is: 20

#wap to find if the number is positive, negative  using ternary operator
num =-505
result = "positive" if num > 0 else ("negative")
print("The number is:", result) # Output: The number is: negative
