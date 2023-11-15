filename="03/programming.txt"

# 覆盖
with open(filename,'w') as file_object:
  file_object.write("I love programming. 1")
  file_object.write("\n")
  file_object.write("I love programming. 2")
  file_object.write("\n")

#追加
with open(filename,'a') as file_object:
  file_object.write("I love programming. 3")
  file_object.write("\n")
  file_object.write("I love programming. 4")