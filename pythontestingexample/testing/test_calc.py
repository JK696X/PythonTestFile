# Part of standard libary
import unittest

# Use this for testing absolute/relative path
import sys
import os

# NOT SURE WHY THIS WORKS BUT IT DOES
absfilepath = os.path.abspath(__file__)  # absolute path of the module
# print("here is the absolute file path: " + absfilepath)
filedir = os.path.dirname(os.path.abspath(__file__))  # directory of the module
# print("here is the file directory path: " + filedir)
parentdir = os.path.dirname(filedir)  # directory of the module directory
# print("here is the parent directory path: " + parentdir)
newpath = os.path.join(
    parentdir, "application"
)  # get the directory for stringfunctions
# print("here is the newpath: " + newpath)
sys.path.append(newpath)  # add path into pythonpath

import calc

testvariable = calc.add(3, 2)
# print(testvariable)

# actual testing work
class TestCalc(unittest.TestCase):
    def test_add(self):
        # This should equal 15
        # result = calc.add(10, 5)
        self.assertEqual(calc.add(10, 5), 15)  # Edge Case 1 positive numbers
        self.assertEqual(calc.add(-1, 1), 0)  # Edge Case 2 nothing number
        self.assertEqual(calc.add(-1, -1), -2)  # Edge Case 3 negative numbers
        # or this: self.assertEqual(result, 15)

    def test_subtract(self):
        # This should equal 15
        # result = calc.add(10, 5)
        self.assertEqual(calc.subtract(10, 5), 5)  # Edge Case 1 positive numbers
        self.assertEqual(calc.subtract(-1, 1), -2)  # Edge Case 2 nothing number
        self.assertEqual(calc.subtract(-1, -1), 0)  # Edge Case 3 negative numbers
        # or this: self.assertEqual(result, 15)

    def test_multiply(self):
        # This should equal 15
        # result = calc.add(10, 5)
        self.assertEqual(calc.multiply(10, 5), 50)  # Edge Case 1 positive numbers
        self.assertEqual(calc.multiply(-1, 1), -1)  # Edge Case 2 nothing number
        self.assertEqual(calc.multiply(-1, -1), 1)  # Edge Case 3 negative numbers
        # or this: self.assertEqual(result, 15)

    def test_divide(self):
        # This should equal 15
        # result = calc.add(10, 5)
        self.assertEqual(calc.divide(10, 5), 2)  # Edge Case 1 positive numbers
        self.assertEqual(calc.divide(-1, 1), -1)  # Edge Case 2 nothing number
        self.assertEqual(calc.divide(-1, -1), 1)  # Edge Case 3 negative numbers
        self.assertEqual(calc.divide(5, 2), 2.5)  # Example that catches 'four division'
        # or this: self.assertEqual(result, 15)

        # This is for catching assertion errors. You want to put the error raised first, then the function you'll test,
        # THEN the arguments you want to add to that function
        # self.assertRaises(ValueError, calc.divide, 10, 0)
        # self.assertRaises(ValueError, calc.divide, 10, 2) #This would be a test failure because it isn't throwing that error!

        # You can also run a test within a context, that way you can actually call the function AND catch the
        # assertion error.
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


# Used to automate all the code for unit testing
if __name__ == "__main__":
    unittest.main()