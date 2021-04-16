# Part of standard libary
import unittest

# Use this for testing absolute/relative path
import sys
import os

# NOT SURE WHY THIS WORKS BUT IT DOES
absfilepath = os.path.abspath(__file__)  # absolute path of the module
print("here is the absolute file path: " + absfilepath)
filedir = os.path.dirname(os.path.abspath(__file__))  # directory of the module
print("here is the file directory path: " + filedir)
parentdir = os.path.dirname(filedir)  # directory of the module directory
print("here is the parent directory path: " + parentdir)
newpath = os.path.join(
    parentdir, "application"
)  # get the directory for stringfunctions
print("here is the newpath: " + newpath)
sys.path.append(newpath)  # add path into pythonpath

import calc

testvariable = calc.add(3, 2)
print(testvariable)