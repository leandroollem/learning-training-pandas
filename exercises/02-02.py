# %%
import pandas as pd
df = pd.read_csv("../data/transacoes.csv", sep=";")
# %%
df["valores 1"] = df["QtdePontos"] + 50
df.to_csv("transacoes_1.csv", sep=";")
# %%
