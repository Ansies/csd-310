from pymongo import MongoClient
import certifi

# Create a connection to the MongoDB server
client = MongoClient("mongodb+srv://admin:admin@cluster0.l5ipfnd.mongodb.net/", tlsCAFile=certifi.where())

# Access the 'pytech' database
db = client.pytech

# Access the 'students' collection
students = db.students

# Use the find_one() method to display a single document by student_id
student = students.find_one({"student_id": "1007"})
print(student)
