Employees_Database=[]
chk=0
while chk<1:
    choice=int((input(" Enter Your Option from 1 to 5: ")))
    if choice==1:
        name = str(input("Enter Employee Name: "))
        age = int(input("Enter Employee Age: "))
        salary = float(input("Eneter Employee Salary: "))
        Employees_Database.append({"employee_name" :name,
        'employee_age': age,
        'employee_salary': salary})
    elif choice==2:
        if len(Employees_Database)==0:
            print('No Employees in the List')
        else:    
            for employee in Employees_Database:
                print(f'employee name is {employee["employee_name"]}, '
                        f'he/she has {employee["employee_age"]} and his/her salary is {employee["employee_salary"]}')
    elif choice==3:
        age_from=int(input("Enter age from: "))
        age_to = int(input("Enter age to: "))
        
        for employee in Employees_Database:
            if employee["employee_age"]>age_from and employee["employee_age"]<age_to:
                print(f'Employee {employee["employee_name"]} was romved from the Database')
                Employees_Database.remove(employee)
    elif choice==4:
        emloyee_name=input("Enter Employee Name: ")
        updated_salary=float(input("Enter New Salary: "))
        for employee in Employees_Database:
            if employee["employee_name"]== emloyee_name:
                employee["employee_salary"]=updated_salary
    elif choice==5:
        break
    else:
        print(" Please, Enter Valid Choice")
    
    