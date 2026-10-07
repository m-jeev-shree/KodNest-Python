s = "Kodnest Technologies 123"
print("Original String:", s)

#case conversion method 
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Title Case:", s.title())
print("Swap Case:", s.swapcase())
print("Capitalize:", s.capitalize())

#searching and counting methods
print("Count of 'o':", s.count('o'))
print("find 'Technologies':", s.find('Technologies'))

#replacement method
s1 = s.replace("123", "456")
print("After Replacement:", s1)

#start and end check 
print("Starts with 'Kodnest':", s.startswith("Kodnest"))
print("Ends with '123':", s.endswith("123"))

# split and join methods
s2 = s.split()
print("Split String:", s2)
s3 = "-".join(s2)
print("Joined String:", s3)

#strip method
s4 = "   Kodnest Technologies   "
print("Original String with spaces:", s4)
print("After strip:", s4.strip())
s5 = "###Kodnest Technologies###"
print("Original String with special characters:", s5)
print("After strip special characters:", s5.strip("#"))
s6 = s4.lstrip()
print("After lstrip:", s6)
s7 = s4.rstrip()
print("After rstrip:", s7)

#checking methods 
isalpha = "Hello"
print("Is alpha:", isalpha.isalpha())
isdigit = "12345"
print("Is digit:", isdigit.isdigit())
isspace = "   "
print("Is space:", isspace.isspace())
isalnum = "Hello123"
print("Is alphanumeric:", isalnum.isalnum())
print("Hello123, isalnum.isalnum():", isalnum.isalnum())

#length of string
print("Length of string:", len(s))

s1 = "Hello"
s2 = "World"
print(id(s1), id(s2))
print(id(s2), id(s1))