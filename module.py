""" 
@param is the string word we want to process
@return string pascalized word
"""
def pascalize(word):
    if(len(word) == 0 or type(word) != str):
        return False
    newWord = word.replace('_',' ')
    newWord = newWord.title()
    return newWord.replace(' ','')

"""
@param is the string word we want to process
@return string depascalized word
"""
def depascalize(word):
    if(len(word) == 0 or type(word) != str):
        return False
    current = 0
    first = 0
    holder = []
    word = word[0].lower() + word[1:]
    for i in word:
        if(i.isupper() == True):
            newWord = word[first].lower() + word[first + 1:current]
            holder.append(newWord)
            first = current
        current+=1
    if(word[first].isupper() == True):
        newWord = word[first].lower() + word[first + 1:]
        holder.append(newWord)
    return "_".join(holder)
"""
@param is the string word we want to process
@return string camelized word
"""
def camelize(word):
    if(len(word) == 0 or type(word) != str):
        return False
    counter = 0
    indexHolder = []
    for i in word:
        if(i.isspace() == True):
            indexHolder.append(counter + 1)
        counter+=1
    wordList = list(word)
    wordList[0] = wordList[0].lower()
    for i in indexHolder:
        wordList[i] = wordList[i].upper()
    return "".join(wordList).replace(" ","")
"""
@param is the string word we want to check whether pascalized or not
@return bool correction value
"""
def is_pascalize(word):
    if(len(word) == 0 or type(word) != str):
        return False
    newWord = depascalize(word)
    return word == pascalize(newWord)
"""
@param is the string word we want to check whether pascalized or not
@return bool correction value
"""
def is_camelcase(word):
    if(len(word) == 0 or type(word) != str):
        return False
    return word == camelize(word)
"""
@param is the string word we want to check whether pascalized or not
@return bool correction value
"""
def is_snakecase(word):
    if(len(word) == 0 or type(word) != str):
        return False
    newWord = pascalize(word)
    return word == depascalize(newWord)

    