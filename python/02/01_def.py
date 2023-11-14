
def printMsg(msg):
  print(msg)

printMsg("哈哈哈")


def namePrint(fist_name,last_name):
  print(f"{fist_name} {last_name}")
  return fist_name+" "+last_name

print(namePrint("pi","siliang")+"hahha")

#重载 没有
# def namePrint(fist_name):
#   print(f"{fist_name}")

# namePrint("pi")
# namePrint("pi","siliang")
