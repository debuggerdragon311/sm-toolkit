from .errors import RangeError, ParseError

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _read_line(prompt: str) -> str:
    return input(prompt).strip()


def _check_range(value, lo, hi) -> None:
    if not (lo <= value <= hi):
        raise RangeError(value, lo, hi)


# ---------------------------------------------------------------------------
# public API
# ---------------------------------------------------------------------------

def get_int(prompt: str, lo: int, hi: int) -> int | None:
    """
    prompt the user for an integer in [lo, hi] (inclusive).
    loops until valid input is supplied.
    """
    while True:
        raw = _read_line(prompt)
        try:
            value = int(raw)
        except ValueError:
            print(ParseError(raw, "int"))
            continue
        try:
            _check_range(value, lo, hi)
        except RangeError as e:
            print(e)
            continue
        return value


def get_float(prompt: str, lo: float, hi: float) -> float | None:
    """
    prompt the user for a float in [lo, hi] (inclusive).
    loops until valid input is supplied.
    """
    while True:
        raw = _read_line(prompt)
        try:
            value = float(raw)
        except ValueError:
            print(ParseError(raw, "float"))
            continue
        try:
            _check_range(value, lo, hi)
        except RangeError as e:
            print(e)
            continue
        return value


def get_int_list(prompt: str, lo: int, hi: int) -> list[int] | None:
    """
    prompt the user for a space-separated list of integers,
    each in [lo, hi] (inclusive).
    loops until the entire list is valid.
    """
    while True:
        raw = _read_line(prompt)
        parts = raw.split()
        if not parts:
            print(ParseError(raw, "list[int]"))
            continue
        try:
            values = [int(p) for p in parts]
        except ValueError as exc:
            print(ParseError(str(exc), "int"))
            continue
        try:
            for v in values:
                _check_range(v, lo, hi)
        except RangeError as e:
            print(e)
            continue
        return values