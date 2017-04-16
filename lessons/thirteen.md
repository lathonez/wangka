## Lesson Objectives

* [Create and include CSS](#create-and-include-css)
* [Add basic styling](#add-basic-styling)
* [Screenshots](#screenshots)
* [Diff](https://github.com/lathonez/wangka/compare/lesson-thirteen...lesson-fourteen)

## New concepts being addressed

* CSS Introduction
* Link tag
* Static content
* Background Images
* Div tag
* class attribute
* pixels
* fonts

## Create and include CSS

We use CSS to define rules about what our page should look like, that our browser should obey. First, we need to create a folder in our project called `static` (file > create folder). Inside the folder, create a file called `wangka.css`. We place this in a static folder because it is not a HTML template. We use try to keep static files (css, images, etc) separate from our templates and logic.

We can test our CSS is linked correctly by adding the following rule:

```css
body {
    background-color: yellow;
}
```

We then need to use the `link` tag on each page, to tell the browser to load our static css file. Put this in both `index.html` and `translated.html`:

```html
    <link rel="stylesheet" type="text/css" href="static/wangka.css">
```

We should see that the background of both our pages has turned yellow.

## Add basic styling

If the students are confident, they are very welcome to look up CSS rules on Google and add their own. We will work through some basic ones in the class.

### Background image

Find a background JPEG image on google and upload it to c9 (file > upload local files). Make sure it is saved in the static folder and named `background.jpeg`.

Add the following CSS rule (remove the yellow background):

* background-image: display the given image as the background
* background-repeat: tell the browser not to tile the background image

```css
body {
    background-image: url("background.jpg");
    background-repeat: no-repeat;
}
```

### Central Div

The content of my page is now quite hard to read because it clashes with the background. To remedy this, we can put a containing box (or `div`) around our content, and use make that content opaque. Add the following code inside the body tag in `index.html` and `translated.html`.

The div is simply a container for our content, so we can have a separate background image for our body. The class means that a css rule we create called ".content" will apply to the div.

```html
    <div class="content">
    <!-- code goes here>
    </div>
```

Add the following css for our `.content` rule:

* `background-colour`: set the background colour to white, but 90% opaque. If the last argument was 1.0, we would not see the background image at all
* `max-width`: tell the content that it should only take up a certain space on the screen
* `padding`: make the content div have a gap between it and the actual content - this is why the writing is indented inside the box
* `text-align`: make the text be centered

```css
.content {
    background-color: rgba(255, 255, 255, 0.9);
    max-width: 300px;
    padding: 30px;
    text-align: center;
}
```

This is looking a lot nicer, but I also want it to be centered on my screen, based on the size of my background. If we open background.jpg in c9, we can get the dimensions. The students will know pixels from scratch but it is worth covering again here.

Mine are 736w * 506h. We know the width of our content is 360 (max width is 300, plus 60 for padding). So if we do 736-300/2, we should get a value of pixels to push our content out by to make it centered (188):

```css
.content {
    margin-left: 188px;
}
```

We might notice that the box is still a bit off center. This is because our body has a margin that is pushing everything out. We can add the following to our body class to stop this:

```css
.body {
    margin: 0px;
}
```

We can do the exact same calculation to center our content vertically, if we force the content to be, say, 125px high:

```css
.content {
    height: 125px;
}
```

We can do 506 (our background height) -125, -60 (padding) = 160:

```css
.content {
    margin-top: 160px;
}

Our home page looks really cool now, but not so with our translated page. As the content here varies so much in length, our best bet is just to make the whole background opaque and use a little padding. Change the class in our div to "translated" so we can give it a different style from the main page:

Add a class to the `translated.html` body tag:

```html
    <div class="translated">
```

And a corresponding CSS rule:

* `background-color`: identical to our main page
* `width` / `height`: We want our translated page to cover the whole background, to account for those long numbers
* `padding`: half the padding of our main page to make use of page space
* `text-align`: identical to our main page

```css
.translated {
    background-color: rgba(255, 255, 255, 0.9);
    width: 736px;
    height: 506px;
    padding: 15px;
    text-align: center;
}
```

### Font

The last thing we're missing for our professional looking translator is a nice aboriginal style font:

* Go to [Google Fonts](fonts.google.com) and pick a font you think suits the translator
* Click on the font to select it
* Click on "Families Selected" at the bottom
* Copy the link and add it to both `index.html` and `translated.html`, under the css link:

```html
<link href="https://fonts.googleapis.com/css?family=Gloria+Hallelujah" rel="stylesheet">
```

* Copy the CSS rule and add it to the body:

.body {
    font-family: 'Gloria Hallelujah', cursive;
}

Depending on which font was chosen, you may want to change the size of it (using the h1-h5) tags to make it fit with our page structure.

## Screenshots

![index](https://github.com/lathonez/powwow/blob/master/lessons/screens/13-index.png "index")

![translateds](https://github.com/lathonez/powwow/blob/master/lessons/screens/13-translated.png "translateds")