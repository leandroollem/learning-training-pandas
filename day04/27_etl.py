# %%
import pandas as pd
import sqlalchemy
from sklearn import cluster

with open("../day04/etl.sql") as open_file:
    query = open_file.read()
    
print(query)

# %%
engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")
df = pd.read_sql_query(query, con=engine)
df
# %%
# Treinando o modelo de cluster
kmean = cluster.KMeans(n_clusters=4)
kmean.fit(df[["totalRevenue", "qtSales"]])
df["cluster"] = kmean.labels_
df
# %%
# Criando um tabela "sellers_cluster" na olist.db
df.to_sql("sellers_cluster", con=engine, index=False, if_exists="replace")