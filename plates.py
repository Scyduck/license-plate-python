def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # check if 1st two characters are alphabet
    for c in plate[0:2]:
        if c.isalpha() == True:
            checkaltwo = True
        else:
            checkaltwo = False

    # check plate length for 2 < len < 6
    length = len(plate)
    if length <= 6 and length >= 2:
        checklen = True
    else:
        checklen = False

    # check for no numbers in middle of plate; must end in numbers

    num = length - 2
    for c in plate[-num:]:
        if c.isdigit() and int(c) != 0:
            num -= 1
            if plate[-num:].isdigit():
                checkendnum = True
                break
            else:
                checkendnum = False
        elif c.isdigit() and int(c) == 0:
            checkendnum = False
            break
        else:
            checkendnum = True

    #check for first number being zero


    # no punctuation allowed
    if plate.isalnum() == True:
        punc = True
    else:
        punc = False

    if checkaltwo and checklen and checkendnum and punc:
        return True
    else:
        return False

main()
