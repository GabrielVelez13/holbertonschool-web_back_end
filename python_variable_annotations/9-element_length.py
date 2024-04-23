#!/usr/bin/env python3
""" Annotate a function challenge """
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Challenge annotation """
    return [(i, len(i)) for i in lst]
