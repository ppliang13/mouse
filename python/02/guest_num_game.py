import random

#猜数字游戏 
#生成1到1000之间的随机整数
random_integer = random.randint(1, 1000)  

guest_num=-1
times=0
while random_integer!=guest_num:
  user_input = input("请输入一个数字: ")
  times=times+1
  try:
      guest_num = float(user_input)
      if(guest_num<random_integer):
        print(f"你输入[{guest_num}]的数字比它小")
      elif(guest_num>random_integer):
        print(f"你输入[{guest_num}]的数字比它大")
      else:
        print(f"你{times}次就猜中答案！")  
  except ValueError:
      print("无法转换为数字。请确保输入的是有效数字。")
