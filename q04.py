##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas
tbl1 = pandas.read_csv('tbl1.tsv', sep = '\t')
tbl11 = tbl1.copy()
unique = tbl11['_c4'].unique()
unique1 = sorted(unique)
unique2 = [n.upper() for n in unique1]
print(unique2)

