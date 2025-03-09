import json
from difflib import get_close_matches
def meaning(word):
    if word in data:
        output=data[word]
    elif word.title() in data:
        output= data[word.title()]
    elif word.capitalize() in data:
        output= data[word.capitalize()]
    elif word.upper() in data:
        output= data[word.upper()]
    elif word!=data.keys():
        word=get_close_matches(word,data.keys())[0]
        print(f"Did you mean {word}?")
        decide=input("Enter y or n")
        if decide=='y':
            output=data[word]
        elif decide=='n':
            output="word not found"
        else:
            output='entered wrong input'
    else:
        output="You have enterd incorrect data"
    return output
    
data = json.load(open(r"data\d1\Worddictionary\data.json"))
word=input("Enter the word to find the meaning of it\n")

output=meaning(word.lower())
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)