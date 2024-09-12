def checkemployee(l):
    for i in l:
        print("{}\t{}\t{}\t{}".format(i[0],i[1],i[2],i[3]))


class employee:
        
    def assign(self,l):
        self.id=l[0]
        self.name=l[1]
        self.pos=l[2]
        self.sal=l[3]

    def checkemp(self):
        print(f"{self.id} \t{self.name} \t{self.pos} \t{self.sal}")

    def addemp(self,eid):
        self.id=eid
        self.name=input("Enter Name:")
        self.pos=input("Enter position:")
        self.sal=float(input("Enter Salary:"))

    def __del__(self):
        print()
######################## normal function- not a part of the class
def checkid(id,emplist):
    exist=False
    for i in emplist:
        if id==i[0]:
            exist=True
            break
    return exist

def getindex(emplist,eid):
    index=0
    for i in emplist:
        if i[0]==eid:
            break
        else:
            index+=1
    return index
