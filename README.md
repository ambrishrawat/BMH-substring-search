# Apple Coding Test
This is an implmentation of the programming assignment defined in ProgrammingAssignment.pdf

Requirements
- Python 2.7.11

## Outline
The script `findCon.py` can be used to find which concepts are present in a given sentence.
```
python findCon.py --sen="Who does West Indian cuisine?" --fpath=./concepts.list
```
### `utils_asgn.py` 
This file contains implementation of Boyer-Moore-Horspool string search algorithm. The developed code is based on the pseudo-code available [here](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore%E2%80%93Horspool_algorithm#Description). A brute-force implementation of search using python string comparison operators is also available here. 

### `classes`
- `Sentence.py`: This class extends the python str class. Preprocessing steps like punctuation removal have been implemented in this class. It can be extended to include other meta deta for a sentence like *source language* etc. which can be later used for refined search. Sentence string is processed to lower case for comparison. Pre-defined python-functions have been used for punctuation removal and lower-case conversion.
- `Concept.py`: This class also extends the python str class. Additionaly, it also generated the look-up table used in Boyer-Moore-Horspool search algorithm. Conceptistring are also preprocessed to lower case for comparison.

## Assumptions
- It is assumed that the list of concepts are stored in a txt file with each line defining a new concept. 
- It is also asumed that there are no repitions in the list of concepts. (each instance will be seperately detected)
- It is assumed that file can fit into CPU memory. 

## Highlights
- 
