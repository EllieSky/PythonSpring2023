import unittest

def print_hi(name):
    return f'Hello {name}'


class MyTestCase(unittest.TestCase):
    def test_hello_world(self):
        expected = 'Hello World'
        actual = print_hi("world")
        self.assertEqual(expected.lower(), actual.lower())  # add assertion here



if __name__ == '__main__':
    unittest.main()
