{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-1-367aa7e9e39d>, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-1-367aa7e9e39d>\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    while True print('Hello world')\u001b[0m\n\u001b[1;37m                   ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#8.Errors and Exceptions\n",
    "#8.1. Syntax Errors\n",
    "while True print('Hello world')\n",
    "  File \"<stdin>\", line 1\n",
    "    while True print('Hello world')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "ZeroDivisionError",
     "evalue": "division by zero",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mZeroDivisionError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-647d0dbab774>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#8.2 Exceptions\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;36m10\u001b[0m \u001b[1;33m*\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m/\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mZeroDivisionError\u001b[0m: division by zero"
     ]
    }
   ],
   "source": [
    "#8.2 Exceptions\n",
    "10 * (1/0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'spam' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-c98bb92cdcac>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;36m4\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0mspam\u001b[0m\u001b[1;33m*\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'spam' is not defined"
     ]
    }
   ],
   "source": [
    "4 + spam*3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "can only concatenate str (not \"int\") to str",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-d2b23a1db757>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;34m'2'\u001b[0m \u001b[1;33m+\u001b[0m \u001b[1;36m2\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: can only concatenate str (not \"int\") to str"
     ]
    }
   ],
   "source": [
    "'2' + 2"
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
      "Please enter a number: 4\n"
     ]
    }
   ],
   "source": [
    "#8.3. Handling Exceptions\n",
    "while True:\n",
    "    try:\n",
    "        x = int(input(\"Please enter a number: \"))\n",
    "        break\n",
    "    except ValueError:\n",
    "        print(\"Oops!  That was no valid number.  Try again...\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-6-7bb513cf5372>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-6-7bb513cf5372>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    except (RuntimeError, TypeError, NameError):\u001b[0m\n\u001b[1;37m         ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "... except (RuntimeError, TypeError, NameError):\n",
    "...     pass\n",
    "\n",
    "class B(Exception):\n",
    "    pass\n",
    "\n",
    "class C(B):\n",
    "    pass\n",
    "\n",
    "class D(C):\n",
    "    pass\n",
    "\n",
    "for cls in [B, C, D]:\n",
    "    try:\n",
    "        raise cls()\n",
    "    except D:\n",
    "        print(\"D\")\n",
    "    except C:\n",
    "        print(\"C\")\n",
    "    except B:\n",
    "        print(\"B\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "OS error: [Errno 2] No such file or directory: 'myfile.txt'\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "try:\n",
    "    f = open('myfile.txt')\n",
    "    s = f.readline()\n",
    "    i = int(s.strip())\n",
    "except OSError as err:\n",
    "    print(\"OS error: {0}\".format(err))\n",
    "except ValueError:\n",
    "    print(\"Could not convert data to an integer.\")\n",
    "except:\n",
    "    print(\"Unexpected error:\", sys.exc_info()[0])\n",
    "    raise"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cannot open -f\n",
      "C:\\Users\\USER\\AppData\\Roaming\\jupyter\\runtime\\kernel-e832abe1-1997-41fc-856b-65a3272a984c.json has 12 lines\n"
     ]
    }
   ],
   "source": [
    "for arg in sys.argv[1:]:\n",
    "    try:\n",
    "        f = open(arg, 'r')\n",
    "    except OSError:\n",
    "        print('cannot open', arg)\n",
    "    else:\n",
    "        print(arg, 'has', len(f.readlines()), 'lines')\n",
    "        f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'Exception'>\n",
      "('spam', 'eggs')\n",
      "('spam', 'eggs')\n",
      "x = spam\n",
      "y = eggs\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    raise Exception('spam', 'eggs')\n",
    "except Exception as inst:\n",
    "    print(type(inst))    # the exception instance\n",
    "    print(inst.args)     # arguments stored in .args\n",
    "    print(inst)          # __str__ allows args to be printed directly,\n",
    "                         # but may be overridden in exception subclasses\n",
    "    x, y = inst.args     # unpack args\n",
    "    print('x =', x)\n",
    "    print('y =', y)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Handling run-time error: division by zero\n"
     ]
    }
   ],
   "source": [
    "def this_fails():\n",
    "    x = 1/0\n",
    "\n",
    "try:\n",
    "    this_fails()\n",
    "except ZeroDivisionError as err:\n",
    "    print('Handling run-time error:', err)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "HiThere",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-11-60371cde561b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#8.4. Raising Exceptions\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mraise\u001b[0m \u001b[0mNameError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'HiThere'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: HiThere"
     ]
    }
   ],
   "source": [
    "#8.4. Raising Exceptions\n",
    "raise NameError('HiThere')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "An exception flew by!\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "HiThere",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-12-bf6ef4926f8c>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m     \u001b[1;32mraise\u001b[0m \u001b[0mNameError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'HiThere'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;32mexcept\u001b[0m \u001b[0mNameError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'An exception flew by!'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[1;32mraise\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: HiThere"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    raise NameError('HiThere')\n",
    "except NameError:\n",
    "    print('An exception flew by!')\n",
    "    raise"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "#8.5. User-defined Exceptions\n",
    "class Error(Exception):\n",
    "    \"\"\"Base class for exceptions in this module.\"\"\"\n",
    "    pass\n",
    "\n",
    "class InputError(Error):\n",
    "    \"\"\"Exception raised for errors in the input.\n",
    "\n",
    "    Attributes:\n",
    "        expression -- input expression in which the error occurred\n",
    "        message -- explanation of the error\n",
    "    \"\"\"\n",
    "\n",
    "    def __init__(self, expression, message):\n",
    "        self.expression = expression\n",
    "        self.message = message\n",
    "\n",
    "class TransitionError(Error):\n",
    "    \"\"\"Raised when an operation attempts a state transition that's not\n",
    "    allowed.\n",
    "\n",
    "    Attributes:\n",
    "        previous -- state at beginning of transition\n",
    "        next -- attempted new state\n",
    "        message -- explanation of why the specific transition is not allowed\n",
    "    \"\"\"\n",
    "\n",
    "    def __init__(self, previous, next, message):\n",
    "        self.previous = previous\n",
    "        self.next = next\n",
    "        self.message = message"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Goodbye, world!\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-14-56de84cec0f0>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#8.6.Defining Clean-up Actions\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[1;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[1;32mfinally\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Goodbye, world!'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "#8.6.Defining Clean-up Actions\n",
    "try:\n",
    "    raise KeyboardInterrupt\n",
    "finally:\n",
    "    print('Goodbye, world!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KeyboardInterrupt"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "KeyboardInterrupt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Goodbye, world!\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-16-c182b08bab5b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m     \u001b[1;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;32mfinally\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Goodbye, world!'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "try:\n",
    "    raise KeyboardInterrupt\n",
    "finally:\n",
    "    print('Goodbye, world!')\n",
    "\n",
    "\n",
    "KeyboardInterrupt\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def bool_return():\n",
    "    try:\n",
    "        return True\n",
    "    finally:\n",
    "        return False\n",
    "\n",
    "bool_return()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "result is 2.0\n",
      "executing finally clause\n",
      "division by zero!\n",
      "executing finally clause\n",
      "executing finally clause\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for /: 'str' and 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-18-4f85d38980a2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     15\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     16\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 17\u001b[1;33m \u001b[0mdivide\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"2\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"1\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-18-4f85d38980a2>\u001b[0m in \u001b[0;36mdivide\u001b[1;34m(x, y)\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mdivide\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m         \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mx\u001b[0m \u001b[1;33m/\u001b[0m \u001b[0my\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m     \u001b[1;32mexcept\u001b[0m \u001b[0mZeroDivisionError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m         \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"division by zero!\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: unsupported operand type(s) for /: 'str' and 'str'"
     ]
    }
   ],
   "source": [
    "def divide(x, y):\n",
    "    try:\n",
    "        result = x / y\n",
    "    except ZeroDivisionError:\n",
    "        print(\"division by zero!\")\n",
    "    else:\n",
    "        print(\"result is\", result)\n",
    "    finally:\n",
    "        print(\"executing finally clause\")\n",
    "\n",
    "divide(2, 1)\n",
    "\n",
    "\n",
    "divide(2, 0)\n",
    "\n",
    "\n",
    "divide(\"2\", \"1\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unindent does not match any outer indentation level (<tokenize>, line 5)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<tokenize>\"\u001b[1;36m, line \u001b[1;32m5\u001b[0m\n\u001b[1;33m    with open(\"myfile.txt\") as f:\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unindent does not match any outer indentation level\n"
     ]
    }
   ],
   "source": [
    "#8.7. Predefined Clean-up Actions\n",
    "for line in open(\"myfile.txt\"):\n",
    "    print(line, end=\"\")\n",
    "    \n",
    "   with open(\"myfile.txt\") as f:\n",
    "    for line in f:\n",
    "        print(line, end=\"\") "
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
