{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-1-a1b356ede6c6>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-1-a1b356ede6c6>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    python3 -m venv tutorial-env\u001b[0m\n\u001b[1;37m                  ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "python3 -m venv tutorial-env"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-2-95460c314efd>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-2-95460c314efd>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    $ source ~/envs/tutorial-env/bin/activate\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "$ source ~/envs/tutorial-env/bin/activate\n",
    "(tutorial-env) $ python\n",
    "Python 3.5.1 (default, May  6 2016, 10:59:36)\n",
    "  ...\n",
    ">>> import sys\n",
    ">>> sys.path\n",
    "['', '/usr/local/lib/python35.zip', ...,\n",
    "'~/envs/tutorial-env/lib/python3.5/site-packages']\n",
    ">>>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-3-097898b44c3e>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-3-097898b44c3e>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    (tutorial-env) $ pip install novas\u001b[0m\n\u001b[1;37m                   ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "(tutorial-env) $ pip install novas\n",
    "Collecting novas\n",
    "  Downloading novas-3.1.1.3.tar.gz (136kB)\n",
    "Installing collected packages: novas\n",
    "  Running setup.py install for novas\n",
    "Successfully installed novas-3.1.1.3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-4-d146f7e084c4>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-4-d146f7e084c4>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    (tutorial-env) $ pip install requests==2.6.0\u001b[0m\n\u001b[1;37m                   ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "(tutorial-env) $ pip install requests==2.6.0\n",
    "Collecting requests==2.6.0\n",
    "  Using cached requests-2.6.0-py2.py3-none-any.whl\n",
    "Installing collected packages: requests\n",
    "Successfully installed requests-2.6.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-5-dcb01a2557a3>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-5-dcb01a2557a3>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    (tutorial-env) $ pip install --upgrade requests\u001b[0m\n\u001b[1;37m                   ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "(tutorial-env) $ pip install --upgrade requests\n",
    "Collecting requests\n",
    "Installing collected packages: requests\n",
    "  Found existing installation: requests 2.6.0\n",
    "    Uninstalling requests-2.6.0:\n",
    "      Successfully uninstalled requests-2.6.0\n",
    "Successfully installed requests-2.7.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-6-f70cf3613c62>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-6-f70cf3613c62>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    (tutorial-env) $ pip list\u001b[0m\n\u001b[1;37m                   ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "(tutorial-env) $ pip list\n",
    "novas (3.1.1.3)\n",
    "numpy (1.9.2)\n",
    "pip (7.0.3)\n",
    "requests (2.7.0)\n",
    "setuptools (16.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-7-e9d56e1be9b6>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-7-e9d56e1be9b6>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    (tutorial-env) $ pip freeze > requirements.txt\u001b[0m\n\u001b[1;37m                   ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "(tutorial-env) $ pip freeze > requirements.txt\n",
    "(tutorial-env) $ cat requirements.txt\n",
    "novas==3.1.1.3\n",
    "numpy==1.9.2\n",
    "requests==2.7.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-8-61dd63f9026b>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-8-61dd63f9026b>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    (tutorial-env) $ pip install -r requirements.txt\u001b[0m\n\u001b[1;37m                   ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "(tutorial-env) $ pip install -r requirements.txt\n",
    "Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))\n",
    "  ...\n",
    "Collecting numpy==1.9.2 (from -r requirements.txt (line 2))\n",
    "  ...\n",
    "Collecting requests==2.7.0 (from -r requirements.txt (line 3))\n",
    "  ...\n",
    "Installing collected packages: novas, numpy, requests\n",
    "  Running setup.py install for novas\n",
    "Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0"
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
