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
    print(student)

# Insert a new document with student_id 1010
new_student = {
    "student_id": 1010,
    "first_name": "Emily",
    "last_name": "Johnson"
}
students.insert_one(new_student)

# Display the inserted document
print("-- DISPLAYING NEWLY INSERTED STUDENT --")
print(students.find_one({"student_id": 1010}))

# Delete the document with student_id 1010
students.delete_one({"student_id": 1010})

# Display all documents after deletion
print("-- DISPLAYING STUDENTS AFTER DELETION --")
for student in students.find():
    print(student)
