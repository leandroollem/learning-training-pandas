# Qual usuário teve maior quantidade de pontos debitados?
# %%
import pandas as pd
df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head(10)

# %%
filtro = df["QtdePontos"] < 0
df[filtro]
((df[filtro].groupby("IdCliente", as_index=False)["QtdePontos"])
            .sum()
            .sort_values(by="QtdePontos", ascending=True)
            .head(1))