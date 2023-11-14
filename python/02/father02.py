class A:
    def __init__(self, value):
        self.value = value

class B(A):
    def __init__(self, value, b_value):
        super().__init__(value)
        self.b_value = b_value

class C(A):
    def __init__(self, value, c_value):
        super().__init__(value)
        self.c_value = c_value

class D(B, C):
    def __init__(self, value, b_value, c_value, d_value):
        super(B, self).__init__(value)  # 指定调用 B 类的构造方法
        super(C, self).__init__(value)  # 指定调用 C 类的构造方法
        self.d_value = d_value
