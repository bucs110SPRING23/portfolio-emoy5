def percentage_to_letter(percent=99):
    """ Called a docstring - different from a comment
    This is a function that returns a letter grade based on a percentage
    args: percent (int)
    return: letter (str)
    """
    let = "A"
    if 80 <= percent < 90:
        let = "B"
    elif 70 <= percent < 80:
        let = "C"
    elif 60 <= percent < 70:
        let = "D"
    elif percent < 60:
        let = "F"
    return let
    
def is_passing(letter): #boolean functions bc they return booleans, is_ *convention
    """ 
    This is a function that returns a letter grade based on a percentage
    args: percent (int)
    return: letter (str)
    """
    return letter.lower() in "abc" # "in" is a boolean operator by def so this whole function will return either a true or a false

def main():
    #no docstring needed 
    grades = [90, 80, 70, 60, 50]
    for grade in grades:
        letter = percentage_to_letter(grade)
        if is_passing(letter):
            print("You passed")
        else:
            print("Someone messed up you grades")

main()
print(is_passing.__doc__)