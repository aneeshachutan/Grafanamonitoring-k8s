import unittest
from firstapp import hello
class TestFirstApp(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello World! Lets sail together - First App.\n")
if __name__ == '__main__':
  unittest.main()
