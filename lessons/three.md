## Lesson Objectives

* [Get User Input](#get-user-input)
* [Next Lesson](#next-lesson)
* [Diff](https://github.com/lathonez/wangka/compare/lesson-three...lesson-four)

## New concepts being addressed

* Variable
* Variable Assignment
* Conditional Statements (IF)
* Integer
* Function Parameter
* String Concatenation
* Value Comparison (using double equal)
* Return Statements
* Input Python Function
* Int Python Function

## Get User Input

Add the following code to our `wangka.py` file. As discussed in the previous lesson, indentation is very important!

```python
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
```

Ask the students to identify the start and end of each function declaration and which one is function call, which one is function declaration.

Here is a list of function calls:
* print("")
* input("")
* int()
* get_wangka_number(number)
* run_wangka_program()
* where: print, input and int functions are already declared in Python

Here is a list of function declarations:
* def run_wangka_program():
* def get_wangka_number(number):

Ask them to run and play with the program for a minute or two. Run the program, enter 1, should show "The Martu Wangka says: kuja" and enter any other number should show "The Martu Wangka says: nope”. Even though there are a few new concepts introduced in the code above, ask the students go through line by line and give a guess what each line may mean or do, based on their observations after running it.

`number = int(input("Please enter a number: "))` will get the user input, convert it to an integer and assign it into a variable “number”. Explain carefully each part inside the parenthesises and their priority in term of execution.

`def get_wangka_number(number)` passes in the user input number and use if-else condition to check for the number and return the wangka language of that number. Make sure every line of code under each if-else condition is indented properly since Python defined a block of code using indentation.

Explain how the variable number is passed into `get_wangka_number` in this line of code: `print(“The Martu Wangka says: " + get_wangka_number(number))` and then how it is used inside get_wangka_number.

Explain the difference between double equal `==` (for comparison) and single equal `=` (for variable assignment).

Since `get_wangka_number` function returns a value (`mw_num`). Show students how this value is returned back to where it is called, that is on line `print("The Martu Wangka says: " + get_wangka_number(number)).`

Ask the students to give an input number and use the whiteboard to show the students the flow of the program, how each line of code is executed.

Again make sure all the students followed and get their program working before moving to step 05.

## Next Lesson

Next time we're going to use recursion to construct a martu wangka number rule

Lesson written by Uyen Nguyen edited by Stephen Hazleton
