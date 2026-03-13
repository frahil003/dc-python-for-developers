import pandas as pd
import pytest

def factorial(n):
    if n == 0: return 1
    elif (type(n) == int):
        return n * factorial(n-1)
    else: return -1

# Test case: expected input
def test_regular():
	assert factorial(5) == 120
     
# Test case: zero input
def test_zero():
	assert factorial(0) == 1
      
# Test case: input of a wrong type
def test_str():
    assert factorial("5")
    print('Test passed')

test_str()

#######################################################

# Fixture to prepare the data
@pytest.fixture
def get_df():
    return pd.read_csv('../data/laptops_train.csv')

# Aggregation feature
def agg_with_sum(data, group_by_column, aggregate_column):
    return data.groupby(group_by_column)[aggregate_column].sum()

# Test function
def test_agg_feature(get_df):
    # Aggregate preparation
    aggregated = agg_with_sum(get_df, 'Manufacturer', 'Price')
    # Test the type of the aggregated
    assert type(aggregated) == pd.Series
    # Test the number of rows of the aggregated
    assert aggregated.shape[0] > 0
    # Test the data type of the aggregated
    assert aggregated.dtype in (int, float)

dataframe = pd.read_csv('../data/laptops_train.csv')
agg_df = dataframe.groupby('Manufacturer')['Price'].sum()
print(agg_df)

#################################################################

# Fixture to read the dataframe
@pytest.fixture
def get_df():
    return pd.read_csv('../data/laptops_train.csv')

# Integration test function
def test_get_df(get_df):
    # Check the type
    assert type(get_df) == pd.DataFrame 
    # Check the number of rows
    assert get_df.shape[0]

############################################################

def create_list():
    return [i for i in range(1000)]

def create_set():
    return set([i for i in range(1000)])

def find(it, el=50):
    return el in it

# Write the performance test for a list
def test_list(benchmark):
    benchmark(find, it=create_list())

# Write the performance test for a set
def test_set(benchmark):
    benchmark(find, it=create_set())

################################################################

def test_list1(benchmark):
	# Add decorator here
    @benchmark
    def iterate_list():
		# Complete the loop here
        for i in [i for i in range(1000)]:
            pass

def test_set1(benchmark):
	# Add decorator here
    @benchmark
    def iterate_set():
        # Complete the loop here
        for i in {i for i in range(1000)}:
            pass
