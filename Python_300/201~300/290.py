class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()


# 자식을 인스턴스를 하여 초기화인 자식생성이 나온고
# super로인해 부모 class인 초기화인 부모생성도 나온다.