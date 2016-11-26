def search(sen=None,
        con_list=None):
    '''
    wrapper for seacrhing a list of concepts in a sentence
    Args:
        sen: a Sentence object
        con_list : a list of Concept objects
    Returns:
        list of concepts found in the Setence object.
        Returns an empty list, if no concepts are found
    '''
    if con_list is not None:
        con_in_sen = filter(lambda concept: search_(sen,concept),con_list)
        return con_in_sen
    else:
        return []



def search_(sen=None,
        concept=None):
    '''
    wrapper for search a concept-string in a sen-string

    This is the place to incorporate new search algorithms
    '''
    sen = sen.get_str()
    concept_pr = concept.get_str()
    T = concept.BMHsearch_Table

    return BMHSearch(text=sen,
            pattern=concept_pr,
            T=T)
    
def BruteForce(text=None,
        pattern=None):
    '''
    Brute-force implemenation using python string comparison 
    '''
    if pattern in text:
        return True
    else:
        return False


def BMHSearch(text=None,
        pattern=None,
        T=None):
    '''
    The code has been developed based on the pseudocode on Wikipedia page for
    Boyer Moore Horspool algorithm
    '''
    skip = 0
    len_text = len(text)
    len_pattern = len(pattern)
    while len_text - skip >= len_pattern:
        i = len_pattern - 1
        while text[skip+i] == pattern[i]:
            if i == 0:
                return True
            i = i - 1
        skip += T[ord(text[skip + len_pattern - 1])]    
    return False
   

def BMSearch(sen=None,
        con=None):
    return NotImplementedError()
