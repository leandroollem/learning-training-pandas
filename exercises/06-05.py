# Qual a média de transações / dia?
# %%
import pandas as pd
df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head(10)

# %%
df["DtDia"] = pd.to_datetime(df["DtCriacao"]).dt.date

summary = df.agg({
    "IdTransacao":"count",
    "DtDia":"nunique"
})

transacoes = summary["IdTransacao"] / summary["DtDia"]
transacoes



