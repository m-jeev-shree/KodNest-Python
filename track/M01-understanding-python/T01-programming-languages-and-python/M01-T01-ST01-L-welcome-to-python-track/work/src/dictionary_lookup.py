products = {"P101": ["Laptop", 1000], "P102": ["Smartphone", 500], 
            "P103": ["Tablet", 300], "P104": ["Headphones", 100], "P105": ["Smartwatch", 200]}
print(products["P104"]) #direct lookup
res = products.get("P106", "Product not found") #using get method also known as safe lookup
print(res)

products["P103"][0] = "Eraser" #adding new product
print(products)

#indexed dictionary 
employees = [{"employee_id": "E101","name":"Asha","age": 22},
             {"employee_id":"E102","name":"Shreyas","age": 17},
             {"employee_id":"E103","name":"Lara","age": 42}]
employee_by_id = {}
for employee in employees:
    employee_id = employee["employee_id"]
    employee_by_id[employee_id] = employee

print(employee_by_id)