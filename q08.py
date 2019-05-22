##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 
import pandas
tbl0 = pandas.read_csv('tbl0.tsv', sep = '\t')
tbl0aux = tbl0.copy()
from datetime import datetime
tbl0aux["_c3"] = pandas.to_datetime(tbl0aux["_c3"])
tbl0aux['_c3'].dt
tbl0aux['ano'] = tbl0aux['_c3'].dt.year
print(tbl0aux)