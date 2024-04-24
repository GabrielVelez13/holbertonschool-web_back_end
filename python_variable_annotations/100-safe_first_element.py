#!/usr/bin/env python3
""" Second challenge """
from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst is list:
        return lst[0]
    else:
        return None
