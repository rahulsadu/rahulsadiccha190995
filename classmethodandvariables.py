class Company:
    companyname="IBM"

    def __init__(self,i,name,city,sal):
        self.identity=i
        self.name=name
        self.city=city
        self.sal=sal

    def show(self):
        print("id is:", self.identity)
        print("name is:",self.name)
        print("city is:" , self.city )
        print("salary is:", self.sal)
        print("company name:" ,Company.companyname)


Rahul=Company(101,"rahul","pune",46000)
Saddiccha=Company(102,"sadicchha","pune",40000)

Rahul.show()
Saddiccha.show()

@classmethod
def company_name_change(cls):
    cls.company_name_change="INFOSYS"
    Company.company_name_change()

Rahul.show()
Saddiccha.show()