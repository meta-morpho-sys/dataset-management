import unittest
import pandas as pd

from helpers import convert_to_numeric


# Assuming the latest version of convert_to_numeric is defined as previously

class TestConvertToNumeric(unittest.TestCase):
    def test_negative_with_parentheses(self):
        self.assertEqual(convert_to_numeric('(1,000)'), -1000.0)

    def test_positive_with_commas(self):
        self.assertEqual(convert_to_numeric('1,000'), 1000.0)

    def test_string_not_numeric(self):
        self.assertTrue(pd.isna(convert_to_numeric('not a number')))

    def test_integer_value(self):
        self.assertEqual(convert_to_numeric(1000), 1000)

    def test_float_value(self):
        self.assertEqual(convert_to_numeric(123.45), 123.45)

    def test_negative_integer_string(self):
        self.assertEqual(convert_to_numeric('-123'), -123.0)

    def test_string_with_text_and_numbers(self):
        self.assertTrue(pd.isna(convert_to_numeric('123abc')))

    def test_negative_number_without_parentheses(self):
        self.assertEqual(convert_to_numeric('-500'), -500.0)

    def test_positive_number_string(self):
        self.assertEqual(convert_to_numeric('500'), 500.0)

    def test_negative_float_string(self):
        self.assertEqual(convert_to_numeric('-123.45'), -123.45)

    def test_positive_float_string_with_commas(self):
        self.assertEqual(convert_to_numeric('1,234.56'), 1234.56)

    def test_negative_float_string_with_commas_and_parentheses(self):
        self.assertEqual(convert_to_numeric('(1,234.56)'), -1234.56)

if __name__ == '__main__':
    unittest.main()
