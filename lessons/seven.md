## Lesson Objectives

* [Validate User Input](#validate-user-input)
* [Next Lesson](#next-lesson)
* [Diff](https://github.com/lathonez/wangka/compare/lesson-seven...lesson-eight)

## New concepts being addressed

* Input Validation
* Edge Cases

## Validate User Input

Ask the students to input a really big number of about 17 digits and tell you what happen to the program.

Since Python recursive has limitation in handling big number of recursive times, make sure to check user input so that the program doesn’t crash!

```python
def run_wangka_program():

    print("Welcome to The Martu Wangka Numbers!")

    while True:

        number = int(input("Please enter a number: "))

        if(number > 9999999999999999):

            ans = raw_input("Please enter a number smaller than 9999999999999999. Press Enter to continue.")

        else:

            print("The Martu Wangka says: " + get_wangka_number(number))

        ans = input("Would you like to try another number? (y/n) ")

        if ans == 'n':

            print("Thank you for learning The Martu Wangka Numbers!")

            break
```

Ask the students to run and test the program again with a really big number and see if the program can handle it.

Review the entire the program with the students.

Ask them questions about the concepts they learnt in building Martu Wangka Number Translator program.

## Next Lesson

Next time we're going to start work on our translator website

Lesson written by Uyen Nguyen edited by Stephen Hazleton

