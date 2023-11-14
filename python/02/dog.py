class Dog:
  """一次模拟小狗的测试"""

  def __init__(self,name,age):
    # 初始化属性
    self.name=name
    self.age=age
  
  def sit(self):
    print(f"{self.name} is now sitting.")
  
  def roll_over(self):
    print(f"{self.name} rolled over!")

my_dog=Dog("while",6)
print(my_dog.name)
print(my_dog.age)
my_dog.sit()