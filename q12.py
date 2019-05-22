##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 
import pandas
tbl0 = pandas.read_csv('tbl0.tsv', sep='\t')
tbl1 = pandas.read_csv('tbl1.tsv', sep='\t')
tbl2 = pandas.read_csv('tbl2.tsv', sep='\t')
tbl21 = tbl2.groupby('_c5a')['_c5b'].sum()
print(tbl21)

