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

areum = Human("불명","미상","모름")
areum.who()


areum = Human("아름",25,"여자")
areum.who()
    