# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    if array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(n, m):
    if n == 0 and m == 0:
        return 1

    count = 1 if n % 10 == m % 10 else 0

    if n < 10 or m < 10:
        return count

    return count + digit_match(n // 10, m // 10)
