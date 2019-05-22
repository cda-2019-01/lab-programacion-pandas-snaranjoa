##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 
import pandas
tbl0 = pandas.read_csv('tbl0.tsv', sep = '\t')
tbl0.head()
tbl01 = tbl0.sort_values('_c2')
tbl01['_c2'] = tbl01['_c2'].apply(str)
tbl02 = tbl01.groupby('_c1')['_c2'].apply(lambda x: ':'.join(x))
tbl03 = pandas.DataFrame({'_c0':tbl02.index, 'lista':tbl02.values})
print(tbl03)
