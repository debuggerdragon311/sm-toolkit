from .errors import DomainError, UnknownOperationError

# ---------------------------------------------------------------------------
# binary dispatch table
# ---------------------------------------------------------------------------

_OPS: dict[str, callable] = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
    "mod": lambda a, b: a % b,
    "pow": lambda a, b: a ** b,
}

_ZERO_GUARD = frozenset({"div", "mod"})


def calc(op: str, a: float, b: float) -> float:
    """
    apply a named binary arithmetic operation to a and b.

    op     -- one of: add sub mul div mod pow
    raises UnknownOperationError for unrecognised op.
    raises DomainError on division/modulo by zero.
    """
    if op not in _OPS:
        raise UnknownOperationError(op, valid=tuple(_OPS))
    if op in _ZERO_GUARD and b == 0:
        raise DomainError(f"{op} by zero is undefined")
    return _OPS[op](a, b)


# ---------------------------------------------------------------------------
# sequences
# ---------------------------------------------------------------------------

def factorial(n: int) -> int:
    """
    compute n! iteratively.
    raises DomainError for n < 0.
    """
    if n < 0:
        raise DomainError(f"factorial undefined for negative n={n}")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibo(n: int) -> list[int]:
    """
    return the first n numbers of the fibonacci sequence.
    fibo(1) -> [0]
    fibo(2) -> [0, 1]
    raises DomainError for n < 1.
    """
    if n < 1:
        raise DomainError(f"fibo requires n >= 1, got {n}")
    if n == 1:
        return [0]
    a, b = 0, 1
    seq  = [a, b]
    for _ in range(n - 2):
        a, b = b, a + b
        seq.append(b)
    return seq