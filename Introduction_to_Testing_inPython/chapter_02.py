# Import the pytest library
import pandas as pd
import pytest

# Define the fixture decorator
@pytest.fixture
# Name the fixture function
def prepare_data():
    return [i for i in range(10)]

# Create the tests
def test_elements(prepare_data):
    assert 9 in prepare_data
    assert 10 not in prepare_data

'''
Im Terminal ausführen
>>> pytest chapter_02.py
'''

##################################################

# Define the fixture for returning the length
@pytest.fixture
def list_length():
    return 10

# Define the fixture for a list preparation
@pytest.fixture
def prepare_list(list_length):
    return [i for i in range(list_length)]

def test_9(prepare_list):
    assert 9 in prepare_list
    assert 10 not in prepare_list

####################################################

@pytest.fixture
def init_list():
    return []

# Declare the fixture with autouse
@pytest.fixture(autouse=True)
def add_numbers_to_list(init_list):
    init_list.extend([i for i in range(10)])

# Complete the tests
def test_elements_2(init_list):
    assert 1 in init_list
    assert 9 in init_list

######################################################

@pytest.fixture
def prepare_data_3():
    data = [i for i in range(10)]
    # Return the data with the special keyword
    yield data
    # Clear the data list
    data.clear()
    # Delete the data variable
    del data

def test_elements_3(prepare_data):
    assert 9 in prepare_data
    assert 10 not in prepare_data

#######################################################

@pytest.fixture
def data():
    df = pd.read_csv('../data/games.csv')
    # Return df with the special keyword
    yield df
    # Remove all rows in df
    df.drop(df.index, inplace=True)
    # Delete the df variable
    del df

def test_type(data):
    assert type(data) == pd.DataFrame

def test_shape(data):
    assert data.shape[0] == 1512




