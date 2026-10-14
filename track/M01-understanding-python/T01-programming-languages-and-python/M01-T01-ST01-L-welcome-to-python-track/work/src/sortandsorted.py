cities = ['Nepal','Bengaluru','Pune','chennai']
u_cities = {city.lower() for city in cities}
print(u_cities)
print(type(u_cities))

num = [2,3,4,5]
uni_num = set()
for num1 in num:
    uni_num.add(num1 * num1)
print(uni_num)

uni_num = {num1 * num1 for num1 in num}
print(uni_num)
print(type(uni_num))

num2 = [12,12,4,3,5,78]
sq_list = [num * num for num in num2]
sq_set = [num*num for num in num2]

print(sq_list)
print(sq_set)

#dicitionary
numbers = [34,34,676,12]
cube = {}
for number in numbers:
    cube[number] = number ** 3
print(cube)

cube_by_num = {number: number ** 3 for number in numbers }
print(cube_by_num)
print(type(cube_by_num))

