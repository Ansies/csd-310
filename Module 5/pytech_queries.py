from pymongo import MongoClient
import certifi

# Connect to the MongoDB server
client = MongoClient("mongodb+srv://admin:admin@cluster0.l5ipfnd.mongodb.net/", tlsCAFile=certifi.where())

# Access the pytech database
db = client.pytech

# Access the students collection
students = db.students

# Display all documents in the collection
print("-- DISPLAYING ALL STUDENTS --")
for student in students.find():
    print(f"Student ID: {student['student_id']}")
    print(f"First Name: {student['first_name']}")
    print(f"Last Name: {student['last_name']}\n")

# Display a single document by student_id
print("-- DISPLAYING STUDENT 1007 --")
student_1007 = students.find_one({"student_id": 1007})
print(f"Student ID: {student_1007['student_id']}")
print(f"First Name: {student_1007['first_name']}")
print(f"Last Name: {student_1007['last_name']}")