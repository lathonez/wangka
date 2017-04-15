# Written by Uyen Nguyen

import math

def run_wangka_program():
    print("Welcome to The Martu Wangka Numbers!")
    while True:
        number = int(input("Please enter a number: "))
        if(number > 9999999999999999):
            ans = input("Please enter a number smaller than 9999999999999999. Press Enter to continue.")
        else:
            print("The Martu Wangka says: " + get_wangka_number(number))

        ans = input("Would you like to try another number? (y/n) ")
        if ans == 'n':
            print("Thank you for learning The Martu Wangka Numbers!")
            break;

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

#Examples:
#1 kuja
#2 kujarra
#3 kujarra kuja
#4 kujarrakujarra
#5 marakuja - mara means hand/feet which has 5 fingers/toes, marakuja means 1 hand of 5
#6 marakuja kuja
#7 marakuja kujarra
#8 marakuja kujarra kuja
#9 marakuja kujarrakujarra
#10 marakujarra - it means 2 hands of 5
#11 marakujarra kuja
#12 marakujarra kujarra
#15 marakujarra kuja - instead of marakujarra marakuja because it's 3 hands of 5
#19 marakujarra kuja kujarrakujarra - instead of marakujarra marakuja kujarrakujarra because it's 15 and 4
