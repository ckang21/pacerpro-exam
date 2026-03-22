# PacerPro Engineer Test

## Overview
This project will keep track of the logs. If we have a response take too long in a certain period of time we will have a lambda function restart the EC2 and send a SNS alert.

## Part 1 - Sumo Logic
We take every log and examine it's response time. Over a 10 minute window we check and see if there were 5 or more logs that exceeded that 3 seconds. If we have that condition met we run the lambda part

## Part 2 - Lambda Function
If we have met the requirements from the Sumo Logic we will run the lambda function. It will restart EC2, log it and notify SNS

## Part 3 - Terraform
List of resources for aws systems and the IAM permissions to make lambda work. Resources are SNS topic, Lambda, IAM role

## Assumptions
Log format is all assumptions. I don't see any logs at all right now. No ID's either using placeholders for now
Not deployed anywhere but code and workflow is correct.
os.environ is commented out. We have a hardcode version for now.

## Recordings
https://drive.google.com/file/d/1lSUkLq5TsRR5-LYtFrrJh1bOwNTOhw-k/view?usp=sharing