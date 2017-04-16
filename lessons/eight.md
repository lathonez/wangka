## Lesson Objectives

* [Install web.py](#install-web.py)
* [Hello World HTML](#hello-world-html)
* [Next Lesson](#next-lesson)
* [Diff](https://github.com/lathonez/wangka/compare/lesson-eight...lesson-nine)

## New concepts being addressed

* Installing an external python library
* HTML basics
* Running the web server
* URL parameters
* Classes
* HTTP GET

## Install Web.py

Our program is working really well by now, but it isn't very useful to most people. Only dev experts know how to run python programs.

By using an external framework we are able to expose our program to the internet, and make it available to the whole world!

The first thing we need to do for this is install a framework called `web.py`. This is a python framework for making websites - it will allow us to run our python code from a web page!

Type this into the console to install `web.py`:

* `sudo` - means we are doing something with the system that needs administrative access. Explain about different user levels.
* `pip` - a package manager for python
* `install` - command to the package manager that installs our package
* `web.py` - the name of the package we want to install

```
sudo pip install web.py
```

## Hello World HTML

We're going to add the following code to a new file, called `server.py` (file > new, file > save)

The following is the example code from the `web.py` home page:

* `import`: import the `web.py` library
* `urls`: We have to tell our web server how to route requests. In this way we can have different pages depending on what people type in their URL bar. At the moment, our server is sending everything to the `hello` class
* `app`: An instance of our webserver with the `urls` above applied
* `hello` class: Explain that classes are way that we can combine / encapsulate related functions.
* `GET`: there are two main HTTP calls, `GET` and `POST`. When we navigate to a webpage, a `GET` request is made. the `GET` function in our `hello` class is the code that will run if someone goes to our website
* `name`: a parameter is passed to our function from the URL - see if the students can figure out how it is used.

```python
import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()
```

## Running the web server

We run the server in the same way as we ran our translator app, from the command line:

```
python server.py
```

We will see some output in the console, and cloud9 will popup saying our application is available. If we click on the link provided  (or Preview > Preview Running Application) we should see our very very basic web page!

Ask the students to type something on the end of the URL - if they type their name, the website will say hello to them!

## Next Lesson

Next time we're going to use a form to capture user input on our website


