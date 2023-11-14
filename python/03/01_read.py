import os

# 获取当前脚本的绝对路径
current_working_directory = os.getcwd()
print("当前工作目录:", current_working_directory)

#全读取
with open('03/pi_digits.txt') as file_object:
  contents=file_object.read()
print(contents)

print("********行读取********")
#行读取
with open("03/pi_digits.txt") as file_object:
  i=1
  for line in file_object:
    formatted_number = "{:02d}".format(i)
    print(f"[{formatted_number}]:{line}".rstrip())
    i+=1

print("********去除空格********")
#去除所有空格
pi=""
with open("03/pi_digits.txt") as file_object:
  for line in file_object:
    pi+=line.replace(" ","").rstrip()

print("pi的长度:",len(pi))

print(pi)

