#!/usr/bin/env python3
""" A staticly typed function that squared two numbers """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Squares a number but it is callable """
    def multiply(x: float) -> float:
        return multiplier * x
    return multiply
