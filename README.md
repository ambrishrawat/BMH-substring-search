# Apple Coding Test
This is an implmentation of the programming assignment defined in ProgrammingAssignment.pdf

Requirements
- Python 2.7.11

## Outline
The script `findCon.py` can be used to find which concepts are present in a given sentence.
```
python findCon.py --sen="Who does west indian cuisine?" --fpath=./concepts.list
```
sample output:
```
Indian
West Indian
```
### `utils_asgn.py` 
This file contains implementation of Boyer-Moore-Horspool string search algorithm. The developed code is based on the pseudo-code available [here](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore%E2%80%93Horspool_algorithm#Description). A brute-force implementation of search using python string comparison operators is also available here. 

### `classes`
- `Sentence.py`: This class extends the python str class. Preprocessing steps like punctuation removal have been implemented in this class. It can be extended to include other meta deta for a sentence like *source language* etc. which can be later used for refined search. Sentence string is processed to lower case for comparison. Pre-defined python-functions have been used for punctuation removal and lower-case conversion.
- `Concept.py`: This class also extends the python str class. Additionaly, it also generated the look-up table used in Boyer-Moore-Horspool search algorithm. Conceptistring are also preprocessed to lower case for comparison.

### `tests.py`
This file contains some basic unti tests for the search algorithms.


## Assumptions
- It is assumed that the list of concepts are stored in a txt file with each line defining a new concept. 
- It is also asumed that there are no repitions in the list of concepts. (each instance will be seperately detected)
- It is assumed that file can fit into CPU memory. 

## Highlights
- The developed code can be easily extended to add new search algorithms
- In the current implementation of Boyer-Moore-Horspool algorithm, the worst case search is O(nm), where n is the lenth of the pattern string and m is the length of the text string.
- As a table is stored for each of the pattern, the space complexity of this implementation is high. However, this needn't be performed on-the-fly, as has been crudely implemented in this case. 
- As the number of concepts can run into millions, data parallelism has been implemented. A proof-of-concept is available in `run_multip` function of the `findCon.py` script.
- The single-process implemetation is also based on the map-reduce paradign where the search funtion is mapped across concepts and then the successfull searches are later collected. Python filter function has been used to carry these two steps jointly.
- The output from cProfile is avaialable in `profiler.output`

## Suggested extensions

The problem statement, as mentioned in the pdf, has a multitide of other dimensions, most of which are beyond the scope of this implementation. THe following lists suggests some incremental updates for improvising the system. 
 
- This code doesn't take into account any structure in sentence or concept. All concepts are dealt with idependently. 
- Instead of looking at each concept independently, some sore of similarity can be captured while iterating to next *more liely* concept. This could be structural similarity like common-substring or semantic similarity as extracted from ontologies/knowledge bases. 
- Large-scale databases can also be used at backend when the number of concepts run in millions. 
- The more general Boyer-Moore algirithm can be used for string matching. It will require additional preprocessing. This however can be a part of one-time preprcessing while building an ontology of concepts. This algorithm is known to be advantageous when the same needle is searched for multiple times in different haystacks.

**NOTE: ** A total of 4 hours were spent on this coding assignment
