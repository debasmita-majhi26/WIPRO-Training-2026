import unittest


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(10 + 20, 30)

    def test_subtraction(self):
        self.assertEqual(30 - 10, 20)


suite = unittest.TestSuite()
suite.addTest(TestCalculator("test_addition"))
suite.addTest(TestCalculator("test_subtraction"))

runner = unittest.TextTestRunner()
runner.run(suite)