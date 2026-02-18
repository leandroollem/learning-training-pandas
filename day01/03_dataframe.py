# %%
import pandas as pd

idades = [20, 22, 50, 40, 80, 35, 40, 20]

letras = ["A", "b", "c", "d", "e", "f","g", "f"]

series_idades = pd.Series(idades)
series_letras = pd.Series(letras)

# %%

df = pd.DataFrame()
df["idades"] = series_idades
df["letras"] = series_letras
df
# %%

df["letras"]
# %%
# retorna uma série de um certo índice
df.iloc[0]
df.iloc[0]["idades"]

# %%
# retornando a ultima linha e a idade
df.iloc[-1]["idades"]