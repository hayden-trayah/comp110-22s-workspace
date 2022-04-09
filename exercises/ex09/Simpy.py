"""Utility class for numerical operations."""

from __future__ import annotations


from typing import Union

__author__ = "730325581"


class Simpy:
    """Creates a simpy object and defines its methods."""
    values: list[float]

    def __init__(self, input_list: list[float]):
        """Constructs a Simpy object."""
        self.values = input_list
    
    def __str__(self) -> str:
        """Presents the values of a Simpy object as a str."""
        str(self.values)
        return f"Simpy({self.values})"

    def fill(self, value: float, factor: int) -> None:
        """Fills a Simpy's values with a specific number of repeating values."""
        self.values: list[float] = []
        i: int = factor
        while i > 0:
            self.values.append(value)
            i -= 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills the values attribute of Simpy objects with a range of values."""
        assert step != 0.0
        factors: list[float] = []
        new_factor: float = start
        factors.append(start)
        turns: float = ((stop - start) / step) - 1
        while turns > 0:
            new_factor += step
            factors.append(new_factor)
            turns -= 1
        
        for item in factors:
            self.values.append(item)
    
    def sum(self) -> float:
        """Sums the values in a Simpy object."""
        output: float = sum(self.values)
        return output

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Creates a new Simpy object and adds the rhs float or Simpy object."""
        output_list: list[float] = []
        i: int = 0
        if isinstance(rhs, float):
            for item in self.values:
                output_list.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for item in self.values:
                output_list.append(item + rhs.values[i])
                i += 1
        output = Simpy(output_list)
        return output

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponentiates the values in Simpy objects with another object or a factor."""
        output_list: list[float] = []
        i: int = 0
        if isinstance(rhs, float):
            for item in self.values:
                output_list.append(item ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for item in self.values:
                output_list.append(item ** rhs.values[i])
                i += 1
        output = Simpy(output_list)
        return output

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a list of bools that represents a mask of equalities between lists."""
        output_list: list[bool] = []
        i: int = 0
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    output_list.append(True)
                else:
                    output_list.append(False)
                i += 1
            i = 0
        else:
            for item in self.values:
                if item == rhs.values[i]:
                    output_list.append(True)
                else:
                    output_list.append(False)
                i += 1
            i = 0
        return output_list

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask (list[bool]) showing which items are greater or less than a value or corresponding set of values."""
        output_list: list[bool] = []
        i: int = 0
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    output_list.append(True)
                else:
                    output_list.append(False)
                i += 1
            i = 0
        else:
            for item in self.values:
                if item > rhs.values[i]:
                    output_list.append(True)
                else:
                    output_list.append(False)
                i += 1
            i = 0
        return output_list

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Makes Simpy objects work with the subscription operator."""
        if isinstance(rhs, int):
            output = self.values[rhs]
            return output
        else:
            output_list: list[float] = []
            i: int = 0
            for item in rhs:
                if item is True:
                    output_list.append(self.values[i])
                i += 1
        output = Simpy(output_list)
        return output