import csv
import json

# with open("myfiles/first.csv","r") as csv_file :
#     csv_reader = csv.reader(csv_file)

#     for row in csv_reader:
#         print(row)

# file = open("myfiles/first.csv" , "r+")

# file.write("a,b,c\n")
# file.write("1,2,3")

# str_val = file.read()

# file.close()

# print("")

# with open("myfiles/first.csv","w") as csv_file :
#     a= 5
#     b= 6
#     csv_writer = csv.writer(csv_file)

#     csv_writer.writerow([a, b, a+b])
#     csv_writer.writerow([a, b, a-b])
#     csv_writer.writerow([a, b, a*b])

#     # csv_writer.writerow(['5', '7', '12'])
#     # csv_writer.writerow(['8', '8', '16'])

with open("myfiles/student.json","r") as json_file :
    new_student = json.load(json_file)

print(new_student["courses"])

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
with open("myfiles/student.json","w") as json_file :
    json.dump(students[0],json_file)