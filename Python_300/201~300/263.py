class Stock:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def set_name(self,k):
        self.k=k

a = Stock(None, None)
a.set_name("삼성전자")
print(a.k)