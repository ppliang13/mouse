import unittest

# 待测试的函数
def add(x, y):
    return x + y

# 编写测试类
class TestAddFunction(unittest.TestCase):
    def setUp(self):
        # 在每个测试方法运行前执行的代码
        print("方法执行前方法")
        pass

    def tearDown(self):
        # 在每个测试方法运行后执行的代码
        print("方法执行后方法")
        pass

    # 测试 add 函数
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # 断言 add(2, 3) 的结果应该等于 5
        self.assertEqual(add(-1, 1), 0)  # 断言 add(-1, 1) 的结果应该等于 0
        print("test_add")

    #测试失败的结果
    def test_add_error(self):
      self.assertEqual(add(2,1),13)  
      print("test_add_error")


if __name__ == '__main__':
    unittest.main()

# assertEqual(a, b): 断言 a 等于 b。
# assertNotEqual(a, b): 断言 a 不等于 b。
# assertTrue(x): 断言 x 为真。
# assertFalse(x): 断言 x 为假。
# assertIs(a, b): 断言 a 和 b 是同一对象。
# assertIsNot(a, b): 断言 a 和 b 不是同一对象。
# assertIn(a, b): 断言 a 在 b 中。
# assertNotIn(a, b): 断言 a 不在 b 中。
# assertIsNone(x): 断言 x 是 None。
# assertIsNotNone(x): 断言 x 不是 None。