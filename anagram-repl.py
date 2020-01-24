import argparse
import readline


def anagramchk(word,chkword):
    for letter in word:
        if letter in chkword:
            chkword=chkword.replace(letter, '', 1)
        else:
            return 0
    return 1

def has_all_required(word,required):
    for letter in required:
        if letter not in word:
            return False
        word = word.replace(letter, '', 1)
    return True

def solve(word_list, params, opts):
    words = []

    for word in word_list:
        if opts['limit'] and len(words) >= opts['limit']:
            break

        if (params['min'] or opts['min']) and not len(word)>=int(params['min'] or opts['min']):
            continue

        if params['starts'] and word[0] != params['starts']:
            continue

        if params['ends'] and word[-1] != params['ends']:
            continue

        if params['required'] and not has_all_required(word, params['required']):
            continue

        if anagramchk(word,params['letters']):
            words.append(word)
        
    for word in words:
        print(word)

run_parser = argparse.ArgumentParser(description='Anagram generator that continues to run and allows for reuse')
run_parser.add_argument('-m','--min', help='Minimum amount of letters in anagram, can be overwritten in the REPL', required=False)
run_parser.add_argument('-u', '--unordered', action='store_true', help='Leave the output in alphabetical order', required=False)
run_parser.add_argument('--limit', help='The maximum number of words you want to see', default=0, type=int, required=False)
args = vars(run_parser.parse_args())

prompt_parser = argparse.ArgumentParser(prog='')
prompt_parser.add_argument('-s','--starts', help='Generates words starting with this letter', required=False)
prompt_parser.add_argument('-e','--ends', help='Generates words ending with this letter', required=False)
prompt_parser.add_argument('-m','--min', help='Minimum amount of letters in anagram', required=False)
prompt_parser.add_argument('letters', metavar='letters', help='Letters provided to generate an anagram')
prompt_parser.add_argument('required', metavar='required', nargs='?', help='Generates words that must have this letter or letters')


all_words = []
f=open('wordlist.txt', 'r')
for line in f:
    all_words.append(line.strip())
f.close()
if not args['unordered']:
    all_words.sort(key=len, reverse=True)

while True:
    text = input("--> ").lower()
    if text == "exit":
        break
    if text == "help":
        prompt_parser.parse_args('-h'.split())
        continue
    promt_params = vars(prompt_parser.parse_args(text.split()))
    solve(all_words, promt_params, args)
