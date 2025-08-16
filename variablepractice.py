class Company:
    company_name="IBM"
    def __init__(self,id1,name,city,sal):
        self.id=id1
        self.name=name
        self.city=city
        self.sal=sal
        print("inside class:", id(self))
    def bonus_cal(self):
        bonus=(self.sal/100)*15
        gs=self.sal+bonus
        return bonus,gs
    def show(self):
        print("ID:",self.id)
        print("Name:",self.name)
        print("city:",self.city)
        print("original sal:",self.sal)
        b,g=self.bonus_cal()
        print("Bonus:",b)
        print("Gross sal:",g)

        print("Company_name:",Company.company_name)
    @classmethod
    def company_name_change(cls):
        cls.company_name="INFOSYS"
akashWaghmare=Company(101,'akash',"pune",1000000)
print("outside class:", id(obj))
Company.company_name_change()
obj.show()