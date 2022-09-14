import random
class Account:
    def __init__(self,name,num):
        self.name=name
        self.num=num
        self.bankname="SC은행"
        self.acnum=((str(random.randint(0, 999)).zfill(3))+"-"+
        str(random.randint(0, 99)).zfill(2)+"-"+str(random.randint(0, 999999)).zfill(6))



counter=Account("심현진",100)
print(counter.name)
print(counter.num)
print(counter.bankname)
print(counter.acnum)