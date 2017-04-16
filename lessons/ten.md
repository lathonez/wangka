## Lesson Objectives

* [Classify Wangka](#classify-wangka)
* [Use wangka class to translate](#use-wangka-class-to-translate)
* [Next Lesson](#next-lesson)
* [Screenshots](#screenshots)
* [Diff](https://github.com/lathonez/wangka/compare/lesson-ten...lesson-eleven)

## New concepts being addressed

* Turning a bunch of functions into a class
* Scoping
* Importing our own class as an external library
* Returning results from our class to browser
* Main methods

## Classify Wangka

In order to be able to use our `wangka` code in our website, we need to make it into a class, so we can import it. At the moment, it is just a bunch of functions (a script) - and we can't use it in this way.

There are three things we need to do:

* Define the class and indent everything beneath. Demonstrate how to do this by higlighting the code and indenting it with `tab`.

```python
class: wangka

    def run_wangka_program():

```

* Add the class variable `self` as the first argument to each function. This is a good time to explain scoping. Now we've made a class, we can't access other functions in that class without referring to `self`. The function exists on the class, and we are inside the class, so we say `self` to access them. The reason we need to pass `self` in as the first argument to these functions is so that we are able to use it to access other functions within the class. We will see how in a moment.

```python
    def run_wangka_program(self):

    #..

    def get_wangka_number(self, number):
```

* Add the `self` reference anywhere we are calling a function. We need to change every call to `get_wangka_number` to `self.get_wangka_number`.

```python
            mw_num = self.get_wangka_number(2) + self.get_wangka_number(2)
            # etc, etc, etc
```

* Finally, we call our new class from outside when the file is run. Before this change, the code was just `run_wangka_program`, but now we are inside the class we need to reference it correctly, by creating a new instance of our class `wangka()` and then running the `run_wangka_program` method against it. We use the weird IF code to make sure that the code will only run if the program is been run from the command line, explain here about the `main` method. Compare it to the `main` method of the server. We can try later on what happens if this code is not in place.

```python
if __name__ == "__main__":
    wangka().run_wangka_program()
```

There are obviously a lot of changes here, and lots of room for errors. By now we should be used to using the red (x) on the side of our files in cloud9 to find errors. So the student should be able to figure out themselves where they have gone wrong.

We should test our program to make sure it still works before proceeding.

# Use Wangka class to translate

We need to import our new class and use it to translate the number. We've imported stuff before, but never something we've written ourselves

**server.py**

```
import wangka

#..

class translate:
    def GET(self):
        user_data = web.input()
        return wangka.wangka().get_wangka_number(int(user_data.number))
```

## Next Lesson

Next time we're going to format the translation nicely for our users - at the moment it's just a raw string, no HTML!

## Screenshots

![translated output](https://github.com/lathonez/wangka/blob/master/lessons/screens/10-after.PNG "translated output")
