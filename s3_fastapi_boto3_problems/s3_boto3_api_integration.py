'''
@Author: Vinit 
@Date: 2023-10-16 12:30:00
@Last Modified by: None
@Last Modified time: None
@Title : With the help of fastapi, boto3, dotenv made the connection with s3 Bucket and perform CURD operation
'''

from fastapi import FastAPI
import os
from dotenv import load_dotenv
import boto3

app = FastAPI()

load_dotenv()

s3 = boto3.client('s3',
                   os.getenv("availability-zone"),
                   aws_access_key_id = os.getenv("access-key-id"),
                   aws_secret_access_key = os.getenv("secret-access-key")
                  )


bucket_name = "devopsymlfiles"  #bucket name you want to search
#local_file_path = 'C:/Users/user1/PYTHONWORK/aws_python/file.txt' #path to upload file
s3_object_name = 'file.txt' #file name inside s3 bucket(object name)
file_list = []



#GET
@app.get("/get_file/")
def get_file():
    response = s3.list_objects_v2(Bucket=bucket_name)
    file_list.clear()
    files = response.get("Contents")
    if files == None:
        print("no files found")
    else:
        for file in files:
            file_list.append(file['Key'])
    
    return {
        "List of Files": file_list
    }




#Delete
@app.delete("/delete_file/")
def delete_file(file_name):
    temp = file_name
    s3.delete_object(Bucket = bucket_name, Key = file_name)
    file_list.remove(file_name)
    return {
        "List of files": file_list
    }


#POST
#give file path like this => C:/Users/vinit/PYTHONWORK/aws_python/file.txt
#file_name means object name in s3_bucket => example.txt
@app.post("/post_file/")
def post_file(local_file_path,file_name,):
    s3.upload_file(local_file_path, bucket_name, file_name)
    file_list.append(file_name)
    return {
        "list of files": file_list
    }



#PUT
@app.put("/post_file/")
def put_file(file_name,content):
    local_file_path_to_download = 'C:/Users/vinit/PYTHONWORK/aws_python/temp/'+file_name
    s3.download_file(bucket_name, file_name, local_file_path_to_download)
    
    with open(local_file_path_to_download, 'a') as file:
        file.write(content+"\n")

    s3.upload_file(local_file_path_to_download, bucket_name, file_name)
    os.remove(local_file_path_to_download)
    return {
        "file present in this path": local_file_path_to_download
    }