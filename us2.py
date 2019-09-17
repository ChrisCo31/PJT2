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

def associate_f_dict(file, dict):
#associate file name to the word/occurrence dictionnary. Returns a dictionnary
    dict_textresult = {}
    dict_textresult[file] = dict
    return dict_textresult

def user_stat(myfiles,wordlist):
    #returns the list of uploaded files of the user, with the research results
    user_results = []
    for file in myfiles:
        r_clean = clean_text(file)
        r_search = search_w_t(wordlist, r_clean)
        r_associate = associate_f_dict(file,r_search)
        user_results.append(r_associate)
    return user_results

myfiles = ['data/text.txt', 'data/text2.txt']
wordlist = ['accord', 'fisc', 'moteur', 'grâce']
user_results = []
user_results = user_stat (myfiles, wordlist)

print (user_results)