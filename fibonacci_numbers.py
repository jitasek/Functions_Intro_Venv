def fibonacci(n: int) -> int:   # function annotation (if you dont use it, then you should include the types in the Docstring instead)
    """Return the `n` th Fibonacci number for positive `n`."""
    if 0 <= n <= 1:     # This says that if n=0, return 0, if n=1, return 1
        return n

    n_minus1, n_minus2 = 1, 0   # stores the first 2 numbers in variables (if we don't return above, we need to add up 2 numbers to get the 3rd)

    result = None
    for f in range(n - 1):      # this is just a loop that ads up the last 2 values and produces the next result
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

# EXPLANATION (to lines 8-12):
# Because of how the range in the loop is defined,
# negative values of n will cause the range to be empty, and this will mean that
# result never gets defined. The function then tries to return result despite it
# not being defined, and that causes the error. Defining result before the loop
# means that the function will never try to return result when it doesn't exist.
