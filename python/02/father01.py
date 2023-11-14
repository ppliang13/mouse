class A:
    def __init__(self):
        print("Initializing class A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Initializing class B")

class C(A):
    def __init__(self):
        super().__init__()
        print("Initializing class C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("Initializing class D")

obj = D()
