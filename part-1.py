# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    if n == 0 or n == 1:
        return 1

    result = n * factorial(n - 1)
    return result


# reverse
def reverse(text):
    if len(text) <= 1:
        return text

    result = text[-1] + reverse(text[:-1])
    return result


# bunny
def bunny(count):
    if count < 0:
        raise ValueError("The count of bunny should not be negative.")
    if count == 0:
        return 0

    count = 2 + bunny(count - 1)
    return count


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    if parens[0] != "(" or parens[-1] != ")":
        return False
    result = is_nested_parens(parens[1:-1])
    return result
