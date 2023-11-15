import json

def greet_user():
  filename="04/username.json"
  try:
    with open(filename) as f: 
      username=json.load(f)
  #    FileNotFoundError 文件不存在异常 json.decoder.JSONDecodeError 文件为空异常
  except (FileNotFoundError,json.decoder.JSONDecodeError) as e:
    username=input("What is your name?")
    with open(filename,'w',encoding='utf-8') as f:
      json.dump(username,f,ensure_ascii=False)
      print(f"We'll remember you when you come back,{username}!")    
  else:
    print(f"Welcome back,{username}!")

greet_user()