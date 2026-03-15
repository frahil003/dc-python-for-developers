import math, unittest

def func_factorial(number):
    if number < 0:
        raise ValueError('Factorial is not defined for negative values')
    factorial = 1
    while number > 1:
        factorial = factorial * number
        number = number - 1
    return factorial

class TestFactorial(unittest.TestCase):
    def test_positives(self):
        # Add the test for testing positives here
        self.assertEqual(func_factorial(5), 120)

    def test_zero(self):
        # Add the test for testing zero here
        self.assertEqual(func_factorial(0), 1)

    def test_negatives(self):
      	# Add the test for testing negatives here
        with self.assertRaises(ValueError):
            func_factorial(-1)

###############################################################

def is_prime(num):
    if num == 1: return False
    up_limit = int(math.sqrt(num)) + 1
    for i in range(2, up_limit):
        if num % i == 0:
            return False
    return True

class TestSuite(unittest.TestCase):
    def test_is_prime(self):
        # Check that 17 is prime
        self.assertEqual(is_prime(17), True)
        
        # Check that 6 is not prime
        self.assertFalse(is_prime(6), False) # WIRD NICHT AUSGEFÜHRT
        
        # Check that 1 is not prime
        self.assertFalse(is_prime(1), False) # WIRD NICHT AUSGEFÜHRT
    
    def test_is_prime1(self):
        # Check that 17 is prime
        self.assertEqual(is_prime(17), True)        

#######################################################

"""
python3 -m unittest -v err_factorial_unittest.py 
"""

########################################################

class TestWord(unittest.TestCase):
    # Fixture setup method
    def setUp(self):
        # Initialize the word banana here
        self.word = "banana"

    # Test method
    def test_the_word(self):
        # Add the tests here
        self.assertNotIn("B", self.word)
        self.assertNotIn("y", self.word)
        self.assertIn("b", self.word)
    
    # Fixture teardown method
    def tearDown(self):
        # Delete the word variable here
        del self.word

"""
python3 -m unittest -k "TestWord" chapter_04.py
"""

####################################################

def check_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

def create_data():
    return ['level', 'step', 'peep', 'toot']

class TestPalindrome(unittest.TestCase):
    def setUp(self):
        # Initialize data here
        self.data = create_data()
    
    def test_func(self):
        expected_result = [True, False, True, True]
        data_checked = list(map(check_palindrome, self.data))
        # Verify the checked data here
        self.assertEqual(data_checked, expected_result)

    def tearDown(self):
        # Clear the data here
        self.data.clear()



