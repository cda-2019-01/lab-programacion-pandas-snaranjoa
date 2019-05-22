##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 
import pandas
tbl1 = pandas.read_csv('tbl1.tsv', sep = '\t')
tbl10 = tbl1.sort_values('_c4')
tbl11 = tbl10.groupby('_c0')['_c4'].apply(lambda x: ','.join(x))
tbl12 = pandas.DataFrame({'_c0':tbl11.index, 'lista':tbl11.values})
print(tbl12)