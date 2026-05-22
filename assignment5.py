#1) Create a CSV file for address book, CSV file should have column for name, address, mobile, email. Insert 2-3 dummy data entered by user.

import csv

data = [
    ['name','address','mobile','email'],
        ["Aman Sharma", "Jaipur Rajasthan", "9876543210", "aman.sharma@gmail.com"],
    ["Priya Verma", "Kota Rajasthan", "9123456789", "priya.verma@gmail.com"],
    ["Rahul Meena", "Delhi India", "9988776655", "rahul.meena@gmail.com"]
]

with open ('addressBoook.csv','w',newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
print("CSV file created successfully")


#2)  Practice DATABASE  
# 1) Create Database
# 2) Create 2-3 tables
# 3) Insert some records
# 4) Perform diffrent select operations
# 5) Update some data
# 6) Delete some data


import sqlite3

# 1) Create database / connect to database
conn = sqlite3.connect("assignment5_database.db")
cur = conn.cursor()

print("\nDatabase created/connected successfully.")


# 2) Create 2-3 tables

cur.execute("""
CREATE TABLE IF NOT EXISTS test(
    id INTEGER PRIMARY KEY,
    name TEXT,
    subject_no TEXT,
    year INTEGER
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS emp(
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS student(
    s_id INTEGER PRIMARY KEY,
    name TEXT,
    semester TEXT,
    branch TEXT
)
""")

print("Tables created successfully.")


# 3) Insert some records

cur.executemany("""
INSERT OR IGNORE INTO test(id, name, subject_no, year)
VALUES (?, ?, ?, ?)
""", [
    (1, "John", "CS101", 2022),
    (2, "Aman", "CS102", 2023),
    (3, "Ravi", "CS103", 2024)
])

cur.executemany("""
INSERT OR IGNORE INTO emp(emp_id, name, salary)
VALUES (?, ?, ?)
""", [
    (101, "Luffy", 150000),
    (102, "Zoro", 33300),
    (103, "Sanji", 14000)
])

cur.executemany("""
INSERT OR IGNORE INTO student(s_id, name, semester, branch)
VALUES (?, ?, ?, ?)
""", [
    (1, "Alice", "5th", "CSE"),
    (2, "Bob", "3rd", "ECE"),
    (3, "Charlie", "7th", "ME")
])

conn.commit()

print("Records inserted successfully.")


# 4) Perform different SELECT operations

print("\nAll records from test table:")
cur.execute("SELECT * FROM test")
for row in cur.fetchall():
    print(row)

print("\nAll records from emp table:")
cur.execute("SELECT * FROM emp")
for row in cur.fetchall():
    print(row)

print("\nAll records from student table:")
cur.execute("SELECT * FROM student")
for row in cur.fetchall():
    print(row)

print("\nEmployees having salary greater than 30000:")
cur.execute("SELECT * FROM emp WHERE salary > 30000")
for row in cur.fetchall():
    print(row)

print("\nStudents from CSE branch:")
cur.execute("SELECT * FROM student WHERE branch = 'CSE'")
for row in cur.fetchall():
    print(row)


# 5) Update some data

cur.execute("""
UPDATE emp
SET salary = 50000
WHERE emp_id = 103
""")

conn.commit()

print("\nAfter updating salary of emp_id 103:")
cur.execute("SELECT * FROM emp")
for row in cur.fetchall():
    print(row)


# 6) Delete some data

cur.execute("""
DELETE FROM student
WHERE s_id = 2
""")

conn.commit()

print("\nAfter deleting student with s_id 2:")
cur.execute("SELECT * FROM student")
for row in cur.fetchall():
    print(row)


# Close connection
conn.close()

print("\nAll database operations completed successfully.")