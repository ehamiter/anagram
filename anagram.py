import argparse
import sys


def anagramchk(word,chkword):
    for letter in word:
        if letter in chkword:
            chkword=chkword.replace(letter, '', 1)
        else:
            return 0
    return 1

parser = argparse.ArgumentParser(description='Anagram generator with several options to control the generated words')
parser.add_argument('-l','--letters', help='Letters provided to generate an anagram', required=True)
parser.add_argument('-m','--min', help='Minimum amount of letters in anagram', required=False)
parser.add_argument('-s','--starts', help='Generates words starting with this letter', required=False)
parser.add_argument('-e','--ends', help='Generates words ending with this letter', required=False)
parser.add_argument('-r','--required', help='Generates words that must have this letter or letters', required=False)
args = vars(parser.parse_args())

f=open('wordlist.txt', 'r')
words = []

for line in f:
    line=line.strip()

    if anagramchk(line,args['letters']):
        words.append(line)

        if args['min']:
            for word in words:
                if not len(word)>=int(args['min']):
                    words.remove(word)
            
        if args['starts']:
            for word in words:
                if word[0] != args['starts']:
                    words.remove(word)
        
        if args['ends']:
            for word in words:
                if word[-1] != args['ends']:
                    words.remove(word)

        if args['required']:
            for word in words:
                if args['required'] not in word:
                    words.remove(word)
    
for word in words:
    print word

f.close()