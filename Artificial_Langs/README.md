# At the Boundaries of Syntactic Prehistory - Artificial Languages

The folder contains the following files:

1. **split.txt**: this file contains the main dataset, but a comma is used to mark family boundaries.

2. **getvalues.py.**: by calling ```python3 getvalues.py split.txt```, we can retrieve the ratio of ```+``` at each parameter for the entire dataset, weighted by family.

3. **sampling.py**: this script is used to create a list of Artificial Distances from a number of artificial languages. It takes the number of languages from which artificial distances are drawn as an argument: ```python3 sampling.py n_langs```.

4. **random_langs.txt**: the output of the preceding function with ```n_langs=5000```.
