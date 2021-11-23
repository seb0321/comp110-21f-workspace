"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730358517"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Intialize a new Simpy object."""
        self.values = values 

    def __str__(self) -> str:
        """String representation of a Simpy."""
        return f"Simpy({self.values})"

    def fill(self, value: float, times: int) -> None:
        """Fill our values array by mutating object called on."""
        self.values = []
        i: int = 0 
        while i < times: 
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in a range of values."""
        self.values = []
        assert step != 0.0

        if step > 0.0:
            next_value: float = start 
            while next_value < stop:
                self.values.append(next_value)
                next_value += step

        else:
            next_value: float = start 
            while next_value > stop:
                self.values.append(next_value)
                next_value += step

    def sum(self) -> float: 
        """Use sum function."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operate overload for addition."""
        result: Simpy = Simpy([])

        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)

        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0 
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result

    def __pow__(self, rhs: Union[float, int, Simpy]) -> Simpy:
        """Operate overload for multiplication."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float) or isinstance(rhs, int):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            i: int = 0 
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for equal."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                if self.values[i] == rhs:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for greater than."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                if self.values[i] > rhs:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloading the Subscription Notation."""
        if isinstance(rhs, int): 
            result = self.values[rhs]
            return result
        else:
            
            result = Simpy([])
            for i in range(len(self.values)):
                if rhs[i]: 
                    result.values.append(self.values[i]) 
            return result
