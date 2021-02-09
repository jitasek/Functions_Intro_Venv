def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers.

    Although this function is intended to multiply two numbers,
    you can also use it to multiply a sequence. If you pass
    a string, for example, as the first argument, you'll get
    the string repeated y times as the returned value.

    :param x: The first number to multiply.
    :param y: The number to multiply x with.
    :return: The product of x times y.
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool: # this = annotation - says that the fce takes a string as an argument and returns a bool
    """
    Check if the string is a palindrome.

    Palindrome is a string that reads the same forwards and backwards.
    :param string: The string to check.
    :return: True, if string is a palindrome, False otherwise.
    """
#    backwards = string[::-1]    # This reverses the original string
#    return backwards == string  # checks if the reverse string is the same as the original and gives True or False
    return string[::-1].casefold() == string.casefold()


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

# answer = multiply(10.5, 4)
# print(answer)
#
# forty_two = multiply(6, 7)
# print(forty_two)
#
# print()
#
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)

# NOTE: Functions are always separated from each other with TWO blank lines!

p = is_palindrome()