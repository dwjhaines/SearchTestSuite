import unittest
import HTMLTestRunner
from time import strftime
from test_basic_search import BasicSearchTest

# get all tests from the test classes
basic_search_tests = unittest.TestLoader().loadTestsFromTestCase(BasicSearchTest)

############################################################### Settings ################################################
useTestRunner = False                # If tests are failing or not working it is easier to debug with this set to False
runFullTestSuite = True             # True to run all tests, False to run a single set of tests
singleTest = basic_search_tests     # Select the test to run if not running all tests
sw_version = 'T 7.2.1.231'          # This will be printed in the Test Runner test report.
dir = "c:\TestResults"              # Directory where test results will end up if using Test Runner
#########################################################################################################################

if (runFullTestSuite == True):
    # Run all tests
    test_suite = unittest.TestSuite([basic_search_tests])
else:
    # Run a single set of tests (choose the tests from above and add to settings)
    test_suite = unittest.TestSuite([singleTest])

if (useTestRunner == True):
    # open the report file
    time = strftime("%Y_%m_%d_%H_%M")
    outfile = open(dir + "\SearchTests_" + time + ".html", "w")
     
    # configure HTMLTestRunner options
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Go! Search Test Report', version=sw_version)
     
    # run the suite using HTMLTestRunner
    runner.run(test_suite)
else:
    # Run tests outside of TestRunner.
    unittest.TextTestRunner(verbosity=2).run(test_suite)

