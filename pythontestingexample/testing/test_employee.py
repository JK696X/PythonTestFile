# Part of standard libary
import unittest

# Use this for testing absolute/relative path
import sys
import os
import requests

# Use this for importing mock with our unit testing
from unittest.mock import patch

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
    # runs before all of testing
    @classmethod
    def setUpClass(cls):
        # Used for resource intensive stuff
        print("setupClass")

    # runs before all of testing
    @classmethod
    def tearDownClass(cls):
        # Used for resource intensive stuff
        print("teardownClass")

    # runs before every test case
    def setUp(self):
        print("setUp\n")
        self.emp_1 = Employee("Corey", "Schafer", 50000)
        self.emp_2 = Employee("Sue", "Smith", 60000)
        pass

    # runs AFTER every test case
    def tearDown(self):
        print("tearDown\n")
        pass

    def test_email(self):
        print("test_email\n")
        self.assertEqual(self.emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "John.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Smith@email.com")

    def test_fullname(self):
        print("test_fullname\n")
        self.assertEqual(self.emp_1.fullname, "Corey Schafer")
        self.assertEqual(self.emp_2.fullname, "Sue Smith")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "John Schafer")
        self.assertEqual(self.emp_2.fullname, "Jane Smith")

    def test_apply_raise(self):
        print("test_apply_raise\n")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        print("Printing test_monthly_schedule with patch")
        with patch("employee.requests.get") as mocked_get:
            # Successful Response
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Schafer/May")
            self.assertEqual(schedule, "Success")

            # Failed Response
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Smith/June")
            self.assertEqual(schedule, "Bad Response!")


if __name__ == "__main__":
    unittest.main()
