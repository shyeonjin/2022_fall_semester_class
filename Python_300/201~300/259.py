class Human:
    def __init__(self, name, age, a):
        self.name = name
        self.age = age
        self.a = a
    def who(self):
        print(f"이름: {self.name},나이: {self.age},성별: {self.a}")

    def setinfo(self,name,age,a):
        self.name = name
        self.age = age
        self.a = a
    def __del__(self):
        print("나의 죽음을 알리지마라")
areum = Human("아름", 25, "여자")
del(areum)