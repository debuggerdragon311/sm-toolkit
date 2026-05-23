from .errors import UnknownOperationError

# ---------------------------------------------------------------------------
# renderers (private)
# ---------------------------------------------------------------------------

def _triangle(n: int, sym: str) -> None:
    for i in range(1, n + 1):
        print(sym * i)


def _reverse(n: int, sym: str) -> None:
    for i in range(n, 0, -1):
        print(sym * i)


def _diamond(n: int, sym: str) -> None:
    mid = n // 2 + 1
    for i in range(1, mid + 1):
        print((" " * (mid - i)) + (sym * (2 * i - 1)))
    for i in range(mid - 1, 0, -1):
        print((" " * (mid - i)) + (sym * (2 * i - 1)))


def _cube(n: int, sym: str) -> None:
    row = (sym + " ") * n
    for _ in range(n):
        print(row)


def _rectangle(n: int, sym: str, *, width: int) -> None:
    row = (sym + " ") * width
    for _ in range(n):
        print(row)


# ---------------------------------------------------------------------------
# dispatch table and public API
# ---------------------------------------------------------------------------

_PATTERNS: dict[str, callable] = {
    "triangle":  _triangle,
    "reverse":   _reverse,
    "diamond":   _diamond,
    "cube":      _cube,
}


def draw(name: str, n: int, sym: str = "*") -> None:
    """
    render a named ASCII pattern to stdout.

    name -- one of: triangle  reverse  diamond  cube
    n    -- size parameter (rows / side length)
    sym  -- character to draw with (default '*')

    raises UnknownOperationError for unrecognised name.
    """
    if name not in _PATTERNS:
        raise UnknownOperationError(name, valid=tuple(_PATTERNS))
    _PATTERNS[name](n, sym)


def rectangle(height: int, width: int, sym: str = "*") -> None:
    """
    render a filled height x width rectangle to stdout.
    separate from draw() because it takes two size parameters.
    """
    _rectangle(height, sym, width=width)