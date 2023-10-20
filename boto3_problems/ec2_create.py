import os
from dotenv import load_dotenv
import boto3

load_dotenv()

ec2 = boto3.client('ec2',
                   os.getenv("availability-zone"),
                   aws_access_key_id = os.getenv("access-key-id"),
                   aws_secret_access_key = os.getenv("secret-access-key")
                   )
                   

#Function for running instances
connection = ec2.run_instances(InstanceType="t2.micro",
                         MaxCount=1,
                         MinCount=1,
                         ImageId="ami-08e5424edfe926b43")
print(connection)

