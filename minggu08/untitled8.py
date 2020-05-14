{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Template' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-8e91f1f01263>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mtime\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mphotofiles\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;34m'img_1074.jpg'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'img_1076.jpg'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'img_1077.jpg'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[1;32mclass\u001b[0m \u001b[0mBatchRename\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mTemplate\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m     \u001b[0mdelimiter\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'%'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mfmt\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Enter rename style (%d-date %n-seqnum %f-format):  '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'Template' is not defined"
     ]
    }
   ],
   "source": [
    "import time, os.path\n",
    "photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']\n",
    "class BatchRename(Template):\n",
    "    delimiter = '%'\n",
    "fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'BatchRename' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-15275ac657aa>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mt\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mBatchRename\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfmt\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mdate\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mtime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstrftime\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'%d%b%y'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfilename\u001b[0m \u001b[1;32min\u001b[0m \u001b[0menumerate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mphotofiles\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mbase\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mext\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msplitext\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilename\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[0mnewname\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msubstitute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0md\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdate\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mn\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mi\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mext\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'BatchRename' is not defined"
     ]
    }
   ],
   "source": [
    "t = BatchRename(fmt)\n",
    "date = time.strftime('%d%b%y')\n",
    "for i, filename in enumerate(photofiles):\n",
    "    base, ext = os.path.splitext(filename)\n",
    "    newname = t.substitute(d=date, n=i, f=ext)\n",
    "    print('{0} --> {1}'.format(filename, newname))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'myfile.zip'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-776aa47785f2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mstruct\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[1;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'myfile.zip'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'rb'\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m     \u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'myfile.zip'"
     ]
    }
   ],
   "source": [
    "#11.3. Working with Binary Data Record Layouts\n",
    "import struct\n",
    "\n",
    "with open('myfile.zip', 'rb') as f:\n",
    "    data = f.read()\n",
    "\n",
    "start = 0\n",
    "for i in range(3):                      # show the first 3 file headers\n",
    "    start += 14\n",
    "    fields = struct.unpack('<IIIHH', data[start:start+16])\n",
    "    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields\n",
    "\n",
    "    start += 16\n",
    "    filename = data[start:start+filenamesize]\n",
    "    start += filenamesize\n",
    "    extra = data[start:start+extra_size]\n",
    "    print(filename, hex(crc32), comp_size, uncomp_size)\n",
    "\n",
    "    start += extra_size + comp_size     # skip to the next header"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The main program continues to run in foreground.\n",
      "Main program waited until background was done.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Exception in thread Thread-6:\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\USER\\anaconda3\\lib\\threading.py\", line 926, in _bootstrap_inner\n",
      "    self.run()\n",
      "  File \"<ipython-input-4-f3935623ac96>\", line 12, in run\n",
      "    f.write(self.infile)\n",
      "  File \"C:\\Users\\USER\\anaconda3\\lib\\zipfile.py\", line 1730, in write\n",
      "    zinfo = ZipInfo.from_file(filename, arcname)\n",
      "  File \"C:\\Users\\USER\\anaconda3\\lib\\zipfile.py\", line 518, in from_file\n",
      "    st = os.stat(filename)\n",
      "FileNotFoundError: [WinError 2] The system cannot find the file specified: 'mydata.txt'\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#11.4. Multi-threading\n",
    "import threading, zipfile\n",
    "\n",
    "class AsyncZip(threading.Thread):\n",
    "    def __init__(self, infile, outfile):\n",
    "        threading.Thread.__init__(self)\n",
    "        self.infile = infile\n",
    "        self.outfile = outfile\n",
    "\n",
    "    def run(self):\n",
    "        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)\n",
    "        f.write(self.infile)\n",
    "        f.close()\n",
    "        print('Finished background zip of:', self.infile)\n",
    "\n",
    "background = AsyncZip('mydata.txt', 'myarchive.zip')\n",
    "background.start()\n",
    "print('The main program continues to run in foreground.')\n",
    "\n",
    "background.join()    # Wait for the background task to finish\n",
    "print('Main program waited until background was done.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING:root:Warning:config file server.conf not found\n",
      "ERROR:root:Error occurred\n",
      "CRITICAL:root:Critical error -- shutting down\n"
     ]
    }
   ],
   "source": [
    "#11.5. Logging\n",
    "import logging\n",
    "logging.debug('Debugging information')\n",
    "logging.info('Informational message')\n",
    "logging.warning('Warning:config file %s not found', 'server.conf')\n",
    "logging.error('Error occurred')\n",
    "logging.critical('Critical error -- shutting down')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#11.6. Weak References\n",
    "import weakref, gc\n",
    "class A:\n",
    "    def __init__(self, value):\n",
    "        self.value = value\n",
    "    def __repr__(self):\n",
    "        return str(self.value)"
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
       "10"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = A(10)                   # create a reference\n",
    "d = weakref.WeakValueDictionary()\n",
    "d['primary'] = a            # does not create a reference\n",
    "d['primary']                # fetch the object if it is still alive"
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
       "96"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "del a                       # remove the one reference\n",
    "gc.collect()                # run garbage collection right away\n"
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
       "10"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d['primary']                # entry was automatically removed\n"
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
       "26932"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#11.7. Tools for Working with Lists\n",
    "from array import array\n",
    "a = array('H', [4000, 10, 700, 22222])\n",
    "sum(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array('H', [10, 700])"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a[1:3]\n"
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
      "Handling task1\n"
     ]
    }
   ],
   "source": [
    "from collections import deque\n",
    "d = deque([\"task1\", \"task2\", \"task3\"])\n",
    "d.append(\"task4\")\n",
    "print(\"Handling\", d.popleft())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import bisect\n",
    "scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]\n",
    "bisect.insort(scores, (300, 'ruby'))\n",
    "scores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[-5, 0, 1]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from heapq import heapify, heappop, heappush\n",
    "data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]\n",
    "heapify(data)                      # rearrange the list into heap order\n",
    "heappush(data, -5)                 # add a new entry\n",
    "[heappop(data) for i in range(3)]  # fetch the three smallest entries\n"
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
       "Decimal('0.74')"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#11.8. Decimal Floating Point Arithmetic\n",
    "from decimal import *\n",
    "round(Decimal('0.70') * Decimal('1.05'), 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.73"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "round(.70 * 1.05, 2)"
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
       "Decimal('0.00')"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Decimal('1.00') % Decimal('.10')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.09999999999999995"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "1.00 % 0.10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum([Decimal('0.1')]*10) == Decimal('1.0')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum([0.1]*10) == 1.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Decimal('0.142857142857142857142857142857142857')"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "getcontext().prec = 36\n",
    "Decimal(1) / Decimal(7)"
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
