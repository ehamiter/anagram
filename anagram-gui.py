# requires easygui, which you can obtain from http://easygui.sourceforge.net/download/index.html

import easygui as eg
import sys


while 1:

    title = "Anagram Generator"
    msg = "Enter letters and options below"
    fieldNames = ["Letters (required)","Minimum length of words","Starts with letter","Ends with letter","Required letter(s) in words"]
    fieldValues = []
    fieldValues = eg.multenterbox(msg,title, fieldNames)

    def anagramchk(word,chkword):
        for letter in word:
            if letter in chkword:
                chkword=chkword.replace(letter, '', 1)
            else:
                return 0
        return 1

    f=open('wordlist.txt', 'r')
    words = []

    for line in f:
        line=line.strip()

        if anagramchk(line,fieldValues[0]):
            words.append(line+'\n')

            if fieldValues[1]:
                for word in words:
                    if not len(word)>int(fieldValues[1]):
                        words.remove(word)
                
            if fieldValues[2]:
                for word in words:
                    if word[0] != fieldValues[2]:
                        words.remove(word)
            
            if fieldValues[3]:
                for word in words:
                    if word[-1] != fieldValues[3]:
                        words.remove(word)

            if fieldValues[4]:
                for word in words:
                    if fieldValues[4] not in word:
                        words.remove(word)

    f.close()
  
    eg.textbox("Generated words using letters '%s'" % fieldValues[0], "Anagram Results", words)

    msg = "Do you want to generate more anagrams?"
    title = "Please confirm"
    if eg.ccbox(msg, title):
        pass
    else:
        sys.exit(0)
