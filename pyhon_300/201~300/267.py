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

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(삼성.money)