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

anagram-gui.py
==============

Anagram generator with a GUI for alternative input methods using easygui

![Anagram-gui screenshot](https://github.com/ehamiter/anagram/raw/master/anagram-gui.png "Anagram GUI")

Requires `easygui` which can be obtained from [http://easygui.sourceforge.net/download/index.html](http://easygui.sourceforge.net/download/index.html)
