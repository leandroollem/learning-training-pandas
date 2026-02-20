# %%
import pandas as pd
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()
# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()
# %%
# CASO AS COLUNAS DO ON SEJAM IGUAIS (QUE NÃO É O CASO)
transacoes.merge(
    right=clientes, 
    how="left", 
    on=['idCliente'],
    suffixes=["Transacao","Cliente"]
)
# %%
# CASO AS COLUNAS DO ON NÃO SEJA IGUAIS (QUE É O CASO)
transacoes.merge(
    right=clientes, 
    how="left", 
    left_on=["IdCliente"],
    right_on=["idCliente"],
    suffixes=["Transacao","Cliente"]
)