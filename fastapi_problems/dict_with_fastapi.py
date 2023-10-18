'''
@Author: Vinit 
@Date: 2023-10-16 14:55:00
@Last Modified by: None
@Last Modified time: None
@Title : Write a Python script to perform CURD operation using fastapi with Dictionary
'''

from fastapi import FastAPI

app = FastAPI()

#students dict
employees_dict = {}


#GET
@app.get("/get_employee/")
def get_employee():
    return {
        "employee_list": employees_dict
    }


#POST
@app.post("/post_employee/")
def post_employee(employee_id,employee_name):
    employees_dict[employee_id] = employee_name
    return {
        "employee_list": employees_dict
    }


#PUT - Based on Key
#@app.put("/put_employee/")
#def put_employee(existing_employee_id,new_name):
#    if existing_employee_id in employees_dict.keys():
#        employees_dict[existing_employee_id] = new_name
#        
#    return {
#        "employee_dictionary": employees_dict
#    }


#PUT - Based on Value
@app.put("/put_employee/")
def put_employee(existing_employee_name,new_name):
    #search by values
    for key, value in employees_dict.items():
        if value == existing_employee_name:
            employees_dict[key] = new_name
            break
        
    return {
        "employee_dictionary": employees_dict
    }


#Delete
@app.delete("/delete_employee/")
def delete_employee(employee_id):
    employees_dict.pop(employee_id)
    return {
        "employee_list": employees_dict
    }