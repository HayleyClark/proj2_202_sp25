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

 # listlen tests
    def test_listlen_empty(self):
        self.assertEqual(listlen(None), 0)

    def test_listlen_one_node(self):
        row = Row("USA", 2020, 5000.0, None, 3000.0, 9.5, 8000.0, None)
        data = Node(row, None)
        self.assertEqual(listlen(data), 1)

    def test_listlen_multiple_nodes(self):
        row1 = Row("USA", 2020, 5000.0, None, 3000.0, 9.5, 8000.0, None)
        row2 = Row("Canada", 2019, 4000.0, 10.0, 2500.0, None, 7000.0, 8.0)
        data = Node(row1, Node(row2, None))
        self.assertEqual(listlen(data), 2)



