import unittest
from proj2 import *

class TestCSVFunctions(unittest.TestCase):

    # read_csv_lines tests
    def test_read_csv_lines_basic(self):
        data = read_csv_lines("sample.csv")
        self.assertIsNotNone(data)
        self.assertEqual(data.value.country, "USA")
        self.assertEqual(data.value.year, 2020)
        self.assertIsNotNone(data.next)
        self.assertEqual(data.next.value.country, "Canada")

    def test_read_csv_lines_missing_values(self):
        data = read_csv_lines("sample.csv")
        self.assertIsNone(data.value.electricity_and_heat_co2_emissions_per_capita)
        self.assertIsNone(data.value.total_co2_emissions_excluding_lucf_per_capita)
        self.assertIsNone(data.next.value.energy_co2_emissions_per_capita)



