import string

def process_sen(sen=None):
    '''
    Function to preprocess a sentence 

    Args:
        sen : a sentence string

    Return:
        processed sentence
        (as string is an immutable objec (call-by-value), a new sring is returned)
    '''
    
    
    #remove punctuations
    sen = sen.translate(None, string.punctuation)

    '''
    Time comparison across different approaches 
    http://stackoverflow.com/a/266162
    '''

    #remove > 2 whitespace
    sen = " ".join(sen.split())
    
    return sen

def naivePythonComparison(sen=None,
        concept=None):

    '''
    Brute-force implemenation using python string comparison 
    '''
    sen = sen.lower()
    concept_pr = concept.lower()

    if concept_pr in sen:
        return True
    else:
        return False



