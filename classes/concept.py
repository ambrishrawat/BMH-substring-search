class Concept(str):
    '''
    class for Concept

    the current implementation only extends python string class
    other meta data can be included like

    - source language (ENG/FRN/GER...)
    - other structure that relates it to concepts like via a knowledge graph/ontology
    - this also allows for adding preprcessing steps eg. shift rules in BMSearch

    '''

    def __new__(cls, value, *args, **kwargs):
        return super(Concept, cls).__new__(cls, value)


    def __init__(self, value):
        self.str_ = value.lower() #any other preprocessing can be added
        self.BMHsearch_Table = Concept.preprocess_table(self.str_)

    def get_str(self):
        return self.str_

    def get_orig_str(self):
        return self

    @staticmethod
    def preprocess_table(pattern):
        '''
        This has been adopted from the Wikipedia page for 
        Boyer Moore HorspoolAlgorithm
        '''
	len_p = len(pattern)

      	T = []
	for _ in range(256): 
            T.append(len_p)

	for i in range(len_p - 1): 
            T[ord(pattern[i])] = len_p - i - 1
	
        return T
    
