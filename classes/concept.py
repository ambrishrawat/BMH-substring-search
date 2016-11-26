class Concept(str):
    '''
    class for Concept

    the current implementation only extends python string class
    other meta data can be included like

    - source language
    - other structure that relates it to concepts like via a knowledge graph

    '''

    def __new__(cls, value, *args, **kwargs):
        return super(Concept, cls).__new__(cls, value)

    

