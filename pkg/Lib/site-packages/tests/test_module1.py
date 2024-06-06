import unittest
from my_package.module1 import foo

class TestModule1(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(foo(), "Hello from module1!")

if __name__ == '__main__':
    unittest.main()
