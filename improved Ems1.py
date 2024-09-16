from ems2 import employee


emplist={1:["Preeti","Developer",45000.0],
         2:["Mansi","IT Testing",30000.0],
         3:["Ronak","IT Manager",75000.0],
         4:["Rohit","IT Executive",16000.0]}


print("Welcome to Employee Management System (EMS) !!")
while True:
    #displaying the menu
    print("How can I help you?")
    print("1.Add Employee")
    print("2.Update Employee")
    print("3.List Employees")
    print("4.Remove Emloyee")
    print("5.Exit EMS")

    #accepting the value
    c=input("Enter your choice:")
    if c=='1':  ##################### Adding a record
         try:
             eid=int(input("Enter employee ID:"))
         except ValueError:
             print("\nEnter valid employee ID\n")
             continue
         if eid not in emplist.keys():
             e=employee()
             emplist.update({eid:e.addemp()})
             del e
             print("Employee added successfully!\n")
         else:
             print("\nEmployee ID already exists \n")
             
    elif c=='2':    ################# updating a record
        try:
            eid=int(input("Enter Employee ID to be updated:"))
        except ValueError:
            print("Enter valid employee ID\n")
            continue
        if eid in emplist.keys():
            e=employee()
            e.assign(emplist[eid],eid)
            emplist.update({eid:e.updateemp()})
            del e
            print("Employee updated successfully!\n")
        else:
            print("\nEmployee ID does not exist\n")
            
    elif c=='3':    ####################listing the record
        print("ID \tName \tPosition \tSalary")
        for eid in emplist:
            e=employee()
            e.assign(emplist[eid],eid)
            e.checkemp()
            del e
        print("All Employee details printed successfuly\n")
        
    elif c=='4':    ####################deleting an record
        try:
            eid=int(input("Enter employee ID to be removed:"))
        except ValueError:
            print("Enter valid employee ID\n")
            continue
        if eid in emplist.keys():
            emplist.pop(eid)
            print("Employee removed Successfuly\n")
        else:
            print("Employee ID does not exist\n")
    elif c=='5':
        print("Thanks for using EMS!!\nHave a great day Ahead!")
        break
    else:
        print("Enter valid input\n")
print("Bye")
