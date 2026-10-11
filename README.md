# Week 5 Python Assignment — Password Generator & Your Own Module

Two small programs that practise using Python's built-in modules and creating your own module to import.

## Files

- `password_generator.py` — uses `random` and `string` to build random passwords; makes one 8-character and one 12-character password.
- `helpers.py` — our own module with two functions: `tables_needed(people, seats)` rounds up with `math.ceil()`, and `welcome(name)` returns a greeting. The `if __name__ == "__main__":` block only runs when the file is run directly.
- `main.py` — imports `helpers` and prints the results of both functions.

## How to run

    python3 password_generator.py
    python3 helpers.py
    python3 main.py

## Expected output

`password_generator.py` (yours will differ — passwords are random):

    Password: zAi1lJ0z
    Length: 8
    Password: d04fiFjnrbEK
    Length: 12

`helpers.py` (run on its own):

    3

`main.py`:

    Welcome to PLP, Amina!
    8
    4

Notice that `3` does not appear when running `main.py` — that is the `if __name__ == "__main__":` line doing its job.

## Concepts used

- `import random` — random choice from a pool
- `import string` — `ascii_letters` and `digits`
- `import math` — `math.ceil()` to round up
- Functions with default parameters — `make_password(length=8)`
- Creating your own module — `helpers.py`
- Importing your module — `import helpers`
- The `if __name__ == "__main__":` guard

## Screenshots

- `screenshot_run1.png` — first run of `password_generator.py`
- `screenshot_run2.png` — second run, showing different passwords
- `screenshot_main.png` — `main.py` output
- `screenshot_helpers.png` — `helpers.py` output on its own

## Author

Zakariye Ali Mursal
PLP 2026