#!/usr/bin/env python3
""" Second challenge checing if its length """
from typing import Any, Sequence, Optional


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """ adding comment for testing """
    if lst:
        return lst[0]
    else:
        return None
