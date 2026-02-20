# Quem teve mais transações de Streak?
# %%
import pandas as pd
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()
# %%
transacao_produto = pd.read_csv("../data/transacao_produto.csv", sep=";")
transacao_produto.head()
# %%
produtos = pd.read_csv("../data/produtos.csv", sep=";")
produtos.head()
# %%
# AGRUPANDO OS DATAFRAMES

cliente_transacao_produto = transacoes.merge(
    transacao_produto, 
    on="IdTransacao",
    how="left"
)[["IdTransacao", "IdCliente", "IdProduto"]]

df_full = cliente_transacao_produto.merge(
    produtos, 
    on="IdProduto",
    how="left"
)

# APLICANDO O FILTRO

filtro = df_full["DescNomeProduto"]=="Presença Streak"
df_full = df_full[filtro]
df_full

# ----- OU -----
# df_full = df_full[df_full["DescNomeProduto"]=="Presença Streak"]
# df_full

# AGRUPANDO POR ID CLIENTE, PEGANDO A ID TRANSACAO E CONTANDO-A. DEPOIS, ORDENANDO DO MAIOR PARA O MENOR
# E LIMITANDO A 1 PESSOA

(df_full.groupby(by=["IdCliente"])["IdTransacao"]
        .count()
        .sort_values(ascending=False)
        .head(1)
)
