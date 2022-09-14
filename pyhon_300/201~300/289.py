class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")

나 = 자식()
# 나에 인스턴스를 받아서 자식안에 있는 
# 초기화 값인 자식생성이 나온다.