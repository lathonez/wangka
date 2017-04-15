## Lesson Objectives

* [Understand Martu Wangka Numbering System](#understand-martu-wangka-numbering-system)
* [Project Explanation](#project-explanation)
* [First Python Function](#first-python-function)
* [Next Lesson](#next-lesson)
* [Diff](https://github.com/lathonez/wangka/compare/lesson-two...lesson-three)

## New concepts being addressed

* Martu Wangka Numbering System

## Understand Martu Wangka Numbering System

Put this table on the projector and work through it, everyone should be able to count in Martu Wangka or we are going to have a difficult time writing a translator for it!

Do some exercises with some higher numbers.

Number | Martu Wangka |Explanation
--- | --- | ---
1 | kuja  |
2 | kujarra |
3 | kujarra kuja |
4 | kujarrakujarra |
5 | marakuja | mara means hand/feet which has 5 fingers/toes, marakuja means 1 hand of 5
6 | marakuja kuja |
7 | marakuja kujarra |
8 | marakuja kujarra kuja |
9 | marakuja kujarrakujarra |
10 | marakujarra | it means 2 hands of 5
11 | marakujarra kuja |
12 | marakujarra kujarra |
15 | marakujarra kuja | instead of marakujarra marakuja because it's 3hands of 5
19 | marakujarra kuja kujarrakujarra | instead of marakujarra marakuja kujarrakujarra because it's 15 and 4

## Project Explanation

We want to write a program that asks us for a number. We give it a number (22) and it replies to us with the correct word in Martu Wangka (marakujarra marakujarra kuja).

After that, we will make a website for this, so anyone in the world can use our translator to figure out the numbers.

If there is time, we will even have a spoken translation!

## First Python Function

Let's open our file we worked on last time, it is `wangka.py` in the LHS files view. Delete our 'Hello, world!' line, and add the following:

```python
def run_wangka_program():

print("Welcome to The Martu Wangka Numbers!")

run_wangka_program()
```

In the console, run our program `python wangka.py`. Note we can press the up arrow to run easily without typing.

It will print out the line &quot;Welcome to The Martu Wangka Numbers!”

Make sure all the students get the code working before going through line by line to explain. First, explain to a student what is a function. A function is a named section of a program that performs a specific task. Give an example that relates to their daily activities such as, ask the students “What do you need to do to make a salad?”, they may say “Clean a salad, chop salad, clean tomatoes, prepare the sauce, etc.”. You then can say, each activity is a function, to do a specific task, so that together they help achieve the purpose of the program, in this case, “Making A Salad”.

The first line of the program def run_wangka_program(): starts with “def” and ends with a colon “:” is called a function declaration.

The second line is indented by spaces (usually 4 spaces) or a tab, right under the function declaration run_wangka_program, means it is INSIDE the function declaration, and acts as the instruction to perform that function. print(“”) is a function call. print(“”) is a function that is already declared in Python.

The third line is NOT indented but ALIGNED with the first line indicates that this line of code is OUTSIDE of the function declaration run_wangka_program.

The third line is a function call of run_wangka_program(). Function declaration only defines what needs to be done, but nothing is done until a function is called.

Ask a student to remove the third line of code and run the program again. Nothing will print out. Ask them why to see if they understand the difference between function declaration and function call.

## Next Lesson

Next time we're going to

Lesson written by Uyen Nguyen edited by Stephen Hazleton