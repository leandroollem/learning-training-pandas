# %%
# 03.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv ?
import pandas as pd
df = pd.read_csv("../data/clientes.csv", sep=";")

# %%
cliente = df["idCliente"].iloc[4]
print(f"O id do cliente no índice 4 é: {cliente}")

