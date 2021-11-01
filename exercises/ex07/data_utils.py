"""Utility functions!"""

__author__ = "730358517"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """""Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based with only N rows"""
    result: dict[str, list[str]] = {}
    curr_list: list[str] = []
    for col in table.keys():
        for i in range(0, n + 1):
            curr_list.append(table[col][i])
        result[col] = curr_list
       
    return result 


def select(table: dict[str, list[str]], subset: list[str]) -> dict[str, list[str]]:
    """Produce a column-based table with only specific columns."""
    result: dict[str, list[str]] = {}
    for i in subset:
        result[i] = table[i]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for i in table1:
        result[i] = table1[i]
    for i in table2: 
        result[i] = table2[i]
    return result 


def count(table: list[str]) -> dict[str, int]: 
    """List that will produce a dict."""
    result: dict[str, int] = {}
    for i in table: 
        result[i] = 0
    for i in table:
        result[i] = result[i] + 1
    return result