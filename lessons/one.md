## Lesson Objectives

* [Setup Cloud9 Workspace](#setup-cloud9-workspace)
* [Run simple Python Progam](#run-simple-python-program)
* [Next Lesson](#next-lesson)
* [Diff](https://github.com/lathonez/powwow/compare/lesson-one...lesson-two)

## New concepts being addressed

* IDE
* Cloud
* Command Line (CLI)
* Printing Text

## Setup Cloud9 Worskapce

We're going to be using the Cloud 9 IDE for this course, which means that anyone can access it from home as long as they have a computer with a browser!

The first thing we need to do is setup our workspace. Ask all the students to go to [http://c9.io](http://c9.io) and login using the details provided.

* Click > Create new workspace - explain to the students what a workspace is, go into fundamental stuff about the cloud. The workspace we are creating is the same as a scratch project for a single game (e.g. scratch > create)
* Add the following details into the new project: name - wangka, private, python (we are coding in python - this will make sure the workspace is set up with the tools we need)
* Click > Create Workspace

We now have our workspace! The first thing we want to do is hide a bunch of stuff we wont be using in this project - it just gets in the way. We want to hide the tabs on the left and right hand sides of the workspace. Right click on a tab and check the following:

* outline
* debugger
* commands
* navigate
* collaborate

## Cloud 9 Overview

Draw as many parallels between scratch and c9 as you can, they are similar enough concepts. We have two main parts to c9. The main bit at the top where our code lives, and the terminal at the bottom where we can run / preview our code. This is similar to scratch coding / preview area.

We're going to make a new file called `wangka.py`. We're going to be working with this file for the next few weeks - it will be the only file we need for the bulk of this course:

* File > new file
* File > save (`wangka.py`)

We're then going to use the command line / terminal in c9 for the first time. Explain the CLI to the students, it is exactly the same as using the keyboard and mouse, but is more powerful as we can tell the computer exactly what we want to do, and work with it's output directly.

The first thing we want to do with the command line, is find our file.

* Type `ls` in the console, we should see `wangka.py` in the output
* Type `python wangka.py` in the console. Nothing happend - ask the students why - they know this from scratch! (we haven't told the computer to do anything yet - the file is empty)*[]:


## Run Simple Python Program

Add the following code to the file, and re-run it. This code is asking Python to say something to the user via the command line. Very similar to "looks > say" in scratch.

`print 'hello world!'`

We have written our first bit of python in c9.

## Next Lesson

Next time we're going to start work on our number translation program
