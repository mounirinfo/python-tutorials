import pandas as pd
from sqlalchemy import create_engine
ma_con= create_engine("mysql://root:@localhost/phone_shop")
frame_sql=pd.read_sql_query("select * from produit", ma_con)
print(frame_sql)
