"""
Oscar Chiqui - ITEC 2905 CAPSTONE 

Write a main function to create some example Student objects with some example names, college_id and GPA values. 
"""

# Get dataclass to use the dataclasses - creating a class Student  

print(" The name, college ID and GPA for students \n")

import dataclasses
from dataclasses import dataclass

@dataclass

# Name of Properties and data types 

# Add one more field: gpa, a float.

class Student:

    name : str
    college_id : str
    gpa : float

# str method name, id , gpa 

    def __str__(self):
        return f'Name: {self.name}, id: {self.college_id}, gpa: {self.gpa}'

# a main function to create some example Student objects with some example
#  names, college_id and GPA values. 

def main():

    Oscar = Student('Oscar', 'aa1234aa', 4.0)
    Erick = Student('Erick','bb234bb', 2.5)
    Sara =  Student('Sara', 'cc345cc', 4.0)

#  Read the name, college ID and GPA

    print(Oscar.name)
    print(Erick.college_id)
    print(Sara.gpa)

    print(Oscar)
    print(Erick)
    print(Sara)

main()