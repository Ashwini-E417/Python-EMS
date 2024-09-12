from ems2 import employee, checkid, getindex



emplist=[[1,"Preeti","Developer",45000],
         [2,"Mansi","IT Testing",30000],
         [3,"Ronak","IT Manager",75000],
         [4,"Rohit","IT Executive",16000]]

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
         if not checkid(eid,emplist):
             e=employee()
             e.addemp(eid)
             emplist.append([e.id,e.name,e.pos,e.sal])
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
        if checkid(eid,emplist):
            index=getindex(emplist,eid)
            e=employee()
            e.assign(emplist[index])
            print("Existing Values are as Follows:")
            e.checkemp()
            print("Enter new values:")
            e.addemp(e.id)
            emplist.pop(index)
            emplist.insert(index,[e.id,e.name,e.pos,e.sal])
            del e
            print("Employee updated successfully!\n")
        else:
            print("\nEmployee ID does not exist\n")
            
    elif c=='3':    ####################listing the record
        print("ID \tName \tPosition \tSalary")
        for i in emplist:
            e=employee()
            e.assign(i)
            e.checkemp()
            del e
        print("All Employee details printed successfuly\n")
    elif c=='4':    ####################deleting an record
        try:
            eid=int(input("Enter employee ID to be removed:"))
        except ValueError:
            print("Enter valid employee ID\n")
            continue
        if checkid(eid,emplist):
            index=getindex(emplist,eid)
            emplist.pop(index)
            print("Employee removed Successfuly\n")
        else:
            print("Employee ID does not exist\n")
    elif c=='5':
        print("Thanks for using EMS!!\nHave a great day Ahead!")
        break
    else:
        print("Enter valid input\n")
print("Bye")
