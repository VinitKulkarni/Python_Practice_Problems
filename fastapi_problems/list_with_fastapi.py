'''
@Author: Vinit 
@Date: 2023-10-16 12:30:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python script to perform CURD operation using fastapi with List
'''

from fastapi import FastAPI

app = FastAPI()

#students list
students_list = []



#GET
@app.get("/get_student/")
def get_student():
    return {
        "student_list": students_list
    }


#PUT
@app.put("/put_student/")
def put_student(existing_student_name,new_name):
    if existing_student_name in students_list:
        index_value = students_list.index(existing_student_name)
        students_list[index_value] = new_name
    return {
        "student_list": students_list
    }



#POST
@app.post("/post_student/")
def post_student(student_name):
    students_list.append(student_name)
    return {
        "student_list": students_list
    }



#Delete
@app.delete("/delete_student/")
def delete_student(student_name):
    students_list.remove(student_name)
    return {
        "student_list": students_list
    }
