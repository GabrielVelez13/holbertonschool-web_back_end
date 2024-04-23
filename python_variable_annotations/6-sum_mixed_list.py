#!/usr/bin/env python3
""" Staticly typed mixed list sum fucntion """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sums a mixed list """
    num: float = 0
    for i in mxd_lst:
        num += i
    return float(num)
