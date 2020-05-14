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
       "datetime.date(2020, 5, 11)"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#10.8. Dates and Times\n",
    "# dates are easily constructed and formatted\n",
    "from datetime import date\n",
    "now = date.today()\n",
    "now"
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
       "'05-11-20. 11 May 2020 is a Monday on the 11 day of May.'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "now.strftime(\"%m-%d-%y. %d %b %Y is a %A on the %d day of %B.\")\n"
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
       "20373"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# dates support calendar arithmetic\n",
    "birthday = date(1964, 7, 31)\n",
    "age = now - birthday\n",
    "age.days"
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
       "41"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#10.9. Data Compression\n",
    "import zlib\n",
    "s = b'witch which has which witches wrist watch'\n",
    "len(s)"
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
       "37"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t = zlib.compress(s)\n",
    "len(t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "b'witch which has which witches wrist watch'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zlib.decompress(t)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "226805979"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zlib.crc32(s)\n"
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
       "0.32839387100000295"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#10.10. Performance Measurement\n",
    "from timeit import Timer\n",
    "Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.3349648880000018"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Timer('a,b = b,a', 'a=1; b=2').timeit()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "TestResults(failed=0, attempted=1)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#10.11. Quality Control\n",
    "def average(values):\n",
    "    \"\"\"Computes the arithmetic mean of a list of numbers.\n",
    "\n",
    "    >>> print(average([20, 30, 70]))\n",
    "    40.0\n",
    "    \"\"\"\n",
    "    return sum(values) / len(values)\n",
    "\n",
    "import doctest\n",
    "doctest.testmod()   # automatically validate the embedded tests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "E\n",
      "======================================================================\n",
      "ERROR: C:\\Users\\USER\\AppData\\Roaming\\jupyter\\runtime\\kernel-5b253d7e-36a3-48e6-a464-ddb978bd3f8a (unittest.loader._FailedTest)\n",
      "----------------------------------------------------------------------\n",
      "AttributeError: module '__main__' has no attribute 'C:\\Users\\USER\\AppData\\Roaming\\jupyter\\runtime\\kernel-5b253d7e-36a3-48e6-a464-ddb978bd3f8a'\n",
      "\n",
      "----------------------------------------------------------------------\n",
      "Ran 1 test in 0.025s\n",
      "\n",
      "FAILED (errors=1)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "True",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m True\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\USER\\anaconda3\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3339: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "import unittest\n",
    "\n",
    "class TestStatisticalFunctions(unittest.TestCase):\n",
    "\n",
    "    def test_average(self):\n",
    "        self.assertEqual(average([20, 30, 70]), 40.0)\n",
    "        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)\n",
    "        with self.assertRaises(ZeroDivisionError):\n",
    "            average([])\n",
    "        with self.assertRaises(TypeError):\n",
    "            average(20, 30, 70)\n",
    "\n",
    "unittest.main()  # Calling from the command line invokes all tests"
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
