## Lesson Objectives

* [Format output using html template](#format-output-using-html-template)
* [Next Lesson](#next-lesson)
* [Screenshots](#screenshots)
* [Diff](https://github.com/lathonez/wangka/compare/lesson-eleven...lesson-twelve)

## New concepts being addressed

* Template variables
* Hyperlink
* Rendering template with variables

## Format output using HTML template

The first thing we need to do is to create a HTML template. We've done this with our index.html page, but this time, our template is going to be `dynamic`. The content will change depending on the output of the translation.

Add the following html to a new file called `translated.html`:

* `def with` - this isn't actually HTML - it's python syntax! We're telling python's templating engine that our HTML template expects two variables to be set.
* `number` - the number the user asked to be translated
* `result` - the result of the translation
* `a href` - this is the first time we've used a `link` in our HTML, we need the user to be able to translate more numbers if necessary. The target of the link (`href`) is the root of our website (`index.html`).

```html
$def with (number, result)

<head>
    <title>Martu Wangka Numeric Translation of $number</title>
</head>
<body>
    <h3>The translation of $number in Martu Wangka is:</h3>
    <h1>$result</h1>
    <a href="/">Click here to translate some more numbers!</a>
</body>
```

We now need to use our translated.html template in our `translate` root. All we are doing here is assigning the values we want to the variables defined in our template, and then rendering the template with those variables.

**server.py**:

```python
class translate:
    def GET(self):
        user_data = web.input()
        number = int(user_data.number)
        result = wangka.wangka().get_wangka_number(int(user_data.number))
        render = web.template.render('.')
        return render.translated(number, result)
```


## Next Lesson

Next time we're going to use Javascript to check the user's input (client side validation)

## Screenshots

![formatted output](https://github.com/lathonez/wangka/blob/master/lessons/screens/11-after.PNG "formatted output")