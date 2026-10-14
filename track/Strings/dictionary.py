#dictionary are key value pairs, they are mutable and unordered collection of data.
#dictionary are defined using curly braces {} and key value pairs are separated by colon : 
# and each key value pair is separated by comma ,
#dictionary can have keys of different data types and values of different data types. 
# Keys must be unique and immutable, while values can be of any data type and can be duplicated.
#  Dictionaries are indexed by keys, which can be used to access the corresponding values.

student = {
    "name": "Jeevitha",
    "name" : "Tanuja", #duplicate key will be overwritten by the last value
    "age": 22,
    "grade": "A",
    "is_enrolled": True,
    "Technologies": ["Python", "Java", "C++"],  #list as value
    "course": "Python Programming",
    "course1": "Python Programming"  #string as value

}
print(student, type(student))  # Output: {'name': 'Tanuja', 'age': 22, 'grade': 'A', 'is_enrolled': True} <class 'dict'>

#update in dictionary
student.update({"age": 23, "grade": "A+"})
print(student)  # Output: {'name': 'Tanuja', 'age': 23, 'grade': 'A+', 'is_enrolled': True} 

student ["color"] = "green"

# fetching only keys from dictionary
print(student.keys())  # Output: dict_keys(['name', 'age', 'grade', 'is_enrolled'])
print(student.values())  # Output: dict_values(['Tanuja', 23, 'A+', True])
print(student.get("name"))  # Output: Tanuja
print(student.items())  # Output: dict_items([('name', 'Tanuja'), ('age', 23), ('grade', 'A+'), ('is_enrolled', True)])

print(student.pop("course1"))
print(student.popitem())  # last element is popped from the dictionary and returned as a tuple
student.clear()  # removes all elements from the dictionary
del student  # deletes the dictionary completely


employee = {
    "name": "Jeevitha",
    "age": 22,
    "department": "IT",
    "salary": 50000,
}

employee.setdefault("salary", 60000)  # if key is not present, it will add the key with the default value
print(employee)  # Output: {'name': 'Jeevitha', 'age': 22, 'department': 'IT', 'salary': 50000}
# if we have a value for the key in the dictionaey it will print the value
# if no value is present it will add the key with the default value and print the value

keys = ["name", "age", "department", "salary"]
y = 0
student = dict.fromkeys(keys, y)  # creates a new dictionary with keys from the list and values as 0
print(student)  # Output: {'name': 0, 'age': 0, 'department': 0, 'salary': 0}

my_dict = student.copy()  # creates a copy of the dictionary
print(my_dict)  # Output: {'name': 0, 'age': 0, 'department': 0, 'salary': 0}
my_dict.update({"department": "IT"})  # updates the dictionary with new key value pairs

for x in employee:
    print(x, employee[x])  # Output: name Jeevitha age 22 department IT salary 0

for x in employee.values():
    print(x)  # Output: Jeevitha 22 IT 50000

for x in employee.items():
    print(x)  # Output: ('name', 'Jeevitha') ('age', 22) ('department', 'IT') ('salary', 50000)

for x in employee.keys():
    print(x)  # Output: name age department salary

#nested dictionary
my_family = {
    "child1": {
        "name": "Sara",
        "age": 5
    },
    "child2": {
        "name": "Rohit",
        "age": 8
    },
    "child3": {
        "name": "Jeevitha",
        "age": 10
    }
}
print(my_family,type(my_family))  # Output: {'child1': {'name': 'Sara', 'age': 5}, 'child2': {'name': 'Rohit', 'age': 8}, 'child3': {'name': 'Jeevitha', 'age': 10}} <class 'dict'>
print(my_family["child3"]["name"], my_family["child3"]["age"])

for x in my_family:
    print(x)
    for y in my_family[x]:
        print(y,my_family[x][y]) #x represent the key and y represents the values present in the nested dictionary