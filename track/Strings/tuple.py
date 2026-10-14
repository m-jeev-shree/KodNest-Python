#it allowes duplicates , ordered, immutable, heterogeneous data type,indexing and slicing is possible,
#  allows nesting, allows membership testing, allows iteration, allows concatenation and repetition

names = ("Jeevitha", "Sara", "Rohit","Sara")
print(names,type(names))  # Output: ('Jeevitha', 'Sara', 'Rohit', 'Sara') <class 'tuple'>
len(names)  # Output: 4
print(len(names))  # Output: 4
names.count("Sara")  # Output: 2
print(names.count("Sara"))  # Output: 2
names.index("Rohit")  # Output: 2
print(names.index("Rohit"))  # Output: 2
names[-1]  # Output: 'Sara'
print(names[-1])  # Output: 'Sara'
yn = names[0:3]  # Output: ('Jeevitha', 'Sara', 'Rohit')
print(yn,type(yn))  # Output: ('Jeevitha', 'Sara', 'Rohit')

# looping 
for i in names:
    print(i)  # Output: Jeevitha Sara Rohit Sara

fruits = ("apple")
print(fruits * 3)  # Output: apple <class 'str'>

#constructors 
students = tuple(["Jeevitha", "Sara", "Rohit","Sara"])
print(students,type(students))  # Output: ('Jeevitha', 'Sara', 'Rohit', 'Sara') <class 'tuple'>

n = (10)
numbers = 1,2,3,4,5
print(numbers,type(numbers)) #default it is treated as tuple

age = 20
age = 25
print(age)  # Output: 25 #reassigning the value of age variable to 25

# modification of tuple
age = [10, 20, 30]
age[1] = 25
print(age)  # Output: [10, 25, 30] #changing the value of the second element in the list to 25

#tuple packing and unpacking
fruits = tuple(["apple", "banana", "cherry"]) #tuples to variable
(f1, f2, f3) = fruits #unpacking the tuple into variables
print(f1)  # Output: apple
print(f2)  # Output: banana
print(f3)  # Output: cherry

#packing
a = 10
b = 20
c = 30
my_tuple = (a, b, c) #packing the variables into a tuple
print(my_tuple)  # Output: (10, 20, 30)

# extend , add , insert, remove, pop, clear, del are not allowed in tuple as it is immutable

a = (1, 2, 3)
b = (4, 5, 6)
c = a + b #concatenation of tuples
print(c)  # Output: (1, 2, 3, 4, 5, 6
