anagram.py
==========

Anagram generator with several options to control the generated words

`usage: anagram.py [-h] -l LETTERS [-m MIN] [-s STARTS] [-e ENDS] [-r REQUIRED]`

mandatory agrument:

    -l, --letters  : Letters provided to generate an anagram

optional arguments:

    -h, --help      : show help message and exit 
    -m, --min       : Minimum amount of letters in anagram
    -s, --starts    : Generates words starting with this letter
    -e, --ends      : Generates words ending with this letter
    -r, --required  : Generates words that must have this letter or letters
    --limit         : The maximum number of words you want to see (Default: unlimited)
    -u, --unordered : Leave the output in alphabetical order

example:

    $ python anagram.py -l reetyquiop -m 4 -s r -r q
    
    reequip
    requite
    roquet
    roque

anagram-repl.py
===============

Anagram generator that continues to run and allows for reuse

`usage: anagram-repl.py [-h] [-m MIN] [-u] [--limit LIMIT]`

Anagram generator that continues to run and allows for reuse

optional arguments:
  -h, --help         show this help message and exit
  -m MIN, --min MIN  Minimum amount of letters in anagram, can be overwritten
                     in the REPL
  -u, --unordered    Leave the output in alphabetical order
  --limit LIMIT      The maximum number of words you want to see

Once in the REPL you will be prompted repeatedly until you type `exit`
The input needs to be of the following format
`[-s STARTS] [-e ENDS] [-m MIN] letters [required]`

positional arguments:
  letters               Letters provided to generate an anagram
  required              Generates words that must have this letter or letters

optional arguments:
  -s STARTS, --starts STARTS
                        Generates words starting with this letter
  -e ENDS, --ends ENDS  Generates words ending with this letter
  -m MIN, --min MIN     Minimum amount of letters in anagram

anagram-gui.py
==============

Anagram generator with a GUI for alternative input methods using easygui

![Anagram-gui screenshot](https://github.com/ehamiter/anagram/raw/master/anagram-gui.png "Anagram GUI")

Requires `easygui` which can be obtained from [http://easygui.sourceforge.net/download/index.html](http://easygui.sourceforge.net/download/index.html)
