# fruits = ["apple" ,"banana", "cherry"] 

# print(fruits[0])

# fruits[1] = "grape"

# fruits.append("orange")

# fruits.remove("cherry")

# print(fruits)

# fruits.pop()

# print(fruits)

# point = (3,5,"t",2.55,5,7)
# # Point statik bir tuple'dır.

# x, y, z, t, a, b = point

# print("x:" ,point[-1])

# print("y:" ,y)

# print("b:" ,b)

# print("t:" ,t)

student ={
    "name" :"Alice",
    "age"  :22,
    "courses" : ["Math","History"]
 }

students = [{
    "name" :"Alice",
    "age"  :22,
    "courses" : ["Math","History"],
    "birth" : "01-05-1990"
 },{
    "name": "Jonah",
    "age": 33,
    "courses": ["History"]
},{
    "name": "Robert",
    "age": 24,
    "courses": ["Math"]
}]

print(students[1]["name"])
students[0]["age"] = 25
students[0]["courses"].append("Science")
students[0]["birth"] = "01-05-1990"

search_key = "01-05-1990"

find = list(students[0].keys())[list(students[0].values()).index(search_key)]

print(find)

numbers=[1,2,4,5]
squad_numbers = [x**3 for x in numbers]
print(squad_numbers)
even_squad_numbers = [x**3 for x in numbers if x**3%2==0]
print(even_squad_numbers)