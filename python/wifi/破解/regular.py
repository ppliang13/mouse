import itertools



# 定义手机号的前两位
prefix = '13'

# 生成后面9位数字的所有组合
suffix_combinations = itertools.product(range(10), repeat=9)

# 打印前几个手机号作为示例
for suffix in itertools.islice(suffix_combinations, 10):
    full_phone_number = f"{prefix}{''.join(map(str, suffix))}"
    print(full_phone_number)
