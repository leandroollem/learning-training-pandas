# 04.01 - Quantos clientes tem vínculo com a Twitch?
# %%
import pandas as pd
df = pd.read_csv("../data/clientes.csv", sep=";")

# %%
filtro = df["flTwitch"] == 1
valor = df[filtro].shape[0]
print(f"Há {valor} clientes com vínculo com a Twitch")