# %%
import pandas as pd

# Lendo o arquivo
df = pd.read_csv("../data/clientes.csv", sep=";")
df

# %%
# Salvo o arquivo
df.to_csv("clientes2.csv", index=False, sep="|")

# %%
df.to_parquet("clientes.parquet", index=False)

# %%
df_2 = pd.read_parquet("clientes.parquet")
df_2

# %%
df.to_excel("clientes.xlsx", index=False)

# %%
df_3 = pd.read_excel("clientes.xlsx")
df_3