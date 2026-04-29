import csv
import math
import sys
import unittest
from dataclasses import dataclass
from typing import *

sys.setrecursionlimit(10_000)


# Task 1
# Row class for storing one line of emissions data
@dataclass(frozen=True)
class Row:
  country: str
  year: int
  electricity_and_heat_co2_emissions: float | None
  electricity_and_heat_co2_emissions_per_capita: float | None
  energy_co2_emissions: float | None
  energy_co2_emissions_per_capita: float | None
  total_co2_emissions_excluding_lucf: float | None
  total_co2_emissions_excluding_lucf_per_capita: float | None
# Node class for storing a value of a row of data and a next pointer
@dataclass(frozen=True)
class Node:
  value: Row
  next: Node | None
# Task 2
# parse_row(fields: list[str]) -> Row: Function takes in a list of strings representing a CSV row and returns a Row object,
# converting numeric values to int or float and replacing empty strings with None.
def parse_row(fields: list[str]) -> Row:
  return Row(
        country=fields[0],
        year=int(fields[1]),
        electricity_and_heat_co2_emissions=None if fields[2] == "" else float(fields[2]),
        electricity_and_heat_co2_emissions_per_capita=None if fields[3] == "" else float(fields[3]),
        energy_co2_emissions=None if fields[4] == "" else float(fields[4]),
        energy_co2_emissions_per_capita=None if fields[5] == "" else float(fields[5]),
        total_co2_emissions_excluding_lucf=None if fields[6] == "" else float(fields[6]),
        total_co2_emissions_excluding_lucf_per_capita=None if fields[7] == "" else float(fields[7])
    )
# def read_csv_rows(rows: list[list[str]], index: int) -> Node | None: Function takes in a list of CSV rows and an index and returns 
# a linked list of Node objects, recursively processing rows starting from the given index, or None if no rows remain.
def read_csv_rows(rows: list[list[str]], index: int) -> Node | None:
  if index >= len(rows):
    return None
  row = parse_row(rows[index])
  return Node(row, read_csv_rows(rows, index + 1))
# read_csv_lines(filename: str) -> Optional[Node] :Function takes in a filename and returns a linked list of Node objects representing the CSV data
def read_csv_lines(filename: str) -> Optional[Node]:
  expected_header = [
        "country",
        "year",
        "electricity_and_heat_co2_emissions",
        "electricity_and_heat_co2_emissions_per_capita",
        "energy_co2_emissions",
        "energy_co2_emissions_per_capita",
        "total_co2_emissions_excluding_lucf",
        "total_co2_emissions_excluding_lucf_per_capita"
    ]
  with open(filename, newline="") as csvfile:
      reader = csv.reader(csvfile)
      rows = list(reader)
  if rows[0] != expected_header:
      raise ValueError("unexpected first line: got {}".format(rows[0]))
  return read_csv_rows(rows, 1)

# Task 3
# listlen(data: Optional[Node]) -> int: Function returns the number of rows within the linked list.
def listlen(data: Optional[Node]) -> int:
  if data is None:
    return 0
  return 1 + listlen(data.next)

# Task 4
# filter_rows: Function takes in a linked list of rows, a field name, a comparison string, and a value, and returns a new linked list 
# containing only the rows that fit the filter.
def filter_rows(
    data: Optional[Node],
    field_name: str,
    comparison: str,
    value: Union[str, float, int]
) -> Optional[Node]:
      if data is None:
        return None
    filtered_rest = filter_rows(data.next, field_name, comparison, value)
    row = data.value
    if field_name == "country":
        field_value = row.country
    elif field_name == "year":
        field_value = row.year
    elif field_name == "electricity_and_heat_co2_emissions":
        field_value = row.electricity_and_heat_co2_emissions
    elif field_name == "electricity_and_heat_co2_emissions_per_capita":
        field_value = row.electricity_and_heat_co2_emissions_per_capita
    elif field_name == "energy_co2_emissions":
        field_value = row.energy_co2_emissions
    elif field_name == "energy_co2_emissions_per_capita":
        field_value = row.energy_co2_emissions_per_capita
    elif field_name == "total_co2_emissions_excluding_lucf":
        field_value = row.total_co2_emissions_excluding_lucf
    elif field_name == "total_co2_emissions_excluding_lucf_per_capita":
        field_value = row.total_co2_emissions_excluding_lucf_per_capita
    else:
        return filtered_rest  # unknown field → skip

    if field_value is None:
        return filtered_rest
    if field_name == "country":
        if comparison == "equal" and field_value == value:
            return Node(row, filtered_rest)
        return filtered_rest
    if comparison == "less_than" and field_value < value:
        return Node(row, filtered_rest)
    if comparison == "greater_than" and field_value > value:
        return Node(row, filtered_rest)
    if comparison == "equal" and field_value == value:
        return Node(row, filtered_rest)
    return filtered_rest
  

  
















