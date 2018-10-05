## documentation - https://github.com/thisbejim/Pyrebase
import pyrebase

## add your own configuration for firebase.
config = {
    "apiKey" : "api-key",
    "authDomain": "domain",
    "databaseURL": "databaseurl",
    "storageBucket": "storageBucket",
}

connection = pyrebase.initialize_app(config)

## reading data from firebase
firebase = connection.database()

## reading data
database_reference = firebase.child("StudentManagement").get()
print("Firebase Data = ", database_reference.val())

## reading complex data
students_record = firebase.child("StudentManagement").child("Students").get()

for student in students_record.each():
    record = student.val()
    print("Student name is: ", record['name'])
    print("Student course is: ", record['course'])
    print("Student address is: ", record['address'])

## writing complex data
new_student_record = {
    'name' : 'Gurjas',
    'course' : 'Civil',
    'address' : 'Kapurthala, Punjab'
}

firebase.child("StudentManagement").child("Students").push(data=new_student_record)
print("New value inserted successfully.")
