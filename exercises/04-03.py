# 04.03 - Quantas transações ocorreram no dia 2025-02-01?
# %%
import pandas as pd
df = pd.read_csv("../data/transacoes.csv", sep=";")

# %%

filtro = (df["DtCriacao"] >= "2025-02-01") & (df["DtCriacao"] < "2025-02-02")
valor = df[filtro].shape[0]
print(f"Houve {valor} transacoes no dia 2025-02-01")