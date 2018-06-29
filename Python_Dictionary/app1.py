import json
import os
import difflib 
path = '\\Users\\pc\\Desktop'
os.chdir(path)
data = json.load(open('data.json'))


def translate(word):
    word_matched = difflib.get_close_matches(word , data.keys())
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: 
        return data[word.title()]
    if word.upper() in data:
        return data[word.upper()]
    elif len(word_matched) > 0:
        yn = input("Did you mean %s instead , Enter Y or N" % word_matched[0])
        if yn == 'Y':
            return data[word_matched[0]]
        elif yn == 'N':
            return('this word does not exist')
        
    else:
        return('this word does not exist')
    

word = input('enter a word:')

output =translate(word)


if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
