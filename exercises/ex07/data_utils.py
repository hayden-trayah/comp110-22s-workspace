"""Dictionary related utility functions."""

__author__ = "730325581"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    # If you want to know how to open a file in a programming language, google it.
    # Read that file

    # Prepare to read the data file as a csv rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Prooduce a list[str] of all values in a single column."""
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


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce the first N rows of a table."""
    result: dict[str, list[str]] = {}
    if N >= len(table):
        return table
    for header in table:
        result[header] = []
    i: int = 0
    while i < N:
        for header in table:
            result[header].append(table[header][i])
        i += 1
    return result


def select(table: dict[str, list[str]], colmuns: list[str]) -> dict[str, list[str]]:
    """Produce a new table only with the given columns."""
    result: dict[str, list[str]] = {}
    for header in colmuns:
        result[header] = table[header]
    return result
    

def concat(table: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine the columns of two tables."""
    result: dict[str, list[str]] = {}
    for header in table:
        result[header] = table[header]
    for header in table2:
        if header not in result.keys(): 
            result[header] = table2[header]
        else:
            result[header] += table2[header]
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """Outputs a dictionary with keys that are input list values and values indicating their frequency."""
    result: dict[str, int] = {}
    for item in input_list:
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1
    return result