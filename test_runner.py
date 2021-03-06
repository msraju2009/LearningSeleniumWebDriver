"""Test Suite of the tests based on https://letskodeit.teachable.com/p/practice website."""

import unittest
import HtmlTestRunner
from LearningSeleniumWebDriver.tests.selenium_methods_and_properties_part_one import \
    SeleniumMethodsAndPropertiesPartOne
from LearningSeleniumWebDriver.tests.selenium_methods_and_properties_part_two import \
    SeleniumMethodsAndPropertiesPartTwo
from LearningSeleniumWebDriver.tests.selenium_methods_and_properties_part_three import \
    SeleniumMethodsAndPropertiesPartThree
from LearningSeleniumWebDriver.tests.selenium_methods_and_properties_part_four import \
    SeleniumMethodsAndPropertiesPartFour
from LearningSeleniumWebDriver.tests.selenium_methods_and_properties_part_five import \
    SeleniumMethodsAndPropertiesPartFive


class TestSuite(object):
    """Test suite class."""

    def __init__(self):
        self.selenium_methods_and_properties_one = unittest.TestLoader().loadTestsFromTestCase(
            SeleniumMethodsAndPropertiesPartOne
        )
        self.selenium_methods_and_properties_two = unittest.TestLoader().loadTestsFromTestCase(
            SeleniumMethodsAndPropertiesPartTwo
        )
        self.selenium_methods_and_properties_three = unittest.TestLoader().loadTestsFromTestCase(
            SeleniumMethodsAndPropertiesPartThree
        )
        self.selenium_methods_and_properties_four = unittest.TestLoader().loadTestsFromTestCase(
            SeleniumMethodsAndPropertiesPartFour
        )
        self.selenium_methods_and_properties_five = unittest.TestLoader().loadTestsFromTestCase(
            SeleniumMethodsAndPropertiesPartFive
        )

    def run_test_methods_and_properties_suite(self):
        """Collect tests into test suites."""
        return unittest.TestSuite([self.selenium_methods_and_properties_one,
                                   self.selenium_methods_and_properties_two,
                                   self.selenium_methods_and_properties_three,
                                   self.selenium_methods_and_properties_four,
                                   self.selenium_methods_and_properties_five])

if __name__ == '__main__':
    test_suite = TestSuite()
    runner = HtmlTestRunner.HTMLTestRunner(output='test-suite-report.html')
    runner.run(test_suite.run_test_methods_and_properties_suite())
