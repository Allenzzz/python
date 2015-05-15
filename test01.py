# for i in range(5000):
# 	aa=[]
# 	nu=('2015%04d' % (i+1))
# 	# gender='M' if i//2 else 'F'
# 	# addr=('Shenzhen shennan road No. %04d' % (i+1))
# 	# aa.append((nu,'Ako','yoga',gender,addr))
# 	aa.append((nu,'Ako'))
# 	print aa

# import os
# print dir(os)
# print help(os)

# import glob

# print glob.glob('*.py')

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print average([20, 30, 70])
    40.0
    """
    return sum(values, 0.0) / len(values)

import doctest
print doctest.testmod()   # automatically validate the embedded tests

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main() # Calling from the command line invokes all tests