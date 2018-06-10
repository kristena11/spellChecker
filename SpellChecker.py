import re, string

def readRef():
    ref = open('ref.txt')
    
    lines = ref.readlines()
  
    refDictionary = {}
    key = 0
    
    for line in lines:
        key = key + 1
        values = line.strip()
        values = values.lstrip(' ')
        refDictionary[int(key)] = values
    
    
    return refDictionary
    
def userPrompt():
    while True:
        inputFile = input('Input file name: ')
        try:
            fd = open(inputFile)
            return fd
            
        except:
            print('unable to open file' + inputFile)
            continue
    
def readSample(fd):
    match_pattern = fd.read().split()
    
    frequency  = {}
    
    for word in match_pattern:
        word = word.lower()
        word = re.sub('[%s]' % re.escape(string.punctuation), '', word)
        word  = word.lstrip('0123456789 ')
        
        if word.strip() == "":
            continue
            
        count = frequency.get(word,0)
        frequency[word] = count + 1
     
    wordDictionary ={}  
    frequency_list = frequency.keys()
    
    for words in frequency_list:
        key = words
        values = frequency[words]
        wordDictionary[str(key)] = values
        
    return(wordDictionary)

def spellCheck(refDictionary, wordDictionary):
    print(refDictionary.values())    
    for value in wordDictionary:
        #print(value)
        #print(refDictionary.values()) 
        if value not in refDictionary.values():
            print(' misspelled word ' + value)

        
   
   
def wordPrompt(wordDictionary):
    while True:
        inputWord = input('enter word to get word count: ')
        if inputWord in wordDictionary:
            value = str(wordDictionary.get(inputWord))
            print('The word ' + inputWord + ' is repeated ' + value + ' times')
            break
            
        else:
            print('Word not in file')
            continue
  
def main():
    refDictionary = readRef()
    fd = userPrompt()
    wordDictionary = readSample(fd)
    spellCheck(refDictionary, wordDictionary)
    wordPrompt(wordDictionary)
    
main()