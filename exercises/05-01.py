# 05.01 - Crie uma coluna nova “twitch_points” que e resultado da 
# multiplicação do saldo de pontos e a marcação da twitch
# %%
import pandas as pd
df = pd.read_csv("../data/clientes.csv", sep=";")

# %%
df["twitch_points"] = df["flTwitch"] * df["qtdePontos"]
df