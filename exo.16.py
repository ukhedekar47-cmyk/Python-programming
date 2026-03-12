#AIM: Write aPython script that prompts the user to enter their phonenumber and email ID. 
# It then employs Regular Expressions toverify if these inputs adhere to standard phone number andemail address formats
print("UIN: 251P102,NAME: Harsh Vernekar")


import re

email = input("Enter Email ID: ")
mobile = input("Enter Mobile Number: ")

email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
mobile_pattern = r'^[6-9]\d{9}$'

if re.fullmatch(email_pattern, email):
    print("Valid Email ID")
    
else:    
    print("Invalid Email ID")

if re.fullmatch(mobile_pattern, mobile):
    print("Valid Mobile Number")
    
else:   
    print("Invalid Mobile Number")
    
    