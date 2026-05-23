from .errors import NotFoundError


def count_occurrences(seq: list[int], target: int) -> int:
    """
    return the number of times target appears in seq.

    seq must be sorted ascending; uses two binary scans (O(log n)).
    returns 0 when target is absent (no exception).
    """
    lo = _lower_bound(seq, target)
    if lo == len(seq) or seq[lo] != target:
        return 0
    hi = _upper_bound(seq, target)
    return hi - lo


def predecessor(seq: list[int], target: int) -> int:
    """
    return the element immediately before the first occurrence of target in seq.

    raises NotFoundError if target is not present.
    raises IndexError if target is the first element (no predecessor exists).
    """
    for i, v in enumerate(seq):
        if v == target:
            if i == 0:
                raise IndexError(f"{target} is the first element -- no predecessor")
            return seq[i - 1]
    raise NotFoundError(target)


def successor(seq: list[int], target: int) -> int:
    """
    return the element immediately after the last occurrence of target in seq.

    raises NotFoundError if target is not present.
    raises IndexError if target is the last element (no successor exists).
    """
    last = -1
    for i, v in enumerate(seq):
        if v == target:
            last = i
    if last == -1:
        raise NotFoundError(target)
    if last == len(seq) - 1:
        raise IndexError(f"{target} is the last element -- no successor")
    return seq[last + 1]


# ---------------------------------------------------------------------------
# internal helpers
# ---------------------------------------------------------------------------

def _lower_bound(seq: list[int], target: int) -> int:
    """return leftmost index where seq[i] >= target."""
    lo, hi = 0, len(seq)
    while lo < hi:
        mid = (lo + hi) // 2
        if seq[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def _upper_bound(seq: list[int], target: int) -> int:
    """return leftmost index where seq[i] > target."""
    lo, hi = 0, len(seq)
    while lo < hi:
        mid = (lo + hi) // 2
        if seq[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo