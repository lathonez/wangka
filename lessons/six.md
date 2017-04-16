## Lesson Objectives

* [Keep the program running until the user wants to quit](#keep-the-program-running-until-the-user-wants-to-quit)
* [Next Lesson](#next-lesson)
* [Diff](https://github.com/lathonez/wangka/compare/lesson-six...lesson-seven)

## New concepts being addressed

* While Loop
* Break Statement
* Testing (continued)

## Keep the program running until the user wants to quit

Add the following code to our `run_wangka_program` function:

```python
def run_wangka_program():

    print("Welcome to The Martu Wangka Numbers!")

    while True:

        number = int(input("Please enter a number: "))

        print("The Martu Wangka says: " + get_wangka_number(number))

        ans = rawinput("Would you like to try another number? (y/n) ")

        if ans == 'n':

            print("Thank you for learning The Martu Wangka Numbers!")

            break
```

Ask the students to guess what each line of the code is doing before running the program.

They should be able to explain function declaration, function calls, variable assignments, the difference between variable assignment and string comparison, string concatenation and conditional statements.

The only 2 lines of code that they are not learnt yet are `while True` and `break`.

Show the student the flow of the loop when the condition is always true and when the condition is met and the loop is break.

Make sure the code is indented properly under `while` statement and `if` statement.

Ask the students to run the program and try out different option.

Ask for a volunteer to explain the flow of the while loop. Give a volunteer student a number and ask them to hand run through the program. When the program asks “Would you like to try another number? (y/n)”, give the student either a “y” or “n” answer and asks what the program will do next.

Ask the students to run and test their program with different numbers.

Make sure all the students get the program working before moving to step 08.

## Next Lesson

Next time we're going to review our translator code and fix some final problems with it

Lesson written by Uyen Nguyen edited by Stephen Hazleton
