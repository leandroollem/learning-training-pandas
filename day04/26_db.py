# %%
import pandas as pd
import sqlalchemy
# %%
# ORM = MANEIRA DE REPRESENTAR AS ENTIDADES DO PROGRAMA EM FORMATO DE TABELAS EM BANCO DE DADOS
engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")

# %%
# NO TERMINAL : 
# cd data/
# sqlite3 olist.db
#.tables

# %%
clientes = pd.read_sql_table(table_name="tb_customers", con=engine)
clientes.shape

# %%
query = "SELECT * FROM tb_customers LIMIT 100"
df_100 = pd.read_sql_query(query, con=engine)
df_100
# %%
