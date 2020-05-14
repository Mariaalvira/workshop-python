{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Results of the 2016 Referendum'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#7.1. Fancier Output Formatting\n",
    "year = 2016\n",
    "event = 'Referendum'\n",
    "f'Results of the {year} {event}'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' 42572654 YES votes  49.67%'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "yes_votes = 42_572_654\n",
    "no_votes = 43_132_495\n",
    "percentage = yes_votes / (yes_votes + no_votes)\n",
    "'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello, world.'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = 'Hello, world.'\n",
    "str(s)"
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
       "\"'Hello, world.'\""
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "repr(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'0.14285714285714285'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str(1/7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The value of x is 32.5, and y is 40000...\n"
     ]
    }
   ],
   "source": [
    "x = 10 * 3.25\n",
    "y = 200 * 200\n",
    "s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'\n",
    "print(s)"
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
      "'hello, world\\n'\n"
     ]
    }
   ],
   "source": [
    "# The repr() of a string adds string quotes and backslashes:\n",
    "hello = 'hello, world\\n'\n",
    "hellos = repr(hello)\n",
    "print(hellos)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"(32.5, 40000, ('spam', 'eggs'))\""
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# The argument to repr() may be any Python object:\n",
    "repr((x, y, ('spam', 'eggs')))\n"
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
      "The value of pi is approximately 3.142.\n"
     ]
    }
   ],
   "source": [
    "#7.1.1. Formatted String Literals\n",
    "import math\n",
    "print(f'The value of pi is approximately {math.pi:.3f}.')\n"
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
      "Sjoerd     ==>       4127\n",
      "Jack       ==>       4098\n",
      "Dcab       ==>       7678\n"
     ]
    }
   ],
   "source": [
    "table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}\n",
    "for name, phone in table.items():\n",
    "    print(f'{name:10} ==> {phone:10d}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My hovercraft is full of eels.\n",
      "My hovercraft is full of 'eels'.\n"
     ]
    }
   ],
   "source": [
    "animals = 'eels'\n",
    "print(f'My hovercraft is full of {animals}.')\n",
    "\n",
    "print(f'My hovercraft is full of {animals!r}.')\n"
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
      "We are the knights who say \"Ni!\"\n"
     ]
    }
   ],
   "source": [
    "#7.1.2. The String Format() Method\n",
    "print('We are the {} who say \"{}!\"'.format('knights', 'Ni'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "spam and eggs\n"
     ]
    }
   ],
   "source": [
    "print('{0} and {1}'.format('spam', 'eggs'))\n"
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
      "eggs and spam\n"
     ]
    }
   ],
   "source": [
    "print('{1} and {0}'.format('spam', 'eggs'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This spam is absolutely horrible.\n"
     ]
    }
   ],
   "source": [
    "print('This {food} is {adjective}.'.format(\n",
    "      food='spam', adjective='absolutely horrible'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The story of Bill, Manfred, and Georg.\n"
     ]
    }
   ],
   "source": [
    "print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))"
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
      "Jack: 4098; Sjoerd: 4127; Dcab: 8637678\n"
     ]
    }
   ],
   "source": [
    "table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}\n",
    "print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '\n",
    "      'Dcab: {0[Dcab]:d}'.format(table))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jack: 4098; Sjoerd: 4127; Dcab: 8637678\n"
     ]
    }
   ],
   "source": [
    "table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}\n",
    "print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " 1   1    1\n",
      " 2   4    8\n",
      " 3   9   27\n",
      " 4  16   64\n",
      " 5  25  125\n",
      " 6  36  216\n",
      " 7  49  343\n",
      " 8  64  512\n",
      " 9  81  729\n",
      "10 100 1000\n"
     ]
    }
   ],
   "source": [
    "for x in range(1, 11):\n",
    "    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " 1   1    1\n",
      " 2   4    8\n",
      " 3   9   27\n",
      " 4  16   64\n",
      " 5  25  125\n",
      " 6  36  216\n",
      " 7  49  343\n",
      " 8  64  512\n",
      " 9  81  729\n",
      "10 100 1000\n"
     ]
    }
   ],
   "source": [
    "#7.1.3. Manual String Formatting\n",
    "for x in range(1, 11):\n",
    "    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')\n",
    "    # Note use of 'end' on previous line\n",
    "    print(repr(x*x*x).rjust(4))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'00012'"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'12'.zfill(5)"
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
       "'-003.14'"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'-3.14'.zfill(7)"
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
       "'3.14159265359'"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'3.14159265359'.zfill(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The value of pi is approximately 3.142.\n"
     ]
    }
   ],
   "source": [
    "#7.1.4. Old string formatting\n",
    "import math\n",
    "print('The value of pi is approximately %5.3f.' % math.pi)\n"
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
       "True"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#7.2. Reading and Writing Files\n",
    "f = open('workfile', 'w')\n",
    "\n",
    "with open('workfile') as f:\n",
    "    read_data = f.read()\n",
    "\n",
    "# We can check that the file has been automatically closed.\n",
    "f.closed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-27-bf012af3c351>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclose\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    "f.close()\n",
    "f.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-29-95996948eba0>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#7.2.1. Methods of file objects\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    "#7.2.1. Methods of file objects\n",
    "f.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-30-7e1d2e12b839>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreadline\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    " f.readline()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-31-7e1d2e12b839>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreadline\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    "f.readline()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-32-7e1d2e12b839>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreadline\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    "f.readline()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-33-f25c033ac067>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfor\u001b[0m \u001b[0mline\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mline\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m''\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    "for line in f:\n",
    "    print(line, end='')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-34-cc42235461d2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'This is a test\\n'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    "f.write('This is a test\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "I/O operation on closed file.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-35-ed08d1bc4d2e>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mvalue\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;34m'the answer'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m42\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0ms\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalue\u001b[0m\u001b[1;33m)\u001b[0m  \u001b[1;31m# convert the tuple to string\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwrite\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: I/O operation on closed file."
     ]
    }
   ],
   "source": [
    "value = ('the answer', 42)\n",
    "s = str(value)  # convert the tuple to string\n",
    "f.write(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'[1, \"simple\", \"list\"]'"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#7.2.2. Saving structured data with json\n",
    "import json\n",
    "json.dumps([1, 'simple', 'list'])"
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
