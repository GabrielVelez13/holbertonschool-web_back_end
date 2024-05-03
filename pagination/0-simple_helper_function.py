#!/usr/bin/env python3
""" Simple helper for pagination """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ Returns a tuple with the start and end of the current page """
    return (page_size*page - page_size, page_size*page)
