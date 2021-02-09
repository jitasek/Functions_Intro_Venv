#def is_palindrome(string):
#   return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.

    The function ignores whitespace, punctuation, and
    capitalisation in the sentence.

    :param sentence: The sentence to check.
    :return: True if the sentence is a palindrome, False otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    return string[::-1].casefold() == string.casefold()     # solution 1
#    return is_palindrome(string)       # Solution 2 (with lines 1+2)


word = input("Please enter a word to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))


# 1. Create a new function called palindrome_sentence
# 2. The fce should return True if the sentence is a palindrome, otherwise False
# 3. Exclude invalid characters: ignore spaces, punctuations etc - only interested
# in alphanumeric characters (check String Methods in documentation)
# 4. e.g. Was it a car, or a cat, I saw?


p = palindrome_sentence()