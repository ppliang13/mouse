#前一百万位是否可以出现每个人的生日
#案例：0110 一月十日 1201 十二月一日 所有日期是四位

from mpmath import mp
from day import Day

day_dict={}
num=1
# 一月
month = "01"
for value in range(1, 32):
    day_num = "{:02d}".format(value)
    month_day = month + day_num
    day_dict[month_day] = Day(month_day, num)
    num += 1

# 二月
month = "02"
for value in range(1, 30):  # 闰年
    day_num = "{:02d}".format(value)
    month_day = month + day_num
    day_dict[month_day] = Day(month_day, num)
    num += 1

# 三月
month = "03"
for value in range(1, 32):
    day_num = "{:02d}".format(value)
    month_day = month + day_num
    day_dict[month_day] = Day(month_day, num)
    num += 1

# 四月
month = "04"
for value in range(1, 31):
    day_num = "{:02d}".format(value)
    month_day = month + day_num
    day_dict[month_day] = Day(month_day, num)
    num += 1

# 五月
month = "05"
for value in range(1, 32):
    day_num = "{:02d}".format(value)
    month_day = month + day_num
    day_dict[month_day] = Day(month_day, num)
    num += 1

# 六月
month = "06"
for value in range(1, 31):
    day_num = "{:02d}".format(value)
    month_day = month + day_num
    day_dict[month_day] = Day(month_day, num)
    num += 1

# 七月
month = "07"
for value in range(1, 32):
    day_num = "{:02d}".format(value)
    month_day = month + day_num
    day_dict[month_day] = Day(month_day, num)
    num += 1

# 八月
month = "08"
for value in range(1, 32):
    day_num = "{:02d}".format(value)
    month_day = month + day_num
    day_dict[month_day] = Day(month_day, num)
    num += 1

# 九月
month = "09"
for value in range(1, 31):
    day_num = "{:02d}".format(value)
    month_day = month + day_num
    day_dict[month_day] = Day(month_day, num)
    num += 1

# 十月
month = "10"
for value in range(1, 32):
    day_num = "{:02d}".format(value)
    month_day = month + day_num
    day_dict[month_day] = Day(month_day, num)
    num += 1

# 十一月
month = "11"
for value in range(1, 31):
    day_num = "{:02d}".format(value)
    month_day = month + day_num
    day_dict[month_day] = Day(month_day, num)
    num += 1

# 十二月
month = "12"
for value in range(1, 32):
    day_num = "{:02d}".format(value)
    month_day = month + day_num
    day_dict[month_day] = Day(month_day, num)
    num += 1

# print("日期字典一共:",len(day_dict))
# for date, day_obj in day_dict.items():
#   print(f"{day_obj.num} {date}")

# 设置精度为一百万位
mp.dps = 100000+1

# 获取π的小数部分
pi_decimal_part = str(mp.pi)[2:]
i=0
while i<len(pi_decimal_part)-3:
  dayStr=pi_decimal_part[i:i+4]
  if dayStr in day_dict:
    day_dict[dayStr].exist(i)
  i+=1

index=0
sum=0
for key,day in day_dict.items():
  if day.flag==True:
    sum+=1
    if day.index>index:
      index=day.index
    print(key,day.index)

print("最大index是:",index)
print("一共有:",sum)
print(pi_decimal_part[index:index+4])



mp.dps = 60879+1
pi_60876 = str(mp.pi)[2:]
print(pi_60876[index:index+15])

mp.dps = 100000+1
pi_100000 = str(mp.pi)[2:]
print(pi_100000[index:index+4])
