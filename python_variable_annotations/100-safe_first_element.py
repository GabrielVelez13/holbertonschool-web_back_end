#!/usr/bin/env python3
""" Second challenge """
from typing import Any, Sequence, Optional, List


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst is List:
        return lst[0]
    else:
        return None
