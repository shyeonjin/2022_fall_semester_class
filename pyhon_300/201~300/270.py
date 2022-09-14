class Stock:
    def __init__(self,a,b,per,pbr,money):
        self.a=a
        self.b=b
        self.per=per
        self.pbr=pbr
        self.money=money
    def set_name(self,k):
        self.k=k

    def set_code(self,k):
        self.k=k

    def get_name(self):
        return self.a

    def get_code(self):
        return self.b
        
    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

l=[]

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

l.append(삼성)
l.append(현대차)
l.append(LG전자)

for i in l:
    print(i.b, i.per) 