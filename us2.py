import datetime
import json

def clean_text(file):
    #Function which cleans the text of the file in parameter
    with open(file, 'r') as text:
        text_read = text.read()
        text_lower = text_read.lower()
        text_clean = text_lower.replace(',', ' ')
        #whole words are not compared, so the word "cherche" counts for 1 occurence in the word "recherches" 
    return (text_clean)

def search_w_t(wordlist, text_clean):
#searches for occurrences of a word list in a text that has been previously cleaned. Returns: word/occurrence dictionary
    # ordonnated dictionnary
    dict_w_o = {}
    for word in wordlist:
        occur = text_clean.count(word)
        dict_w_o[word] = occur
    #print (dict_w_o)
    return dict_w_o


myfiles = 'data/text.txt'
wordlist = ['accord', 'fisc', 'moteur', 'grâce']


def retrieve_data(file, dict_w_o):
#create the whole dictionary (python object) in the same dataformat as the dynamodb
    dict_data = {
        "user" : "chrisco",
        "text" : file,
        "date": datetime.datetime.today().strftime('%Y-%m-%d'),
        "words" : dict_w_o
    }
    return dict_data

def put_item(dict_data):
    return json.dump(dict_data)


c=clean_text(myfiles)
s=search_w_t(wordlist, c)
p=retrieve_data(myfiles,s)
j=put_item(p)
print (p)
