class A:
    def __init__(self, value):
        self.value = value

class B(A):
    def __init__(self, value, b_value):
        A.__init__(self, value)  # 直接调用 A 类的构造方法
        self.b_value = b_value

class C(A):
    def __init__(self, value, c_value):
        A.__init__(self, value)  # 直接调用 A 类的构造方法
        self.c_value = c_value

class D(B, C):
    def __init__(self, value, b_value, c_value, d_value):
        B.__init__(self, value, b_value)  # 直接调用 B 类的构造方法
        C.__init__(self, value, c_value)  # 直接调用 C 类的构造方法
        self.d_value = d_value

d=D(1,2,3,4)
print(d)
