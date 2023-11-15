try:
  print(4/0)
except ZeroDivisionError:
  print("You can't divide by zero!")  


# print("Give me two numbers,and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#   first_number =input("\nFirst number:")
#   if first_number == 'q':
#     break
#   second_number=input("Second number:")
#   if(second_number=='q'):
#     break
#   answer=int(first_number)/int(second_number)
#   print(answer)

filename='alice.txt'
try:
  with open(filename,encoding="utf-8") as f:
    contents=f.read()
except FileNotFoundError:
  print(f"文件不存在 {filename}")



