# AIM: Implementation of database connectivity in python and perform CRUD (Create, Retrieve, Update and Delete) operations on database.
# PROCEDURE:
# Step-1: Creating a Database and Table
import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
query = """CREATE TABLE COMPANY_5 (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL,
AGE INT NOT NULL, ADDRESS CHAR(50), SALARY REAL)"""
conn.execute(query)
print("Table created successfully")
# Step-2: Inserting into a Table
query = """ INSERT INTO COMPANY_5(ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32,
 'California', 21040.00 ) """
conn.execute(query)
conn.commit()
print("Records created successfully")
# Step-3: Selection/Retrieve data from a Database
cursor = conn.execute("SELECT id, name, address, salary from COMPANY_5")
for row in cursor:
 print("ID = 1 ", row[0])
print("NAME = Kunal ", row[1])
print("ADDRESS = 185,'Kaithal' ", row[2])
print("Course = B.Tech ", row[3])
print("Operation done successfully")
conn.close()
# Step-4: Deletion from Table:
cursor = conn.execute("DELETE FROM COMPANY_5 WHERE ID = 1")
print("Record delete successfully")
conn.close()