# %%
import pandas as pd
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%
# Aplicando count em cada coluna para cada cliente (como índice)
# Retorna um DataFrame
transacoes.groupby(by=["IdCliente"]).count()

# %%
# Retorna uma Serie
transacoes.groupby(by=["IdCliente"])["IdTransacao"].count()

# %%
# Retorna um DataFrame
transacoes.groupby(by=["IdCliente"])[["IdTransacao"]].count()

# %%
# Caso queira que retorna o IdCliente como coluna e não index
transacoes.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]].count()

# %%
# Somar quantidade de transações, quantidade de pontos e a média de pontos por transação para cada cliente
summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
                     .agg({
                            "IdTransacao":["count"],
                            "QtdePontos":["sum", "mean"]
                        }))
summary
# %%
summary[("QtdePontos", "mean")]
# %%
summary.columns = ["IdCliente", "qtdeTransacao", "totalPontos", "avgPontos"]
summary
# %%
