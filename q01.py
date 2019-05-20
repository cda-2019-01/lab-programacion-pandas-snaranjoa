##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0
## 
import pandas
tbl0 = pandas.read_csv('tbl0.tsv', sep = '\t')
q01 = tbl0.groupby('_c1').count()['_c0']
print(q01)