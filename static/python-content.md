# Python

[Introduction to Python](#Introduction to Python)

[Basic Programming](#Basic Programming Constructs)

[Whitespace](#Whitespace)

[Variables and DataTypes](#Variables)

[Functions](#Functions)

[Selection](#Selection)

[Iteration](#Iteration)

## Introduction to Python
## What is Python

Python is different to most programming languages because it is a scripting language.  It is designed because of it is simplicity and the ability to produce high end applications such as web development and bash script. This is a perfect language for beginners, because it is a general purpose language.

## Why Use Python
Because the systems were built so long ago, IS needed a way in building new systems to help the existing old systems and make the caseworker’s life and the customers life a lot easier. The old systems were built using PL1 and Delphi languages 15 years ago.  So that is why the main languages we use are Python and Java, because it is a perfect programming language for beginners and so many apps on the web use it.  This makes it easy to follow the GDS guidelines of styling and to make it accessible too.

## How to Download Python
If you want to download Python on your home computer or on a non DITI machine, you need to go onto https://www.python.org
In the Land Registry we use Python 3, so it is recommended you install the latest version of Python 3 on whatever operating system you want. If you want to download it using your Land Registry DITI computer, you will have to raise a Marval Request on My Self Service. More information on how you can do this can be found on the HR Portal or via talking to your team lead, line manager or your buddy. You will have to ask permission from your team lead to see its okay with the software being installed and you put that relevant person in the Authorisation box. You will need your LRQ/ LLID of your machine so the relevant people can remotely install the software for you, without you needing to do anything.  Once it is been approved, the request gets taken to Service Desk and they will sort the rest out.

-----------------------------------------------------------------------------------------------------------------------------
## Basic Programming Constructs
The first program that you write in any language is Hello World and it gives you a basic understanding of the syntax. To print a line to the program, you just use the keyword print, followed by the word you want to print in brackets. In this case, we would want to print:

```
print ("Hello World")
```
This is how it appears in Python.

Image here:

## Whitespace

Whitespace is used in Python to structure code. It is different than languages such as Java or C# where indentation is done by using curly braces { }. In Python it is different.  Once a function is declared, you have to indent the code with four spaces in the first line and another 4 spaces before return. Here is an example:


```
def spam():
    eggs = 12
    return eggs

```
-----------------------------------------------------------------------------------------------------------------------------

## Variables
If you want to create a web app, they all involve storing and working with different types of data by using variables. Variables stores that particular data and gives it a specific name.
Eg:

```
variable = 5

```
This variable called variable now stores the number 5. How you name the variable it doesn’t matter. However it is strongly suggested that you start the first word of your variable in lower case.

## Data types
The data types in Python can be grouped into several classes. These are the following:

Int: non-limited length in Python 3

Long: A non-limited length which only exists in Python 2

Float: floating point numbers

Complex: complex numbers

str: String as a sequence of Unicode characters

bytes: Sequence of integers in the range of 0-255 in Python 3.x

dict: Python Dictionaries - element of a list is associated with a definition.

-----------------------------------------------------------------------------------------------------------------------------

##Functions
What happens if you want to keep reusing the same code all over again, but it repeats throughout your code, then it becomes hard for code to read. Functions help solve that and you can reuse code, without writing the same block of code multiple times.
Here is what a function should have:
A function contains at least 1 argument and 1 parameter, or it can have infinite amount of these. You may not have seen this but print() is a function. This function contains an unlimited amount of arguments.
A function begins with the keyword def along with the function name and relevant arguments. After declaring a function, you end the first line with a colon (:).  You got to make sure that it is indented.
You then print the output with the relevant arguments or return it.

Example of printing the output:

```
def my_function_with_args(username, greeting):
    print "Hello, %s , From My Function!, I wish you %s"%(username, greeting)

```



##Selection
Selection in Python is also known as one type of control flow.  Here are a few examples.

## If statement
The if statement will execute code if the condition is true. For example, if 8 is less than 9, it would print whatever is after that line of code.

```
if 8 < 9
    print "Eight is less than nine!"
```
You can also declare it by using functions:

```
def function_1():
if 1 < 2:
    def function_2():
if 2 < 3:
     return “Success #2”

print function_1()
print function_2()

```
-----------------------------------------------------------------------------------------------------------------------------

## Else Statements
Else statement follows the if statement. This tells the program that if the if statement is not true, then the code after the else statement would execute.

You can do it with multiple functions in the same way as the previous example.

```
answer = "'Tis but a scratch!"
def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:         
        return  False      # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:          
        return False       # Make sure this returns False

        ```

## Else if Statements (nested ifs)
Elif is a short form for else if. It is saying if the first expression is true, it checks to see if the 2nd expression is true and so on and so on.
In the example below, the elif statement is only checked if the first expression is false.

```
if 8 > 9:
    print "I don't get printed!"
elif 8 < 9:
    print "I get printed!"
else:
    print "I also don't get printed!"

  ```

-----------------------------------------------------------------------------------------------------------------------------

## Iteration in Python
If we wanted to do similar things many times, then iteration is a perfect tool to do that. There are many types of things that can happen with iteration. With every loop it has a condition which is an expression that decides whether the loop is going to be executed or not.

### While Loops
While Loops are known as conditional loop, which means that the loop will keep iterating until the conditions are met. It is indefinite, because there is no guarantee on when the loop will end. Like the if statement, the condition has a boolean expression which is set to either true or false. Once the condition is true, it will keep executing. If the condition is not true, it would stop and it would continue to the code outside of the loop.


This is a while loop example:
```
password = "secret"
while password != "secret":
    password = input("Please enter the password: ")
    if password == "secret":
        print"Thank you. You have entered the correct password")
    else:
        print("Sorry the value entered in incorrect - try again")

  ```

## For Loops
For Loop is used to repeat certain things a number of times. How many times the code should be repeated is indicated in the first line of the for loop.

Here is a basic example of an for loop:

```
for counter in range(5):
      print("hello world")

      ```
