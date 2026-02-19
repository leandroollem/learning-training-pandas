# %%
import pandas as pd
# Mostrando a ultima e a primeira transacao de cada dia
# %%
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes

# %%
transacoes["date"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date
transacoes = transacoes.sort_values("DtCriacao")
transacoes

# %%
first = transacoes.drop_duplicates(keep="first", subset=["IdCliente", "date"])
last = transacoes.drop_duplicates(keep="last", subset= ["IdCliente", "date"])

pd.concat([first,last])
