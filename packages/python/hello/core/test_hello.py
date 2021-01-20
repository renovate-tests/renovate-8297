import unittest

from packages.python.hello.core.hello import say_hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(say_hello("Peter"), "Hello Peter")


if __name__ == "__main__":
    unittest.main()
