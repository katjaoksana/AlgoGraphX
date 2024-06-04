The **CSV** files contain the incidences of a graph and the weight associated with the edge.
You can use these files as examples to run the programs by simply entering the CSV file name
at the end of the code where the function is called.

**Example**

_MatrizAdyacencia("graph.csv")_

_FloydWarshall("graph.csv")_

To run the _FloydWarshall.py_ code, it's necessary to generate the adjacency matrix from the _CSV_ file.
The _MatrizAdyacencia.py_ code generates this matrix, so it's necessary for the _FloydWarshall.py_ code to function.

**Note:** the _MatrizAdyacencia.py_ code works independently.
