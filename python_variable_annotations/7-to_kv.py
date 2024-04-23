#!/usr/bin/env python3
""" Stacticly typed tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple with a string an a squared value """
    return (k, v*v)
