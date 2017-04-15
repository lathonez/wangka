def run_wangka_program():

    print("Welcome to The Martu Wangka Numbers!")

    number = int(input("Please enter a number: "))

    print("The Martu Wangka says: " + get_wangka_number(number))

def get_wangka_number(number):

    mw_num = ""

    if number == 1:

        mw_num = "kuja"

    else:

        mw_num = "nope"

    return mw_num

run_wangka_program()
