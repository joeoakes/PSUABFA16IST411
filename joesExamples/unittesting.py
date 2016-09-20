import unittest
# assertEquals(a, b, msg=None) a == b
# assertNotEqual(a, b, msg=None) a != b
# assertTrue(x) bool(x) is True
# assertFalse(x) bool(x) is False
# assertIs(a, b) a is b
# assertIsNot(a, b) a is not b
# assertIsNone(x) x is None
# assertIsNotNone(x) x is not None
# assertIn(a, b) a in b
# assertNotIn(a, b) a not in b
# assertIsInstance(a, b) isinstance(a, b)
# assertNotIsInstance(a, b) not isinstance(a, b)
# assertRaises

def fun1(var1):
    return var1 + 1

def fun2(var2):
    return var2 * 2

def funTrue():
    return True

def funFalse():
    return False

# function to raise exception
def funRaises():
    try:
      1/0
    except ZeroDivisionError as err:
      print('Error', err)
    return

#subclass 
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun1(3), 4)

    def test2(self):
        self.assertEqual(fun1(3), 5)

    def test3(self):
        self.assertFalse(funFalse())

    def test4(self):
        self.assertTrue(funTrue())

    def test5(self):
        self.assertRaises(funRaises())

    def test6(self):
        self.assertRaises(funTrue())

if __name__ == '__main__':
    unittest.main()
