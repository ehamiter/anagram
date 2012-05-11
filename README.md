anagram.py
==========

Anagram generator with several options to control the generated words

`usage: anagram.py [-h] -l LETTERS [-m MIN] [-s STARTS] [-e ENDS] [-r REQUIRED]`

mandatory agrument:

    -l, --letters  : Letters provided to generate an anagram

optional arguments:

    -h, --help     : show help message and exit 
    -m, --min      : Minimum amount of letters in anagram
    -s, --starts   : Generates words starting with this letter
    -e, --ends     : Generates words ending with this letter
    -r, --required : Generates words that must have this letter or letters
