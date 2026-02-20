# %%
# 03.05 - Qual o saldo de pontos do cliente na 10a posição (sem ordenar) 
# do arquivo clientes.csv ?

import pandas as pd
df = pd.read_csv("../data/clientes.csv", sep=";")
# %%
valor = df["qtdePontos"][9]
print(f"O saldo de pontos do cliente na 10ª posição é: {valor}")