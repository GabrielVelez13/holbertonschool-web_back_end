#!/usr/bin/env python3
""" Second challenge checing if its length """
from typing import Optional, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """ adding comment for testing """
    if lst:
        return lst[0]
    else:
        return None
