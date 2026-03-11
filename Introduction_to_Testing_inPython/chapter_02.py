import pytest

def multiple_of_two(num):
    if num == 0:
        raise(ValueError)
    return num % 2 == 0

def test_numbers():
    # Write the "True" test below
    assert multiple_of_two(2) is True
    # Write the "False" test below
    assert multiple_of_two(3) is False

def test_zero():    
	# Add a context for an exception test here
  with pytest.raises(ValueError):
   	# Check zero input below
    multiple_of_two(0)

##################################################

'''
Im Terminal ausführen
>>> pytest chapter_02.py
'''

##################################################

'''
Im Terminal ausführen
>>> pytest chapter_02.py -k "numbers"
'''

##################################################

# Add the pytest marker decorator here
@pytest.mark.xfail
def test_fails():
    # Write any assert test that will fail
    assert multiple_of_two(5) is True

####################################################
from datetime import datetime

day_of_week = datetime.now().isoweekday()

def get_unique_values(lst):
    return list(set(lst))

condition_string = 'day_of_week == 6'
# Add the conditional skip marker and the string here
@pytest.mark.skipif(condition_string)
def test_function():
	# Complete the assertion tests here
    assert get_unique_values([1,2,3]) == [1,2,3]
    assert get_unique_values([1,2,3,1]) == [1,2,3,4]
