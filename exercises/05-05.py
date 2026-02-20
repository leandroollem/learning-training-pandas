# 05.05 - Selecione a primeira transação diária de cada cliente.

# %%
import pandas as pd

# %%
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%
transacoes = transacoes.sort_values(by="DtCriacao") # ordenar
transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date # criar uma coluna com apenas a data para a transacao

first = transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"]) # dropa as duplicatas e pegando só as primeiras do dia
last = transacoes.drop_duplicates(keep="last", subset=["IdCliente", "data"]) # dropa as duplicatas e pegando só as ultimas do dia

pd.concat([last,first])