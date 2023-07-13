from pymongo import MongoClient
import certifi

# Connect to the MongoDB server
client = MongoClient("mongodb+srv://admin:admin@cluster0.l5ipfnd.mongodb.net/", tlsCAFile=certifi.where())

# Access the pytech database
db = client.pytech

# Access the students collection
students = db.students

# Output all documents in the students collection
print("-- DISPLAYING STUDENTS DOCUMENTS --")
for student in students.find():
    print(student)

# Update the last name for student_id 1007
students.update_one({"student_id": 1007}, {"$set": {"last_name": "Doe"}})

# Find and output the updated document for student_id 1007
print("\n-- DISPLAYING STUDENT DOCUMENT 1007 --")
print(students.find_one({"student_id": 1007}))
