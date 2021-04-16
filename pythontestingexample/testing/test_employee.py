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

from employee import Employee


class TestEmployee(unittest.TestCase):
    def test_email(self):
        emp_1 = Employee("Corey", "Shaefer", 50000)
        emp_2 = Employee("Sue", "Smith", 60000)

        self.assertEqual(emp_1.email, "Corey.Shaefer@email.com")
        self.assertEqual(emp_2.email, "Sue.Smith@email.com")

        emp_1.first = "John"
        emp_2.first = "Jane"

        self.assertEqual(emp_1.email, "John.Shaefer@email.com")
        self.assertEqual(emp_2.email, "Jane.Smith@email.com")

    def test_fullname(self):
        emp_1 = Employee("Corey", "Schafer", 50000)
        emp_2 = Employee("Sue", "Smith", 60000)

        self.assertEqual(emp_1.fullname, "Corey Schafer")
        self.assertEqual(emp_2.fullname, "Sue Smith")

        emp_1.first = "John"
        emp_2.first = "Jane"

        self.assertEqual(emp_1.fullname, "John Schafer")
        self.assertEqual(emp_2.fullname, "Jane Smith")

    def test_apply_raise(self):
        emp_1 = Employee("Corey", "Schafer", 50000)
        emp_2 = Employee("Sue", "Smith", 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)


if __name__ == "__main__":
    unittest.main()
