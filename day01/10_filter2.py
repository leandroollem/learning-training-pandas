# %%
import pandas as pd
df = pd.read_csv("../data/transacao_produto.csv", sep=";")
df

# %%
filtro = (df["IdProduto"] == "5" ) | (df["IdProduto"] == "11")
df[filtro]
# %%
df["IdProduto"].isin(["5", "11"])
df[filtro]

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

filtro = clientes["DtCriacao"].notna()
clientes[filtro]

# %%
# ~ é para negar a condição 
~clientes["DtCriacao"].isna()