#!/usr/bin/env python3
""" Third challenge checking if it is length """
from typing import Mapping, Union, Any, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, type(None)] = None) -> Union[Any, T]:
    """ Using typevar Checking if it is length """
    if key in dct:
        return dct[key]
    else:
        return default
