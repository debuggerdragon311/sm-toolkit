def binary_search(seq: list[int], target: int, presorted: bool = False) -> bool:
    """
    return True if target exists in seq, False otherwise.

    presorted -- set True when seq is already sorted to skip the O(n log n)
                sort step.  default False (safe for unsorted input).

    note: does not mutate the original list.
    """
    work = seq if presorted else sorted(seq)
    lo, hi = 0, len(work) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if work[mid] == target:
            return True
        elif target < work[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return False


def linear_search(seq: list, target) -> int:
    """
    return the index of the first occurrence of target in seq.
    returns -1 if target is not found.
    works on any comparable element type.
    """
    for i, v in enumerate(seq):
        if v == target:
            return i
    return -1