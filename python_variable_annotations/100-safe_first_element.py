#!/usr/bin/env python3
""" Second challenge checing if its length """
from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """ Duck typing checking if its length """
    if lst:
        return lst[0]
    else:
        return None