# %%
# 03.01 - Quantas linhas há no arquivo clientes.csv ?
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.describe

print("O arquivo clientes.csv tem: 4970 linhas")