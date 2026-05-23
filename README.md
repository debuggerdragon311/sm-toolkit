<div align="center">

  # ⚙️ SM-TOOLKIT

**A clean, zero-dependency Python utility library for arithmetic, search, arrays, patterns, and safe I/O.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen?style=flat-square)
![Dependencies](https://img.shields.io/badge/Dependencies-None-orange?style=flat-square)

Drop in a module. Call a function. Done.

No third-party packages. No configuration. No boilerplate. Just a tightly scoped set of utilities that handle the repetitive logic you'd otherwise rewrite in every project — with consistent error types, clear contracts, and zero surprises.

---
</div>

## What's Inside

Six modules, twenty-one functions, one coherent error hierarchy.

| Module | Functions | What it does |
|---|---|---|
| `arith` | `calc`, `factorial`, `fibo` | Named arithmetic operations + number sequences |
| `search` | `binary_search`, `linear_search` | Sorted and unsorted element lookup |
| `array` | `count_occurrences`, `predecessor`, `successor` | Frequency counting and neighbor retrieval |
| `pattern` | `draw`, `rectangle` | ASCII pattern rendering to stdout |
| `io` | `get_int`, `get_float`, `get_int_list` | Validated, looping terminal input |
| `errors` | 6 exception classes | Typed, structured exception hierarchy |

---

## Installation

No PyPI package yet. Clone and import directly.

```bash
git clone https://github.com/your-username/sm-toolkit.git
```

Place the cloned folder (as `sm_core/`) in your project root, or add it to your `PYTHONPATH`. Then import:

```python
import sm_core
# or selectively:
from sm_core import calc, binary_search, draw
```

> **Requirements:** Python 3.10 or above. No `pip install` needed — standard library only.

---

## Module Reference

### `arith` — Arithmetic

#### `calc(op, a, b) → float`

Dispatch a named binary operation. Cleaner than a chain of `if/elif` blocks when the operation is data-driven.

```python
from sm_core import calc

calc("add", 10, 3)   # → 13.0
calc("sub", 10, 3)   # → 7.0
calc("mul", 10, 3)   # → 30.0
calc("div", 10, 3)   # → 3.333...
calc("mod", 10, 3)   # → 1.0
calc("pow", 2, 8)    # → 256.0
```

| `op` key | Operation | Guards |
|---|---|---|
| `add` | a + b | — |
| `sub` | a − b | — |
| `mul` | a × b | — |
| `div` | a ÷ b | raises `DomainError` if b == 0 |
| `mod` | a % b | raises `DomainError` if b == 0 |
| `pow` | a ** b | — |

Raises `UnknownOperationError` for any key not in the table above.

---

#### `factorial(n) → int`

Iterative factorial. No recursion limit concerns.

```python
from sm_core import factorial

factorial(0)   # → 1
factorial(5)   # → 120
factorial(12)  # → 479001600
```

Raises `DomainError` for `n < 0`.

---

#### `fibo(n) → list[int]`

Return the first `n` numbers of the Fibonacci sequence.

```python
from sm_core import fibo

fibo(1)   # → [0]
fibo(5)   # → [0, 1, 1, 2, 3]
fibo(8)   # → [0, 1, 1, 2, 3, 5, 8, 13]
```

Raises `DomainError` for `n < 1`.

---

### `search` — Search Algorithms

#### `binary_search(seq, target, presorted=False) → bool`

O(log n) existence check. Does not mutate the input list.

```python
from sm_core import binary_search

binary_search([3, 1, 4, 1, 5, 9], 4)             # → True  (sorts internally)
binary_search([1, 2, 3, 4, 5], 6, presorted=True) # → False (skips sort step)
```

Set `presorted=True` when your list is already sorted to avoid the internal `sorted()` call.

---

#### `linear_search(seq, target) → int`

Return the index of the first match, or `-1` if absent. Works on any comparable type.

```python
from sm_core import linear_search

linear_search([10, 20, 30, 20], 20)    # → 1
linear_search(["a", "b", "c"], "d")   # → -1
```

---

### `array` — Array Utilities

> All three functions expect a **sorted ascending** list. Pass `sorted(your_list)` if unsorted.

#### `count_occurrences(seq, target) → int`

Binary lower/upper bound scan — O(log n). Returns `0` when the target is absent; never raises.

```python
from sm_core import count_occurrences

count_occurrences([1, 2, 2, 3, 4, 4, 4], 4)   # → 3
count_occurrences([1, 2, 3], 9)                # → 0
```

---

#### `predecessor(seq, target) → int`

Return the element immediately before the first occurrence of `target`.

```python
from sm_core import predecessor

predecessor([1, 2, 3, 4], 3)   # → 2
```

| Condition | Raises |
|---|---|
| `target` not in `seq` | `NotFoundError` |
| `target` is the first element | `IndexError` |

---

#### `successor(seq, target) → int`

Return the element immediately after the **last** occurrence of `target`.

```python
from sm_core import successor

successor([1, 2, 2, 3], 2)   # → 3
```

| Condition | Raises |
|---|---|
| `target` not in `seq` | `NotFoundError` |
| `target` is the last element | `IndexError` |

---

### `pattern` — ASCII Pattern Drawing

#### `draw(name, n, sym="*") → None`

Render a named ASCII pattern to stdout.

```python
from sm_core import draw

draw("triangle", 4, "#")
# #
# ##
# ###
# ####

draw("reverse", 4, "#")
# ####
# ###
# ##
# #

draw("diamond", 5, "*")
#   *
#  ***
# *****
#  ***
#   *

draw("cube", 3, "O")
# O O O
# O O O
# O O O
```

| `name` | Shape | `n` controls |
|---|---|---|
| `triangle` | Left-aligned growing rows | number of rows |
| `reverse` | Left-aligned shrinking rows | number of rows |
| `diamond` | Centred diamond | half-height |
| `cube` | n × n filled square | side length |

Raises `UnknownOperationError` for unrecognised names.

---

#### `rectangle(height, width, sym="*") → None`

Render a filled rectangle — separate from `draw()` because it takes two size parameters.

```python
from sm_core import rectangle

rectangle(3, 5, "-")
# - - - - -
# - - - - -
# - - - - -
```

---

### `io` — Validated Terminal Input

All three functions loop indefinitely until the user provides valid input. Errors are printed inline — no exceptions propagate to the caller.

#### `get_int(prompt, lo, hi) → int`

```python
from sm_core import get_int

age = get_int("Enter your age: ", 1, 120)
```

#### `get_float(prompt, lo, hi) → float`

```python
from sm_core import get_float

temp = get_float("Temperature (−50 to 60 °C): ", -50.0, 60.0)
```

#### `get_int_list(prompt, lo, hi) → list[int]`

Accepts a space-separated line. Every token must parse as `int` and fall within `[lo, hi]`.

```python
from sm_core import get_int_list

scores = get_int_list("Enter scores (0–100): ", 0, 100)
# input: "85 90 72 68"
# → [85, 90, 72, 68]
```

---

### `errors` — Exception Hierarchy

All toolkit exceptions inherit from `ToolkitError`, making it easy to catch the whole family or individual types.

```
ToolkitError
├── RangeError            value outside permitted [lo, hi]
├── ParseError            raw string could not be parsed
├── DomainError           argument violates a math/logical precondition
├── UnknownOperationError unrecognised operation key
└── NotFoundError         target element absent from sequence
```

Every class exposes its constructor arguments as instance attributes for programmatic inspection:

```python
from sm_core.errors import RangeError, UnknownOperationError

try:
    raise RangeError(150, 0, 100)
except RangeError as e:
    print(e.value, e.lo, e.hi)   # 150  0  100

try:
    raise UnknownOperationError("xor", valid=("add", "sub"))
except UnknownOperationError as e:
    print(e.op, e.valid)         # xor  ('add', 'sub')
```

---

## Complete Examples

### Example 1 — Array neighbour lookup

```python
# example01a.py
from sm_core import count_occurrences, predecessor

arr = [1, 0, 5, 4, 4]

print(predecessor(arr, 0))                    # → 1
print(count_occurrences(sorted(arr), 4))      # → 2
```

### Example 2 — Factorial

```python
# example02b.py
from sm_core import factorial

print(factorial(5))   # → 120
```

### Example 3 — Pattern drawing

```python
# example03c.py
from sm_core import draw

draw("triangle", 5, "#")
draw("reverse",  4, "#")
```

### Example 4 — Safe arithmetic with validated input

```python
# example04d.py
import sm_core

x = sm_core.get_int("Enter 1st number: ", 1, 100)
y = sm_core.get_int("Enter 2nd number: ", 1, 100)

print(sm_core.calc("add", float(x), float(y)))
```

---

## Running the Tests

```bash
python -m unittest check_array_utils.py -v
```

Expected output:

```
test_array_utils (check_array_utils.MyTestCase) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

---

## Project Structure

```
sm-toolkit/
├── sm_core/
│   ├── __init__.py          # Public API surface — all exports declared here
│   ├── arith.py             # calc · factorial · fibo
│   ├── search.py            # binary_search · linear_search
│   ├── array.py             # count_occurrences · predecessor · successor
│   ├── pattern.py           # draw · rectangle
│   ├── io.py                # get_int · get_float · get_int_list
│   └── errors.py            # ToolkitError and all subclasses
│
├──tests/
│   └── check_array_utils.py     # unittest suite for array module
└── examples/
    ├── example01a.py            # Array neighbour demo
    ├── example02b.py            # Factorial demo
    ├── example03c.py            # Pattern rendering demo
    └── example04d.py            # Validated input + arithmetic demo
```

---

## Design Decisions

**Why a named-operation dispatch table instead of separate `add()`, `sub()` functions?**
`calc("add", x, y)` composes cleanly when the operation itself is a variable — menus, config files, user input. Individual function names don't.

**Why does `binary_search` sort internally by default?**
Silent data corruption from assuming a list is sorted when it isn't is worse than a one-time O(n log n) cost. The `presorted=True` flag gives you the speed when you know the input is clean.

**Why do `predecessor` / `successor` use a linear scan instead of binary search?**
The functions are intentionally sequence-order aware, not value-sorted — `predecessor([5, 1, 3], 1)` returns `5` (the element before in list position). Binary search on unsorted data would give wrong answers.

**Why do the `io` functions loop instead of raising on bad input?**
They model interactive terminal sessions where the user is expected to retry. Exceptions are the right tool when the caller decides retry logic — looping is the right tool when the user does.

---
> [!WARNING]
> I had build this library while learning python years ago. It was my way of learning. Keep in mind I might not able to maintain it frequently. It was part of a fun learning for me.

## License

MIT — see `LICENSE`.

---

## Author

<div align="center">

**Soumyajit Bala**

*Systems engineer. I build automation infrastructure, AI pipelines, and local-first tools.*

[![Email](https://img.shields.io/badge/Email-soumyajit@zelkyr.dev-333?style=for-the-badge&logo=gmail&logoColor=white)](mailto:soumyajit@zelkyr.dev)
[![GitHub](https://img.shields.io/badge/GitHub-debuggerdragon311-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/debuggerdragon311)

**Need a custom automation pipeline, AI integration, or data extraction system built?**
Reach out at [soumyajit@zelkyr.dev](mailto:soumyajit@zelkyr.dev) <<

</div>

---

<div align="center">
  <sub>For beginners use only.</sub>
</div>
