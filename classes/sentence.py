import string
class Sentence(str):
    '''
    class for sentence

    the current implementation only extends python string class
    other meta data can be included like

    - source language
    -

    '''

    def __new__(cls, value, *args, **kwargs):
        return super(Sentence, cls).__new__(cls, value)


    def __init__(self,value):
        self.str_ = Sentence.process_sen(value)

    def get_orig_str(self):
        return self

    def get_str(self):
        return self.str_

    @staticmethod
    def process_sen(sen=None):
	'''
	Function to preprocess a sentence
	'''


	#remove punctuations
	sen = sen.translate(None, string.punctuation)

	'''
	Time comparison across different approaches
	http://stackoverflow.com/a/266162
	'''

	#remove > 2 whitespace
	sen = " ".join(sen.split())

	return sen.lower()
