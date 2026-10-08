#sets are unordered collection of unique elements. They are mutable, don't allow duplicate elements, and are not indexed.
# meaning you can add or remove elements from a set after its creation. 
# Sets are defined using curly braces {} or the set() constructor.

s = {1, 2, 3, 4, 5}
print(s, type(s))  # Output: {1, 2, 3, 4, 5} <class 'set'>

#adding elements to a set
s.add(6)
print(s)  # Output: {1, 2, 3, 4, 5, 6}

#updating a set with multiple elements
s.update([7, 8, 9]) #update w a list of elements or as a set 
print(s)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

#remove elements from a set
s.remove(9)  # removes 9 from the set
print(s)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

#discard method removes an element from a set if it is present.
# If the element is not present, it does nothing and does not raise an error.
s.discard(10)  # removes 10 from the set
print(s)  # Output: {1, 2, 3, 4, 5, 6, 7}

s.pop()  # removes and returns an arbitrary element from the set
print(s)  # Output: {2, 3, 4, 5, 6, 7} #unordered collection, so the element removed is arbitrary

s.clear()  # removes all elements from the set
print(s)  # Output: set() #empty set

# del s  # deletes the set completely
# print(s)  # Output: NameError: name 's' is not defined

#how to get the index of a element in a set?
s1 = {}
print(s1, type(s1))  # Output: {} <class 'dict'> #empty set is treated as a dictionary
s2 = set({34,223,12,23})  
print(s2, type(s2))  # Output: {34, 223, 12, 23} <class 'set'> #non-empty set is treated as a set

 #to get the index of an element use loops
for n in s2:
     print(n)

#how to create an immutable set? cannot add modify or change elements in an immutable set it's an object.
s3 = frozenset({1, 2, 3, 4, 5})
print(s3, type(s3))  # Output: frozenset({1, 2, 3, 4, 5}) <class 'frozenset' 

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

#union of sets
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)  # Output: Union of set1 and set2: {1, 2, 3, 4, 5, 6, 7, 8}

intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)  # Output: Intersection of set1 and set2: {4, 5}

print(set1.isdisjoint(set2))
print(set1.issuperset(set2))
print(set1.issubset(set2))

print(set1.union(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

set1.add(12)
print(set1)  # Output: {1, 2, 3, 4, 5, 12}

set1.update([13, 14, 15])
print(set1)  # Output: {1, 2, 3, 4, 5, 12, 13, 14, 15}

set1.remove(12)
print(set1)  # Output: {1, 2, 3, 4, 5}

set1.discard(12)  # does not raise an error if the element is not present
print(set1)  # Output: {1, 2, 3, 4, 5}

set1.pop()  # removes and returns an arbitrary element from the set 
print(set1)  # Output: {2, 3, 4, 5} #unordered collection, so the element removed is arbitrary

set1.clear()  # removes all elements from the set
print(set1)  # Output: set() #empty set

#what is the difference between set and frozenset? 
# A set is mutable, meaning you can add or remove elements from it after its creation.
#  A frozenset is immutable, meaning you cannot add or remove elements from it after its creation.