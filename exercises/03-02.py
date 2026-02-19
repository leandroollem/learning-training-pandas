# %%
# 03.02 - Quantas colunas do tipo int há no arquivo transacoes.csv ?
import pandas as pd
df = pd.read_csv("../data/transacoes.csv", sep=";")

# %%
df.info()
print("Há apenas um colunas do tipo int no arquivo transacoes.csv")