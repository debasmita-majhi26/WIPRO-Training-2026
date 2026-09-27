import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        print("Test started")

    def tearDown(self):
        print("Test finished")

    def test_addition(self):
        result = 10 + 20
        self.assertEqual(result, 30)


if __name__ == "__main__":
    unittest.main()