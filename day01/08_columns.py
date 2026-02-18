# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep = ";")
df

# %%
df.shape

# %%
df.info(memory_usage="deep")

# %%
df.dtypes

# %%
# Renomeando uma coluna
# Chave = Nome antigo | Valor = Nome novo

renamed_columns = {
    "QtdePontos" : "qtPontos",
    "DescSistemaOrigem": "SistemaOrigem"
}

# df = df.rename(columns=renamed_columns)
df.rename(columns=renamed_columns, inplace=True)

# %%
df

# %%
# Retorna uma série do IdCliente
df["IdCliente"]
# %%
# Retorna um dataframe por se ter DOIS [[]]
df[["IdCliente","qtPontos"]]
# %%
columns = ["IdCliente","qtPontos"]
df[columns]

# %%
# SELECT * FROM df
df

# %%
# SELECT IdCliente FROM df
df[["IdCliente"]]

# %%
# SELECT IdCliente, qtPontos FROM df LIMIT 5
df[["IdCliente", "qtPontos"]].head(5)

# %%
# SELECT IdCliente, IdTransacao, qtPontos FROM df LIMIT 5
df[["IdCliente", "IdTransacao", "qtPontos"]].head(5)

# %%
colunas = list(df.columns)
colunas.sort()
colunas

df = df[colunas]
df