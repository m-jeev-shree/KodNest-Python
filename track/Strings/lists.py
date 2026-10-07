numbers = [1, 2, 3, 4, 5, 3]
print(numbers[1:5])
print(numbers[3:])
print(numbers[-4:-1])  # Output: [2, 4]
print(numbers,type(numbers))  # Output: [1, 2, 3, 4, 5] <class 'list'>

print(len(numbers))  # Output: 5
print(numbers[4])  # Output: 1

#using constructor 
stu = list(['Jeevitha',45.5,True,22])
print(stu,type(stu))  # Output: [1, 2, 3
stu.append('Python')
print(stu)  # Output: [1, 2, 3, 4
stu.insert(2,'Shreyas')
print(stu)  # Output: [1, 2, 'Shreyas', 3, 4
stu.extend(['Java','C++'])
print(stu)  # Output: [1, 2, 'Shreyas', 3, 4, 'Java', 'C++']

#pop the element at index 3
stu.pop(3) #pops the element at index value
print(stu)  # Output: [1, 2, 'Shreyas',

stu.remove('Java') #removes the element with value
print(stu)  # Output: [1, 2, 'Shreyas', 4, 'C++']

stu.clear() #removes all the elements from the list

del stu #deletes the list completely

#changing elements
num = [1,4,3,5,6,7,8,93]
num[5] = 6
num[1:4] = [20,30,40]
print(num)  # Output: [1, 20, 30, 40,


a = [10,20,4,65,34,78,44]
b = a.copy()  # creates a copy of the list

a.count(4)  # counts the number of occurrences of 4 in the list
print(a.count(4))  # Output: 1

a.index(65)  # returns the index of the first occurrence of 65 in the list
print(a.index(65))  # Output: 3

x = [7,34,21,565,67]
x.sort(reverse=True)  # sorts the list in descending order
print(x)  # Output: [7, 21, 34, 67, 565]