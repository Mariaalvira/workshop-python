{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-1-30f4b8a490c2>, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-1-30f4b8a490c2>\"\u001b[1;36m, line \u001b[1;32m2\u001b[0m\n\u001b[1;33m    ef scope_test():\u001b[0m\n\u001b[1;37m                ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#9.2.1. Scopes and Namespaces Example\n",
    "ef scope_test():\n",
    "    def do_local():\n",
    "        spam = \"local spam\"\n",
    "\n",
    "    def do_nonlocal():\n",
    "        nonlocal spam\n",
    "        spam = \"nonlocal spam\"\n",
    "\n",
    "    def do_global():\n",
    "        global spam\n",
    "        spam = \"global spam\"\n",
    "\n",
    "    spam = \"test spam\"\n",
    "    do_local()\n",
    "    print(\"After local assignment:\", spam)\n",
    "    do_nonlocal()\n",
    "    print(\"After nonlocal assignment:\", spam)\n",
    "    do_global()\n",
    "    print(\"After global assignment:\", spam)\n",
    "\n",
    "scope_test()\n",
    "print(\"In global scope:\", spam)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-2-a72651622716>, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-2-a72651622716>\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    <statement-1>\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#9.3.1. Class Definition Syntax\n",
    "class ClassName:\n",
    "    <statement-1>\n",
    "    .\n",
    "    .\n",
    "    .\n",
    "    <statement-N>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#9.3.2. Class Objects\n",
    "class MyClass:\n",
    "    \"\"\"A simple example class\"\"\"\n",
    "    i = 12345\n",
    "\n",
    "    def f(self):\n",
    "        return 'hello world'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3.0, -4.5)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class Complex:\n",
    "    def __init__(self, realpart, imagpart):\n",
    "        self.r = realpart\n",
    "        self.i = imagpart\n",
    "\n",
    "x = Complex(3.0, -4.5)\n",
    "x.r, x.i\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "16\n"
     ]
    }
   ],
   "source": [
    "#9.3.3. Instance Objects\n",
    "x.counter = 1\n",
    "while x.counter < 10:\n",
    "    x.counter = x.counter * 2\n",
    "print(x.counter)\n",
    "del x.counter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'Complex' object has no attribute 'f'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-6-63bf62437ee2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#9.3.4. Method Objects\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mx\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m: 'Complex' object has no attribute 'f'"
     ]
    }
   ],
   "source": [
    "#9.3.4. Method Objects\n",
    "x.f()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'Complex' object has no attribute 'f'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-7-871a974d9bc0>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#9.3.4. Method Objects\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mx\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mxf\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mx\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mf\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mwhile\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'Complex' object has no attribute 'f'"
     ]
    }
   ],
   "source": [
    "#9.3.4. Method Objects\n",
    "x.f()\n",
    "\n",
    "xf = x.f\n",
    "while True:\n",
    "    print(xf())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-8-4ac43540e5aa>, line 9)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-8-4ac43540e5aa>\"\u001b[1;36m, line \u001b[1;32m9\u001b[0m\n\u001b[1;33m    >>> d = Dog('Fido')\u001b[0m\n\u001b[1;37m     ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#9.3.5. Class and Instance Variables\n",
    "class Dog:\n",
    "\n",
    "    kind = 'canine'         # class variable shared by all instances\n",
    "\n",
    "    def __init__(self, name):\n",
    "        self.name = name    # instance variable unique to each instance\n",
    "\n",
    ">>> d = Dog('Fido')\n",
    ">>> e = Dog('Buddy')\n",
    ">>> d.kind                  # shared by all dogs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-9-f757f62771a5>, line 8)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-9-f757f62771a5>\"\u001b[1;36m, line \u001b[1;32m8\u001b[0m\n\u001b[1;33m    >>> d = Dog('Fido')\u001b[0m\n\u001b[1;37m     ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "class Dog:\n",
    "\n",
    "    kind = 'canine'         # class variable shared by all instances\n",
    "\n",
    "    def __init__(self, name):\n",
    "        self.name = name    # instance variable unique to each instance\n",
    "\n",
    ">>> d = Dog('Fido')\n",
    ">>> e = Dog('Buddy')\n",
    ">>> d.kind                  # shared by all dogs\n",
    "'canine'\n",
    ">>> e.kind                  # shared by all dogs\n",
    "'canine'\n",
    ">>> d.name                  # unique to d\n",
    "'Fido'\n",
    ">>> e.name                  # unique to e\n",
    "'Buddy'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-10-5d4614af504d>, line 11)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-10-5d4614af504d>\"\u001b[1;36m, line \u001b[1;32m11\u001b[0m\n\u001b[1;33m    >>> d = Dog('Fido')\u001b[0m\n\u001b[1;37m     ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "class Dog:\n",
    "\n",
    "    tricks = []             # mistaken use of a class variable\n",
    "\n",
    "    def __init__(self, name):\n",
    "        self.name = name\n",
    "\n",
    "    def add_trick(self, trick):\n",
    "        self.tricks.append(trick)\n",
    "\n",
    ">>> d = Dog('Fido')\n",
    ">>> e = Dog('Buddy')\n",
    ">>> d.add_trick('roll over')\n",
    ">>> e.add_trick('play dead')\n",
    ">>> d.tricks                # unexpectedly shared by all dogs\n",
    "['roll over', 'play dead']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-11-8619753d1c44>, line 10)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-11-8619753d1c44>\"\u001b[1;36m, line \u001b[1;32m10\u001b[0m\n\u001b[1;33m    >>> d = Dog('Fido')\u001b[0m\n\u001b[1;37m     ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "class Dog:\n",
    "\n",
    "    def __init__(self, name):\n",
    "        self.name = name\n",
    "        self.tricks = []    # creates a new empty list for each dog\n",
    "\n",
    "    def add_trick(self, trick):\n",
    "        self.tricks.append(trick)\n",
    "\n",
    ">>> d = Dog('Fido')\n",
    ">>> e = Dog('Buddy')\n",
    ">>> d.add_trick('roll over')\n",
    ">>> e.add_trick('play dead')\n",
    ">>> d.tricks\n",
    "['roll over']\n",
    ">>> e.tricks\n",
    "['play dead']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block (<ipython-input-12-3ea09170d4ac>, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-12-3ea09170d4ac>\"\u001b[1;36m, line \u001b[1;32m6\u001b[0m\n\u001b[1;33m    w1 = Warehouse()\u001b[0m\n\u001b[1;37m     ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m expected an indented block\n"
     ]
    }
   ],
   "source": [
    "#9.4. Random Remarks\n",
    "class Warehouse:\n",
    "\n",
    "\n",
    "\n",
    "w1 = Warehouse()\n",
    "print(w1.purpose, w1.region)\n",
    "\n",
    "w2 = Warehouse()\n",
    "w2.region = 'east'\n",
    "print(w2.purpose, w2.region)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (<ipython-input-13-cf71a4421ac8>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-13-cf71a4421ac8>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    class Warehouse:\u001b[0m\n\u001b[1;37m                    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "class Warehouse:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Warehouse' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-14-066006f2ee06>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mw1\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mWarehouse\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mw1\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpurpose\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mw1\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mregion\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'Warehouse' is not defined"
     ]
    }
   ],
   "source": [
    ">>> w1 = Warehouse()\n",
    ">>> print(w1.purpose, w1.region)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Function defined outside the class\n",
    "def f1(self, x, y):\n",
    "    return min(x, x+y)\n",
    "\n",
    "class C:\n",
    "    f = f1\n",
    "\n",
    "    def g(self):\n",
    "        return 'hello world'\n",
    "\n",
    "    h = g"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Bag:\n",
    "    def __init__(self):\n",
    "        self.data = []\n",
    "\n",
    "    def add(self, x):\n",
    "        self.data.append(x)\n",
    "\n",
    "    def addtwice(self, x):\n",
    "        self.add(x)\n",
    "        self.add(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-17-92eec186f8ef>, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-17-92eec186f8ef>\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    <statement-1>\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#9.5. Inheritance\n",
    "class DerivedClassName(BaseClassName):\n",
    "    <statement-1>\n",
    "    .\n",
    "    .\n",
    "    .\n",
    "    <statement-N>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-18-a206b50df6ff>, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-18-a206b50df6ff>\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    <statement-1>\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#9.5.1. Multiple Inheritance\n",
    "class DerivedClassName(Base1, Base2, Base3):\n",
    "    <statement-1>\n",
    "    .\n",
    "    .\n",
    "    .\n",
    "    <statement-N>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (<ipython-input-19-4d289bac6b48>, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-19-4d289bac6b48>\"\u001b[1;36m, line \u001b[1;32m2\u001b[0m\n\u001b[1;33m    <statement-1>\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "#class DerivedClassName(Base1, Base2, Base3):\n",
    "    <statement-1>\n",
    "    .\n",
    "    .\n",
    "    .\n",
    "    <statement-N>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "#9.6. Private Variables\n",
    "class Mapping:\n",
    "    def __init__(self, iterable):\n",
    "        self.items_list = []\n",
    "        self.__update(iterable)\n",
    "\n",
    "    def update(self, iterable):\n",
    "        for item in iterable:\n",
    "            self.items_list.append(item)\n",
    "\n",
    "    __update = update   # private copy of original update() method\n",
    "\n",
    "class MappingSubclass(Mapping):\n",
    "\n",
    "    def update(self, keys, values):\n",
    "        # provides new signature for update()\n",
    "        # but does not break __init__()\n",
    "        for item in zip(keys, values):\n",
    "            self.items_list.append(item)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "#9.7. Odds and Ends\n",
    "class Employee:\n",
    "    pass\n",
    "\n",
    "john = Employee()  # Create an empty employee record\n",
    "\n",
    "# Fill the fields of the record\n",
    "john.name = 'John Doe'\n",
    "john.dept = 'computer lab'\n",
    "john.salary = 1000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "1\n",
      "2\n",
      "3\n",
      "one\n",
      "two\n",
      "1\n",
      "2\n",
      "3\n"
     ]
    },
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'myfile.txt'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-22-6fc5c8a41da7>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mchar\u001b[0m \u001b[1;32min\u001b[0m \u001b[1;34m\"123\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mchar\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 10\u001b[1;33m \u001b[1;32mfor\u001b[0m \u001b[0mline\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"myfile.txt\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     11\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mline\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m''\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'myfile.txt'"
     ]
    }
   ],
   "source": [
    "#9.8. Iterators\n",
    "for element in [1, 2, 3]:\n",
    "    print(element)\n",
    "for element in (1, 2, 3):\n",
    "    print(element)\n",
    "for key in {'one':1, 'two':2}:\n",
    "    print(key)\n",
    "for char in \"123\":\n",
    "    print(char)\n",
    "for line in open(\"myfile.txt\"):\n",
    "    print(line, end='')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<str_iterator at 0x57f1f90>"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = 'abc'\n",
    "it = iter(s)\n",
    "it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'a'"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "next(it)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'b'"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "next(it)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'c'"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "next(it)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "ename": "StopIteration",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mStopIteration\u001b[0m                             Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-27-bc1ab118995a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mnext\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mit\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mStopIteration\u001b[0m: "
     ]
    }
   ],
   "source": [
    "next(it)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Reverse:\n",
    "    \"\"\"Iterator for looping over a sequence backwards.\"\"\"\n",
    "    def __init__(self, data):\n",
    "        self.data = data\n",
    "        self.index = len(data)\n",
    "\n",
    "    def __iter__(self):\n",
    "        return self\n",
    "\n",
    "    def __next__(self):\n",
    "        if self.index == 0:\n",
    "            raise StopIteration\n",
    "        self.index = self.index - 1\n",
    "        return self.data[self.index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<__main__.Reverse at 0x4d2f7f0>"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rev = Reverse('spam')\n",
    "iter(rev)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "m\n",
      "a\n",
      "p\n",
      "s\n"
     ]
    }
   ],
   "source": [
    "for char in rev:\n",
    "    print(char)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "#9.9. Generators\n",
    "def reverse(data):\n",
    "    for index in range(len(data)-1, -1, -1):\n",
    "        yield data[index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "f\n",
      "l\n",
      "o\n",
      "g\n"
     ]
    }
   ],
   "source": [
    "for char in reverse('golf'):\n",
    "    print(char)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "285"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#9.10. Generator Expressions\n",
    "sum(i*i for i in range(10))                 # sum of squares\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "260"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "xvec = [10, 20, 30]\n",
    "yvec = [7, 5, 3]\n",
    "sum(x*y for x,y in zip(xvec, yvec))         # dot product\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'page' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-35-3d05ec1bc9c5>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0munique_words\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mset\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mword\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mline\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mpage\u001b[0m  \u001b[1;32mfor\u001b[0m \u001b[0mword\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mline\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'page' is not defined"
     ]
    }
   ],
   "source": [
    "unique_words = set(word for line in page  for word in line.split())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'page' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-36-9dc616d66a5e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0munique_words\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mset\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mword\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mline\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mpage\u001b[0m  \u001b[1;32mfor\u001b[0m \u001b[0mword\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mline\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mvaledictorian\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmax\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstudent\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgpa\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstudent\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mstudent\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mgraduates\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'golf'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'page' is not defined"
     ]
    }
   ],
   "source": [
    "unique_words = set(word for line in page  for word in line.split())\n",
    "\n",
    "valedictorian = max((student.gpa, student.name) for student in graduates)\n",
    "\n",
    "data = 'golf'\n",
    "list(data[i] for i in range(len(data)-1, -1, -1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['f', 'l', 'o', 'g']"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = 'golf'\n",
    "list(data[i] for i in range(len(data)-1, -1, -1))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
