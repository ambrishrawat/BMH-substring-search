class Sentence(str):
    '''
    class for sentence

    the current implementation only extends python string class
    other meta data can be included like

    - source language
    -

    '''

    def __new__(cls, value, *args, **kwargs):
        print('Yoda',value)
        return super(Sentence, cls).__new__(cls, value)

