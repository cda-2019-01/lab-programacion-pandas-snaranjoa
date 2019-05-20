##
## Imprima el promedio de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
import pandas
tbl0 = pandas.read_csv('tbl0.tsv', sep = '\t')
q02 = tbl0.groupby('_c1').mean()['_c2']
print(q02)
