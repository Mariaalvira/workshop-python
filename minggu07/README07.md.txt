#9. Classes
Classes provide a means of bundling data and functionality together. 
Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. 
Class instances can also have methods (defined by its class) for modifying its state.

##9.1. A Word About Names and Objects
Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object.
This is known as aliasing in other languages. This is usually not appreciated on a first glance at Python, and can be safely ignored when dealing with immutable basic types (numbers, strings, tuples). However, aliasing has a possibly surprising effect on the semantics of Python code involving mutable objects such as lists, dictionaries, and most other types. 
This is usually used to the benefit of the program, since aliases behave like pointers in some respects.

##9.2. Python Scopes and Namespaces
Before introducing classes, I first have to tell you something about Python’s scope rules. 
Class definitions play some neat tricks with namespaces, and you need to know how scopes and namespaces work to fully understand what’s going on. 
Incidentally, knowledge about this subject is useful for any advanced Python programmer.
Although scopes are determined statically, they are used dynamically. At any time during execution, there are at least three nested scopes whose namespaces are directly accessible:
->the innermost scope, which is searched first, contains the local names
->the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
->the next-to-last scope contains the current module’s global names
->the outermost scope (searched last) is the namespace containing built-in names

###9.2.1. Scopes and Namespaces Example
Note how the local assignment (which is default) didn’t change scope_test’s binding of spam. The nonlocal assignment changed scope_test’s binding of spam, and the global assignment changed the module-level binding.
You can also see that there was no previous binding for spam before the global assignment.

##9.3. A First Look at Classes
Classes introduce a little bit of new syntax, three new object types, and some new semantics.

###9.3.1. Class Definition Syntax
Class definitions, like function definitions (def statements) must be executed before they have any effect. (You could conceivably place a class definition in a branch of an if statement, or inside a function.)
In practice, the statements inside a class definition will usually be function definitions, but other statements are allowed, and sometimes useful — we’ll come back to this later. The function definitions inside a class normally have a peculiar form of argument list, dictated by the calling conventions for methods — again, this is explained later.
When a class definition is entered, a new namespace is created, and used as the local scope — thus, all assignments to local variables go into this new namespace. In particular, function definitions bind the name of the new function here.
When a class definition is left normally (via the end), a class object is created. This is basically a wrapper around the contents of the namespace created by the class definition; we’ll learn more about class objects in the next section. The original local scope (the one in effect just before the class definition was entered) is reinstated, and the class object is bound here to the class name given in the class definition header (ClassName in the example).

###9.3.2. Class Objects
Class objects support two kinds of operations: attribute references and instantiation.
Attribute references use the standard syntax used for all attribute references in Python: obj.name. Valid attribute names are all the names that were in the class’s namespace when the class object was created.

###9.3.3. Instance Objects
Now what can we do with instance objects? The only operations understood by instance objects are attribute references. There are two kinds of valid attribute names: data attributes and methods.
data attributes correspond to “instance variables” in Smalltalk, and to “data members” in C++. Data attributes need not be declared; like local variables, they spring into existence when they are first assigned to.

###9.3.4. Method Objects
What exactly happens when a method is called? You may have noticed that x.f() was called without an argument above, even though the function definition for f() specified an argument. What happened to the argument? Surely Python raises an exception when a function that requires an argument is called without any — even if the argument isn’t actually used…
Actually, you may have guessed the answer: the special thing about methods is that the instance object is passed as the first argument of the function. In our example, the call x.f() is exactly equivalent to MyClass.f(x). In general, calling a method with a list of n arguments is equivalent to calling the corresponding function with an argument list that is created by inserting the method’s instance object before the first argument.
If you still don’t understand how methods work, a look at the implementation can perhaps clarify matters. When a non-data attribute of an instance is referenced, the instance’s class is searched. If the name denotes a valid class attribute that is a function object, a method object is created by packing (pointers to) the instance object and the function object just found together in an abstract object: this is the method object. When the method object is called with an argument list, a new argument list is constructed from the instance object and the argument list, and the function object is called with this new argument list.

###9.3.5. Class and Instance Variables
Generally speaking, instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class:

##9.4. Random Remarks
If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritizes the instance

##9.5. Inheritance
Of course, a language feature would not be worthy of the name “class” without supporting inheritance.
Python has two built-in functions that work with inheritance:
->Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.
->Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.

###9.5.1. Multiple Inheritance
For most purposes, in the simplest cases, you can think of the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy. Thus, if an attribute is not found in DerivedClassName, it is searched for in Base1, then (recursively) in the base classes of Base1, and if it was not found there, it was searched for in Base2, and so on.
In fact, it is slightly more complex than that; the method resolution order changes dynamically to support cooperative calls to super(). This approach is known in some other multiple-inheritance languages as call-next-method and is more powerful than the super call found in single-inheritance languages.

##9.6. Private Variables
“Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.
Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses), there is limited support for such a mechanism, called name mangling. Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a class.

##9.7. Odds and Ends
Sometimes it is useful to have a data type similar to the Pascal “record” or C “struct”, bundling together a few named data items.

##9.8. Iterators
This style of access is clear, concise, and convenient. The use of iterators pervades and unifies Python. Behind the scenes, the for statement calls iter() on the container object. The function returns an iterator object that defines the method __next__() which accesses elements in the container one at a time. When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate. You can call the __next__()

##9.9. Generators
Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).

##9.10. Generator Expressions
Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions but with parentheses instead of square brackets. These expressions are designed for situations where the generator is used right away by an enclosing function. Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory friendly than equivalent list comprehensions.