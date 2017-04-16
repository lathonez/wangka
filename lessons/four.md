## Lesson Objectives

* [Add Recursive Call to get_wangka_number](#add-recursive-call-to-get_wangka_number)
* [Next Lesson](#next-lesson)
* [Diff](https://github.com/lathonez/wangka/compare/lesson-four...lesson-five)

## New concepts being addressed

* Extend conditional statement (if-elif-else)
* Recursive function
* Martu Wangka Logic (continued)

## Add Recursive Call to get_wangka_number

We need to chanve the `get_wangka_number` function so it can call.. itself:

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

    else:

        mw_num = ""

    return mw_num
```

Ask the students to think about the Martu Wangka numbering system. What is the difference between number 1 and number 2 in Martu Wangka? How about number 3? How can I get number 3 from number 2 and number 1? etc. Then show the how each number is constructed in Martu Wangka using the previous numbers.

Ask the students to identify function calls. Is there anything special about this function call? Show the student that the function is calling itself. This type of function is called recursive function.

For example, when you input number 2, it will first get the return value of `get_wangka_number(1)`, which is "kuja"

`get_wangka_number(1) + "rra"` Then "kuja" will concatenate with "rra" and return "kujarra" when input number 2.


## Next Lesson

Next time we're going to introduce math libraries to translate bigger numbers

Lesson written by Uyen Nguyen edited by Stephen Hazleton
