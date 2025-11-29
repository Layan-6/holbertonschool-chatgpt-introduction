# Factorial Code Debugging

## Problem
The original code had two main issues:
1. Indentation problem
2. Infinite loop due to not decrementing `n`

## Errors Fixed

### Error 1: Indentation
- The line `result *= n` was not properly inside the `while` loop
- Fixed by adding proper indentation

### Error 2: Infinite Loop
- Added `n -= 1` line inside the loop to decrement `n` in each iteration

## Original Code (with errors)
```python
def factorial(n):
    result = 1
    while n > 1:
    result *= n
    return result
