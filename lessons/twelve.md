## Lesson Objectives

* [Validate Client Input](#validate-client-input)
* [Next Lesson](#next-lesson)
* [Screenshots](#screenshots)
* [Diff](https://github.com/lathonez/wangka/compare/lesson-twelve...lesson-thirteen)

## New concepts being addressed

* Javscript introduction
* `<script>`
* Form events
* Required HTML inputs
* Javascript Alerts

## Validate client input

We have some code in our `wangka.py` which makes sure users cannot enter numbers over a certain amount. However, we are bypassing that code here as we are taking the input directly from the web form.

We need to validate the input on the client, before we allow it to be submitted, which will make sure that no bad input can get to our server.

The first thing we're going to do, is make sure the user has to enter _something_! We can do this easily by using the `required` HTML directive:

```html
        <input type="number" name="number" required/>
```

Next we should make sure the user can't enter a large number, or a number smaller than zero. To do this we're going to use `javascript`. Javascript is very similar to python. It is a basic scripting language. The key difference is that our browser can understand Javascript, but it can't understand python. So we have to use a simple Javascript function to validate our input. One main difference between python and Javascript in terms of coding, is that python uses indentations to define function scope, whereas Javascript uses curly braces: `{}`. It's still very good practice to keep the indentations the same as they would be in python anyway - so we just need to remember the curly braces!

We're going to write some Javascript straight into our HTML page, to do this we use the `<script></script>` tag - this tells the browser that it is reading Javascript instead of HTML:

Put this inside the `<body>` of your HTML, at the top:

* `function validateForm` - we declare a javascript function so we can access it from eleswhere
* `var number` - we declare a variable for our number - this is the input the user has entered
* `alert` - these will show a simple alert message to the user
* `return false` - this is very important, it stops our form from being submitted

```html
    <script type="text/javascript">
        function validateform() {
            var number = parseInt(document.forms["translate"]["number"].value);

            if (number < 1) {
                alert("Please enter a number greater than zero!");
                return false;
            }

            if (number > 9999999999999999) {
                alert("Please enter a number smaller than 9999999999999999!");
                return false;
            }
        }
    </script>
```

Now we have a Javascript function to validate our form, but we are not using it yet. To use it, we use the form `event` called `onsubmit`. This event is triggered when the user tries to submit the form, and will prevent the submission from happening if `false` is returned.

We also name our form "translate" so we can access it easily from the Javascript above.

```html
    <form name="translate" action="/translate" onsubmit="return validateform()" method="get">
```

Get the students to test their code, they should not be able to submit the form if:

* The number is not set
* The number is less than 0
* The number is greater than 9999999999999999

## Next Lesson

Next time we're going to use CSS to create a cool theme for our website

## Screenshots

![negative](https://github.com/lathonez/wangka/blob/master/lessons/screens/12-negative.PNG "negative")

![large](https://github.com/lathonez/wangka/blob/master/lessons/screens/12-large.PNG "large")