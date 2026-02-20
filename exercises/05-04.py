# 05.04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?
# %%
import pandas as pd
df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %%
cliente_maior = df.sort_values(by="qtdePontos",ascending=False).head(1)["idCliente"].values

cliente_menor = df.sort_values(by="qtdePontos",ascending=True).head(1)["idCliente"].values

print(f"O cliente com maior saldo de pontos é: {cliente_maior}\nO cliente com menor saldo de pontos é: {cliente_menor}"
      )