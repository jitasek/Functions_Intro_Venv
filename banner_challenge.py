def banner_text(text=" ", screen_width=80):    # added screen_width here in the function + deleted line 2
    # screen_width = 50                 # + I have to add a width (66) as the 2nd argument on each line
    if len(text) > screen_width - 4:    # but better = if I use a default argument instead (width=80 - without spaces around the equal sign)
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))
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
banner_text()
banner_text("When you're feeling in the dumps,", 80)    # This will get displayed in the same way as without the "80" when I run it
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look at the bright side of life...")
banner_text("*")

# Challenge:
# Modify the banner_text function so that it takes another argument, the width for the banner

# Default parameter value (default argument) - e.g. line 1 "screen_width=80" : if I don't specify
# the screen_width argument later in the code, we will automatically get the default value of 80

# I added one more default value - to the "text" parameter (text=" ") on line 1 -> I dont have to
# remember to use a space when I wanna include a blank line in the banner (line 19)