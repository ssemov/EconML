import unittest
import sys
from io import StringIO

# Redirect stdout to capture output
old_stdout = sys.stdout
sys.stdout = StringIO()

# List of test cases to run
test_cases = [
    'econml.tests.test_driv.TestDRIV',
    'econml.tests.test_inference',
    'econml.tests.test_statsmodels',
    'econml.tests.test_dml.TestDML.test_ignores_final_intercept',
    'econml.tests.test_discrete_outcome.TestDiscreteOutcome.test_accuracy',
    'econml.tests.test_discrete_outcome.TestDiscreteOutcome.test_accuracy_iv'
]

# Run the tests
for test_case in test_cases:
    suite = unittest.TestLoader().loadTestsFromName(test_case)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Get the output
output = sys.stdout.getvalue()

# Restore stdout
sys.stdout = old_stdout

# Save the output to a file
with open('test_results.txt', 'w') as f:
    f.write(output)

print("Test results have been saved to test_results.txt")
