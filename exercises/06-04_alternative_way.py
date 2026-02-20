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
produtos = produtos[produtos["DescNomeProduto"]=="Presença Streak"]

(transacoes.merge(transacao_produto, on="IdTransacao",how="left")
           .merge(produtos, on=["IdProduto"], how="right")
           .groupby(by=["IdCliente"])["IdTransacao"]
           .count()
           .sort_values(ascending=False)
           .head(1)
)