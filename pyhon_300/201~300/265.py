class Stock:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def set_name(self,k):
        self.k=k

    def set_code(self,k):
        self.k=k

    def get_name(self):
        return self.a

    def get_code(self):
        return self.b
삼성 = Stock("삼성전자", "005930")
print(삼성.a)
print(삼성.b)
print(삼성.get_name())
print(삼성.get_code())