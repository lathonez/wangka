## Lesson Objectives

* [Add our first HTML page](#add-our-first-html-page)
* [Create a form to capture input](#create-a-form-to-capture-input)
* [Next Lesson](#next-lesson)
* [Screenshots](#screenshots)
* [Diff](https://github.com/lathonez/wangka/compare/lesson-nine...lesson-ten3,mb )

## New concepts being addressed

* HTML templates
* HTML tags
* Forms
* GET / POST
* Client / Server
* User Input Validation

## Add our first HTML page

At the moment, our server is returning a string of characters to the browser, printing out 'hello, world'. This is very similar to printing out to the console, but just using the browser instead of the console.

Browsers use HTML to understand how to display content - and it is much easier for us to write nice web pages if we use HTML, instead of just printing raw characters to the browser.

To use HTML, we have to make a couple of changes to our program.

First let's create a HTML file called `index.html` (file > new, file > save). `index.html` is always the name given to your website's main page.

Inside `index.html`, let's add this code:

* `<h1></h1>` - this is our first example of HTML tags! h1 means header 1. The browser treats anything between these two tags as "Header 1" content. We'll see exactly what that means shortly. Pay attention to the closing tag `</h1>`. If we don't close the tag, any content afterwards will also be displayed as header 1.

**index.html**:

```html
<h1>Hello, world!</h1>
```

We also need to modify `server.py` to server our html template. Let's update our `GET` function to the following:

* `render =` : this searches for templates (anything ending in `.html`) in the current directory
* `return render.index()` :  this returns the content of the template (our HTML page above), to the browser

**server.py**
```python
    def GET(self, name):
        render = web.template.render('.')
        return render.index()
```

Ask the students what happens if they change the numbers (`<h2>`)

## Create a form to capture input

We need to work on our HTML a bit before it can be a proper web page. It is missing some fundamental properties that all web pages need in order to confirm to the web standards. Also, we need to add somewhere for our user to enter data. Let's update `index.html` to the following:

* `head`: HTML tag that defines the header of the page
* `title`: The title of our browsers window / tab
* `body`: HTML tag that defines the content of the page
* `form`: HTML component to capture users input. When our form is `submitted`, we are instructing the browser to go to the `/translate` handler - we don't have this yet, but we will soon! We're also telling it to use `GET` instead of `POST`. GET means that the data inside the form will be submitted into the URL, we will see how this works shortly
* `input`: This is where our user will be able to type their number to translate. We've set the type of the input to `number`, which means the user wont be able to type any text in. This is an example of `client side validation`. Discuss the difference between the client and server. The client is the website running in the user's browser, on their computer. The server is our python program running on cloud9. We should talk about client vs server validation. What other validation do we need on our input? Is it safe to rely on the client to handle it?
* `button`: This is the button the user will click when they are ready to have their number translated

**index.html**
```html
<head>
    <title>Martu Wangka Numeric Translator</title>
</head>
<body>
    <h3>Enter a number below to translate it into Martu Wangka!</h3>
    <form action="/translate" method="get">
        <input type="number" name="number"/>
        <button>Translate!</button>
    </form>
</body>
```

Get the students to test the page and find out what happens when they click "Translate". They should see the `/translate?number=22` bit go onto the URL:

* `translate`: the route we are going to in order to translate. We have no route for translate at the moment, so everything is going to `hello`
* `number:` the name of our form's input (set in the html above)
* `=22`: the value the user typed in

Finally, we need to add another route handler into our server. At the moment, everything is going to `hello`, which means nothing special will happen when the user clicks "Translate".

* Add a new  route for translate, if the form is submitted and the user goes to `/translate` the code will call our translate.GET function (below)
* Add a new function for translate. At the moment this just returns the number the user has asked to translate

**server.py**:

```python
urls = (
    '/translate', 'translate',

    #..

class translate:
    def GET(self):
        user_data = web.input()
        return user_data.number
```

## Next Lesson

Next time we're going to pass the number through to our translator

## Screenshots

![Our first HTML page](https://github.com/lathonez/powwow/blob/master/lessons/screens/9-after.png "Our first HTML page")

