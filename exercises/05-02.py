# 05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova
# %%
import pandas as pd
import numpy as np
df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()
# %%
df["pontos_log"] = np.log(1+df["qtdePontos"])
df