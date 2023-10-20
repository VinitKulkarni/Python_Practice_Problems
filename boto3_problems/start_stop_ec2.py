'''
@Author: Vinit 
@Date: 2023-10-19 14:37:00
@Last Modified by: None
@Last Modified time: None
@Title : Check the status of ec2 and based on the status start or stop the ec2 using boto3
'''

#Import the Library
import boto3


#Management console
aws_console = boto3.session.Session(profile_name = "developer1")

#EC2 management console
ec2_console = aws_console.client("ec2")

#Check the status of ec2
my_ec2 = 'i-0f78599745ece20c2'
ec2_details = ec2_console.describe_instances()
for instance in ec2_details['Reservations']:
    for temp in instance['Instances']:
        if my_ec2 == temp['InstanceId']:
            ec2_current_state = temp['State']['Name']
            print(temp['InstanceId']," is ",temp['State']['Name'])
            if ec2_current_state == "stopped":
                #ec2 start
                response = ec2_console.start_instances(InstanceIds=[my_ec2])
                print(my_ec2, " is starting . . .")
            elif ec2_current_state == "running":
                #ec2 stop 
                response = ec2_console.stop_instances(InstanceIds=[my_ec2])
                print(my_ec2, " is stoping . . .")
            elif ec2_current_state == "pending":
                print(my_ec2, " is pending state please wait")
            else:
                print(my_ec2, " is in unknow state")