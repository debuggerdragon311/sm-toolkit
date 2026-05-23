class ToolkitError(Exception):
    """base class for all toolkit exceptions."""


class RangeError(ToolkitError):
    """value falls outside the permitted [lo, hi] range."""

    def __init__(self, value, lo, hi):
        self.value = value
        self.lo    = lo
        self.hi    = hi
        super().__init__(f"{value} out of range [{lo}, {hi}]")


class ParseError(ToolkitError):
    """raw input could not be parsed to the expected type."""

    def __init__(self, raw: str, expected: str):
        self.raw      = raw
        self.expected = expected
        super().__init__(f"cannot parse {raw!r} as {expected}")


class DomainError(ToolkitError):
    """argument violates a mathematical or logical precondition."""

    def __init__(self, msg: str):
        super().__init__(msg)


class UnknownOperationError(ToolkitError):
    """an unrecognised operation key was requested."""

    def __init__(self, op: str, valid: tuple[str, ...] = ()):
        self.op    = op
        self.valid = valid
        hint = f"  valid: {', '.join(valid)}" if valid else ""
        super().__init__(f"unknown operation: {op!r}{hint}")


class NotFoundError(ToolkitError):
    """target element does not exist in the sequence."""

    def __init__(self, target):
        self.target = target
        super().__init__(f"element not found: {target!r}")