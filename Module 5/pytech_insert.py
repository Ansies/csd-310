from pymongo import MongoClient
import certifi

# Establish connection to MongoDB
client = MongoClient("mongodb+srv://admin:admin@cluster0.l5ipfnd.mongodb.net/", tlsCAFile=certifi.where())
db = client.pytech
students = db.students


# Create new student documents
new_students = [
    {"student_id": 1007, "first_name": "John", "last_name": "Doe"},
    {"student_id": 1008, "first_name": "Jane", "last_name": "Smith"},
    {"student_id": 1009, "first_name": "Michael", "last_name": "Johnson"}
]

# Insert new student documents and retrieve the inserted IDs
inserted_ids = []
for student in new_students:
    result = students.insert_one(student)
    inserted_ids.append(result.inserted_id)

# Display the returned student IDs
print("Inserted Student IDs:", inserted_ids)
