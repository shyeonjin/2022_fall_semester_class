class 부모:
  def 호출(self):
    print("부모호출")

class 자식(부모):
  def 호출(self):
    print("자식호출")

나 = 자식()
나.호출()

# 결과 자식호출
# 자식을 인스턴스해서 호출함수를 사용
# super을 안썼기에 자식호출이 나옴