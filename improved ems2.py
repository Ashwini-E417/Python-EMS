class employee:
        
    def assign(self,l,eid):
        self.id=eid
        self.name=l[0]
        self.pos=l[1]
        self.sal=l[2]

    def checkemp(self):
        print(f"{self.id} \t{self.name} \t{self.pos} \t{self.sal}")

    def addemp(self):
        self.name=input("Enter Name:")
        self.pos=input("Enter position:")
        self.sal=float(input("Enter Salary:"))
        return [self.name,self.pos,self.sal]

    def __del__(self):
        print()


    def updateemp(self):
        while True:
            print("Existing Values are as Follows:")
            self.checkemp()
            print("\nEnter the value you want to change:")
            print("Press 1 to change Name")
            print("Press 2 to change position")
            print("Press 3 to change salary")
            
            ch=input("\nEnter your choice:")
            if ch=='1':
                self.name=input("Enter Name:")
                break
            elif ch=='2':
                self.pos=input("Enter position:")
                break
            elif ch=='3':
                self.sal=float(input("Enter Salary:"))
                break
            else:
                print("Enter Valid input")
        return [self.name,self.pos,self.sal]
