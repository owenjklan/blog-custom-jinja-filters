import unittest
from decimal import Decimal

from filters import monetary_value_filter


# Some Decimal objects representing various monetary values
WHOLE_DOLLARS_WITH_CENTS = Decimal("1.00")
WHOLE_DOLLARS_WITHOUT_CENTS = Decimal("1")
WHOLE_DOLLARS_WITH_4_DECIMAL_PLACES = Decimal("4.1234")

test_parameters = {
    "Two decimal places when provided two decimal places": {
        "input": WHOLE_DOLLARS_WITH_CENTS,
        "expected": "1.00",
    },
    "Two decimal places when provided no decimal places": {
        "input": WHOLE_DOLLARS_WITHOUT_CENTS,
        "expected": "1.00",
    },
    "Four decimal places when provided with four decimal places": {
        "input": WHOLE_DOLLARS_WITH_4_DECIMAL_PLACES,
        "expected": "4.1234",
    }
}

class MonetaryValueFilterTestCase(unittest.TestCase):
    def test_basic_filter_output(self):
        for test_name, parameters in test_parameters.items():
            print(f"Sub-test: {test_name}")
            with self.subTest(input_param=parameters["input"]):
                self.assertEqual(monetary_value_filter(parameters["input"]), parameters["expected"])


if __name__ == '__main__':
    unittest.main()
