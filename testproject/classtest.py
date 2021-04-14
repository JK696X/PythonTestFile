def greeting(name):
  print("Hello, " + name)


class myClass:
	def __init__(self,val):
		self.val=val
	def getVal(self):
		return self.val

# Defining a class
class Student:
    def __init__(self, name, course):
        self.course = course
        self.name = name

    def get_student_details(self):
        print("Your name is " + self.name + ".")
        print("You are studying " + self.course)