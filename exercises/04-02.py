# 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?
# %%
import pandas as pd
df = pd.read_csv("../data/clientes.csv", sep=";")

# %%
filtro = df["qtdePontos"] > 1000
qtde = df[filtro].shape[0]
# %%
print(f"Há {qtde} clientes com saldo de pontos maior que 1000")
# %%
