import math

def run_wangka_program():

    print("Welcome to The Martu Wangka Numbers!")

    number = int(input("Please enter a number: "))

    print("The Martu Wangka says: " + get_wangka_number(number))

def get_wangka_number(number):

    mw_num = ""

    if number == 1:

        mw_num = "kuja"

    elif number == 2:

        mw_num = get_wangka_number(1) + "rra"

    elif number == 3:

        mw_num = get_wangka_number(2) + " " + get_wangka_number(1)

    elif number == 4:

        mw_num = get_wangka_number(2) + get_wangka_number(2)

    elif number >= 5:

        floor_quotient = math.floor(number / 5)

        remainder = number % (floor_quotient * 5)

        mw_num = "mara" + get_wangka_number(floor_quotient) + " " + get_wangka_number(remainder)

    else:

        mw_num = ""

    return mw_num.strip()

run_wangka_program()
