## Lesson Objectives

* [Handle numbers bigger than 5](#handle-numbers-bigger-than-5)
* [Testing](#testing)
* [Next Lesson](#next-lesson)
* [Diff](https://github.com/lathonez/wangka/compare/lesson-five...lesson-six)

## New concepts being addressed

* Import an external library
* External library functions
* Math operators
* Debugging / Testing
* Stripping Whitespace from a string

## Handle numbers bigger than 5

Add the following code at the top of the file:

```
import math
```

Importing the math library will allow us to access Math functions.

We will use math.floor() function to get the rounded down number.

```python
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
```

Review with the students these math terms such as quotient, remainder, modulo, round down to make sure they know what these mean.

Any number that is equal or bigger than 5 can be handle by the condition under `elif` number >= 5

Explain the priority or order of execution of `floor_quotient = math.floor(number/5)`. number will be divided by 5, then rounded down using math.floor, and finally assigned to floor_quotient.

Explain the priority or order of execution of `remainder = number % (floor_quotient * 5)`. floor_quotient is multiplied by 5, then number is modulo by the result of (floor_quotient * 5), and finally assigned to remainder.

Show the students how these formulas are derived using different examples in Martu Wangka Number System table.

## Testing

* Ask the students what number they want to try and hand run a program line by line with the student to show them the flow of the program.
* Ask the students to run and play with a program with any number and see if they can find any problem.
* Ask the students to to run with any big number such as 6743. It will print out the string with some extra white spaces. To remove these extra whitespaces, in the return statement, instead of “return mw_num”, use “return mw_num.strip()”. strip() removes extra whitepaces from the front and the back of the string.
* Ask the students to run and test again with the same number.

## Next Lesson

Next time we're going to add a feature that lets the user keep using the program until they quit

Lesson written by Uyen Nguyen edited by Stephen Hazleton
