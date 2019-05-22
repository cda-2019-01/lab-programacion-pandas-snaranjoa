##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
import pandas
tbl2 = pandas.read_csv('tbl2.tsv', sep="\t")
tbl2['lista'] = pandas.concat(['_c5a'], tbl2['_c5b'])
