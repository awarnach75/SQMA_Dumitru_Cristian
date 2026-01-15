import unittest

class MyHomeworkTests(unittest.TestCase):

    def test_one(self):
        print("Running Test One...")
        self.assertTrue(True)

    def test_two(self):
        print("Running Test Two...")
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':

    unittest.main()
