#!/usr/bin/env python3

from main import app, db, Student
from datetime import date

def init_student_db():
    with app.app_context():
        # Create the student table
        db.create_all()
        print("Student database initialized successfully!")
        
        # Add sample student data
        sample_students = [
            Student(name='John Doe', age=20, dob=date(2004, 5, 15), address='123 Main St, City'),
            Student(name='Jane Smith', age=22, dob=date(2002, 8, 22), address='456 Oak Ave, Town'),
            Student(name='Bob Johnson', age=19, dob=date(2005, 1, 10), address='789 Pine Rd, Village')
        ]
        
        for student in sample_students:
            db.session.add(student)
        
        db.session.commit()
        print("Sample student data added successfully!")
        
        # Display all students
        students = Student.query.all()
        print("\nCurrent students in database:")
        for student in students:
            print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, DOB: {student.dob}, Address: {student.address}")

if __name__ == '__main__':
    init_student_db()
