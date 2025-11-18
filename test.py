import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask

# connect to a database file (creates it if not existing)
engine = create_engine('sqlite:///my_database.db')
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, Sequence('student_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(2))

Base.metadata.create_all(engine)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')
conn.commit()
print("Table created successfully")
cursor.execute('''
INSERT INTO students (name, age, grade)
VALUES (?, ?, ?)
''', ('Aziza', 21, 'A'))
conn.commit()
print("Record inserted successfully")
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()
for row in rows:
    print(row)