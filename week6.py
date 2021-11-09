#Employee ID (this is required, and must be a number that is 7 or less digits long)
while True:
    employee_id = input("Enter Employee ID\n")
    if employee_id  == "":     #if employee id is empty
        print("Employee ID can't be Empty")
    elif len(employee_id ) > 7: #if employee id is greater than 7
        print("Employee ID must be less than 7")
    elif employee_id .isdigit(): #it must be a number
        break
    else:
        print("It must be numberic digit")

#Employee Name (this is required, and must be comprised of primarily upper and lower case letters. Spaces, the ' and - character are all allowed as well.        
while True:
    employee_name = input("Enter Employee Name\n")
    if employee_name.strip()=="":   #if employee name is empty
        print("Employee Name should not be empty")
    elif employee_name.lower().replace("-","").replace("'","").replace(" ","").isalpha(): #Spaces, the ' and - character are all allowed as well.
        break
    else:
        print("please enter correct Name")

#Employee Email Address (this is required, and must be comprised of primarily of alphanumeric characters. It also cannot contain any of the following characters: ! " ' # $ % ^ & * ( )  = + , < > / ? ; : [ ] { } \ ).        
while True:
    employee_email = input("Enter Employee Email address\n")
    if len(set("!'#$%^&*()=+,<>/?;:[]{ }").intersection(set(employee_email)))>0: #if users enters these characters it will not accepct
         print("Please Enter Correct Email Address of Employee")
    elif employee_email.strip().replace("@","").replace(".","").replace("_","").isalnum(): #if user enters @._ it will accepct
        break
    else:
        print("Employee Email cant be Empty")
#Employee salary (this is required, and must be a floating point number between 18 and 27)        
while True:
    employee_salary = input("Enter Employee Salary\n")
    try:
         employee_salary = float(employee_salary)
         if employee_salary < 18 or employee_salary > 27: #if user enters value less than 18 and greater than 27 it will not accepct
             print("employee salary should be in between 18 and 27")
         else:
             break
    except:
        print("salary must be a floating Point")
        

employees_list = list() #created an empty list
my_dict = {"Employee_ID":employee_id,"Employee_Name":employee_name,"Employee_Email":employee_email,"Employee_Salary":employee_salary} #create a list of dictionaries that hold all of the information.
employees_list.append(my_dict)

for i in employees_list:
    i["Employee_Name"] = "IT Department " + i["Employee_Name"]   #Add the words "IT Department" to each name in your list
    i["total_updated_salary"] = i["Employee_Salary"]*1.3         #Update salary information to be 30% higher than the number provided to reflect total salary information with benefits included
print(employees_list)

#GitHub Link : https://github.com/
#Repository Name : week6