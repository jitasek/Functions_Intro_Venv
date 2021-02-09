def banner_text(text: str = " ", screen_width: int = 80) -> None: # spaces around "=" needed if I add annotation
    #screen_width = 50   # I decreased the size from 80 to 50:
    """
    Print a string centred with ** either side.
    :param text: The string to print.
    An asterisk (*) will result in a row of asterisks.
    The default will print a blank line with a ** border at
    the left and right edges.
    :param screen_width: The overall width to print within
    (including the 4 spaces for the ** either side).
    :raises ValueError: if the supplied string is too long to fit.
    """
    if len(text) > screen_width - 4:
        #print("EEK!!")
        #print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
        raise ValueError("String {0} is larger than specified width {1}"    # raise = raises exception
                         .format(text, screen_width))   # This makes the program scrash - not ideal, but
# definitely better then e.g.burning someone's foot with a laser :) + programmer is aware s/he made a mistake
    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(" ")
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look at the bright side of life...")
banner_text("*")


# result = banner_text("Nothing is returned")
# print(result)

# This fce does printing and formating of the text. Doesn't return any value, only performs an action. Therefore
# the 'return' is not needed here (would print None - see if you activate lines 28, 29)

# NOTE: annotations:
# If you annotate any part of a function definition, you should annotate all of it. Either all parameters and the
# return value should be annotated or nothing