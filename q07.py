##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 
import pandas
tbl0 = pandas.read_csv('tbl0.tsv', sep = '\t')
tbl0aux = tbl0.copy()
tbl0aux['suma'] = tbl0aux['_c0'] + tbl0aux['_c2']
print(tbl0aux)