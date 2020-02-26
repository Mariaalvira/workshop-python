##4. More Control Flow Tools
Besides the while statement just introduced, Python uses the usual flow control statements known from other languages, with some twists.

#4.1. if Statements
Perhaps the most well-known statement type is the if statemen
#4.2. for Statements
The for statement in Python differs a bit from what you may be used to in C or Pascal. Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or giving the user the ability to define both the iteration step and halting condition (as C), Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.
#4.3. The range() Function
If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy.
#4.4. break and continue Statements, and else Clauses on Loops
The break statement, like in C, breaks out of the innermost enclosing for or while loop. Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the iterable (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement.
#4.5. pass Statements
The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.
#4.6. Defining Functions
The keyword def introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters. The statements that form the body of the function start at the next line, and must be indented.

The first statement of the function body can optionally be a string literal; this string literal is the function’s documentation string, or docstring. (More about docstrings can be found in the section Documentation Strings.) There are tools which use docstrings to automatically produce online or printed documentation, or to let the user interactively browse through code; it’s good practice to include docstrings in code that you write, so make a habit of it.
he keyword def introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters. The statements that form the body of the function start at the next line, and must be indented.
#4.7. More on Defining Functions
It is also possible to define functions with a variable number of arguments. There are three forms, which can be combined.

#4.7.1. Default Argument Values
The most useful form is to specify a default value for one or more arguments. This creates a function that can be called with fewer arguments than it is defined to allow.
#4.7.2. Keyword Arguments
Functions can also be called using keyword arguments of the form kwarg=value.
#4.7.3. Special parameters
By default, arguments may be passed to a Python function either by position or explicitly by keyword. For readability and performance, it makes sense to restrict the way arguments can be passed so that a developer need only look at the function definition to determine if items are passed by position, by position or keyword, or by keyword.
#4.7.3.1. Positional-or-Keyword Arguments
If / and * are not present in the function definition, arguments may be passed to a function by position or by keyword.

#4.7.3.2. Positional-Only Parameters
Looking at this in a bit more detail, it is possible to mark certain parameters as positional-only. If positional-only, the parameters’ order matters, and the parameters cannot be passed by keyword. Positional-only parameters are placed before a / (forward-slash). The / is used to logically separate the positional-only parameters from the rest of the parameters. If there is no / in the function definition, there are no positional-only parameters.

Parameters following the / may be positional-or-keyword or keyword-only.

#4.7.3.3. Keyword-Only Arguments
To mark parameters as keyword-only, indicating the parameters must be passed by keyword argument, place an * in the arguments list just before the first keyword-only parameter.

#4.7.3.4. Function Examples
Consider the following example function definitions paying close attention to the markers / and *
#4.7.3.5. Recap
As guidance:

Use positional-only if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when the function is called or if you need to take some positional parameters and arbitrary keywords.

Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed.

For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.

#4.7.4. Arbitrary Argument Lists
Finally, the least frequently used option is to specify that a function can be called with an arbitrary number of arguments. These arguments will be wrapped up in a tuple (see Tuples and Sequences). 
#4.7.5. Unpacking Argument Lists
The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments. For instance, the built-in range() function expects separate start and stop arguments. 
#4.7.6. Lambda Expressions
Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition.
#4.7.7. Documentation Strings
Here are some conventions about the content and formatting of documentation strings.

The first line should always be a short, concise summary of the object’s purpose. For brevity, it should not explicitly state the object’s name or type, since these are available by other means (except if the name happens to be a verb describing a function’s operation). This line should begin with a capital letter and end with a period.
#4.7.8. Function Annotations
Function annotations are completely optional metadata information about the types used by user-defined functions (see PEP 3107 and PEP 484 for more information).

Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no effect on any other part of the function. Parameter annotations are defined by a colon after the parameter name, followed by an expression evaluating to the value of the annotation.
#4.8. Intermezzo: Coding Style
Now that you are about to write longer, more complex pieces of Python, it is a good time to talk about coding style. Most languages can be written (or more concise, formatted) in different styles; some are more readable than others. Making it easy for others to read your code is always a good idea, and adopting a nice coding style helps tremendously for that.
Footnotes
1. Actually, call by object reference would be a better description, since if a mutable object is passed, the caller will see any changes the callee makes to it (items inserted into a list).