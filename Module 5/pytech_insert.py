from pymongo import MongoClient
import certifi

# Connect to the MongoDB server
client = MongoClient("mongodb+srv://admin:admin@cluster0.l5ipfnd.mongodb.net/", tlsCAFile=certifi.where())

# Access the pytech database
db = client.pytech

# Access the students collection
students = db.students

# Insert three new student documents
student1 = {
    "student_id": 1007,
    "first_name": "John",
    "last_name": "Doe"
}

student2 = {
    "student_id": 1008,
    "first_name": "Jane",
    "last_name": "Smith"
}

student3 = {
    "student_id": 1009,
    "first_name": "Mark",
    "last_name": "Johnson"
}

# Insert the documents and get the inserted IDs
student_id1 = students.insert_one(student1).inserted_id
student_id2 = students.insert_one(student2).inserted_id
student_id3 = students.insert_one(student3).inserted_id

# Display the returned student IDs
print("Student IDs:")
print(student_id1)
print(student_id2)
print(student_id3)