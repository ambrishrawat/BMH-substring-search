def make_Bad_Char_SR_table(value):
    pass


class Concept(str):
    '''
    class for Concept

    the current implementation only extends python string class
    other meta data can be included like

    - source language
    - other structure that relates it to concepts like via a knowledge graph/ontology
    - this also allows for adding preprcessing steps eg. shift rules in BMSearch

    '''

    def __new__(cls, value, *args, **kwargs):
        return super(Concept, cls).__new__(cls, value)


    def __init__(self, value):
        self.badCharacterShiftRule = make_Bad_Char_SR_table(value)
        self.goodSuffixRule = make_Bad_Char_SR_table(value)

