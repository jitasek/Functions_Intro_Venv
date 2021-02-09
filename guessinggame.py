import random


def get_integer(prompt):    # this fce will get input from the user and return an integer value
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that the user will see, when they're
        prompted to enter a value.
    :return: The integer that the user enters.
    """
    while True:     # It's gonna keep looping until they enter a valid input (integer)
        temp = input(prompt) # we need to get their input + check if it can be converted into a number:
        if temp.isnumeric():
            return int(temp)
        else:   # This else is not needed, i can simply use only the following line (10) indented one level back
            print("{0} is not a valid number".format(temp))


help(get_integer) # This also prints the docstring for the object in parentheses (same result as the following 4 lines)

# print(input.__doc__) # We aren't calling the fce names here, only referring their attributes -> no parentheses therefore
# print("*" * 80)
# print(get_integer.__doc__) # These lines (25-28) only print the docstrings - not often used feature :)
# print("*" * 80)

highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: remove after testing
guess = 0   # initialize to any number that doesn't equal the answer

print("Please guess number between 1 a {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        if guess > answer:
            print("Please guess lower")

# NOTE: cmd + J = pops up documentation to specific Python objects (e.g. stand on "input" on line 6 and press Ctrl + J)
#       by holding cmd and clicking on a Python object (e.g. "input") you are taken to its source code = docstring (= the content btw the two """)
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else: # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
#
