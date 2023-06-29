import sys
sys.path += ['../src']

from src.funf import *

def test_answer():
    assert func(3) == 6
