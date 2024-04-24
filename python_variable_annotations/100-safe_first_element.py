#!/usr/bin/python3
""" Second challenge """
from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """ Use correct duct-typed annotations """
    if lst:
        return lst[0]
    else:
        return None
