#import sys
#sys.path += ['../src']

#from test_func import *

def func(x):
    return x + 2

def test_answer():
    assert func(3) == 5
