# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

# %%
filtro = df["QtdePontos"] >= 50
df[filtro]

# %%
# filtro = (df["QtdePontos"] >= 50) * (df["QtdePontos"] <= 100)
filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] <= 100)
df[filtro]

# %%
# filtro = (df["QtdePontos"] == 1) + (df["QtdePontos"] == 100)
filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro]

# %%
# Pontos entre 0 e 50 ou do ano de 2025 pra frente
filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"] <= 50) | (df["DtCriacao"]>= '2025-01-01')
df[filtro]
# %%
