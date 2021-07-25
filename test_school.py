import unittest

from school import Student, WebProgramming


class TestWebProgramming(unittest.TestCase):

    def setUp(self):
        self.john = Student(name="John", grade=91)
        self.sarah = Student(name="Sarah", grade=90)
        self.marc = Student(name="Marc", grade=84)
        self.george = Student(name="George", grade=84)

