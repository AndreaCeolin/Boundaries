# At the Boundaries of Syntactic Prehistory

Scripts and data from the paper "Ceolin, A., Guardiano, C., Irimia, M. A., Longobardi, G., Bortolussi L., & Sgarro A. (to appear, 2021). At the Boundaries of Syntactic Prehistory. Philosophical Transactions of the Royal Society B. 20200197. doi: 10.1098/rstb.2020.0197". 

The repository contains the following files:

1. **table.txt**: this file contains the name of the languages and their 94 associated features (with values ```+, -, 0```), separated by a tab. 

2. **Table1.csv**: this file contains some information about the languages of the dataset

3. **table.txt**: this file contains the name of the languages and their 94 associated features (with values ```+, -, 0```), separated by a tab. 

4. **dist.py**: this Python3 script takes the file ```table.txt``` as input and prints ```TableS3```, which contains the Jaccard distances in matrix format. The syntax is simply ```python3 dist.py table.txt```. Note that features where either language shows a '0' are ignored for the purposes of the distance computation.

5. **TableS3**: this is the output of ```python3 dist.py table.txt```.

6. **coord.txt**: this file contains the coordinates of the populations sampled.

7. **gcd.py**: this script is used to print Great Circle Distances from ```coord.txt```, by simply calling```python3 gcd.py``` The output file is ```TableS5```.

8. **TableS5**: this is the output of ```python3 gcd.py```.

9.  **checker.py**: a useful tool to check whether the values in the dataset are compatible with the structural implications. It can be called with ```python3 dist.py table.txt``` and it returns a file called errors_table.txt with a list of errors.   

10. **Artificial_Langs**: this folder contains the material used for the generation of the Artificial Languages.

11. **GCD**: this folder contains the material used for the syntax/geography correlation.

12. **Figures**: this folder contains the material used to generate the figures in the paper.

13. **Supplementary_Information**: this folder contains the material used to generate the figures in Supplementary Information.



