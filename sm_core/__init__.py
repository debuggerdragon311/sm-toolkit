# sm-toolkit --> personal utility library

# meta-data
__version__   = "0.1.0"
__author__    = "Soumyajit Bala"
__email__     = "soumyajit@zelkyr.dev"
__license__   = "MIT"
__description__ = "A zero-dependency Python utility library for arithmetic, search, arrays, patterns and I/O."

from .arith   import calc, factorial, fibo
from .search  import binary_search, linear_search
from .array   import count_occurrences, predecessor, successor
from .pattern import draw, rectangle
from .io      import get_int, get_float, get_int_list
from .errors  import (
    ToolkitError,
    RangeError,
    ParseError,
    DomainError,
    UnknownOperationError,
    NotFoundError,
)

__all__ = [
    # arithmetic
    "calc",
    "factorial",
    "fibo",

    # search
    "binary_search",
    "linear_search",

    # array
    "count_occurrences",
    "predecessor",
    "successor",

    # pattern
    "draw",
    "rectangle",

    # io
    "get_int",
    "get_float",
    "get_int_list",

    # errors
    "ToolkitError",
    "RangeError",
    "ParseError",
    "DomainError",
    "UnknownOperationError",
    "NotFoundError",
]
