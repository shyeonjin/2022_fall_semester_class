class Stock:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def set_name(self,k):
        self.k=k

    def set_code(self,k):
        self.k=k

a = Stock(None, None)
a.set_code("005930")
print(a.k)