test_durations = [245.50, 189.99, 312.75, 156.20, 428.90, 201.35, 167.80]

 # Complete the function
def test_report(durations):
    num_tests = len(durations)
    
    # Calculate total test time
    total_time = sum(durations)
    
    print("=== Test Report ===")
    print("Total Tests: ", num_tests)
    print("Total Execution Time (s): ", total_time)

# Generate the report for recent test runs
test_report(test_durations)