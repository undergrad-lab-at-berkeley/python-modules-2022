import math
import random
import __main__
import datetime
import unittest
import numpy as np
from IPython.display import Markdown, display

########## TESTS ##########
class Tests(unittest.TestCase):

    def test_2a(self, f):
        self.assertAlmostEqual(f(10), [2, 5])
        self.assertAlmostEqual(f(104939402), [2,17, 31, 99563])

    def test_2b(self, f):
        self.assertEquals(f(20,5,2), 7)
        self.assertEquals(f(30,5,2), 11)
        self.assertEquals(f(40,5,2), 15)
        self.assertEquals(f(40,5,2), 15)
    def test_cat(self, f):
        self.assertEquals(f(10), [1.0, 1.0, 2.0, 5.0, 14.0])
        self.assertEquals(f(102434), [1.0, 1.0, 2.0, 5.0, 14.0, 42.0, 132.0, 429.0, 1430.0, 4862.0, 16796.0, 58786.0, 208012.0])


    





########## TESTS ##########


def printmd(string):
    display(Markdown(string))

tests = Tests()

def run(test_name, *args, hint=False):
    dt = datetime.datetime.now()
    try:
        getattr(tests, test_name)(*args)
    except tests.failureException as e:
        printmd(f'**<span style="color: red;">Failed // {dt}</span>**')
        if hint:
            print('Hint:',  e)
        return
    printmd(f'**<span style="color: green;">Passed // {dt}</span>**')


