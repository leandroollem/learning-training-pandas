# %%
import pandas as pd

df = pd.read_csv("../case_credit_card/dados_cartao.csv", sep=";")
df
# %%
# Transformando dtTransacao em DATETIME
df["dtTransacao"] = pd.to_datetime(df["dtTransacao"])
df

# %%
# Criando coluna com o valor de cada parcela
df["vlParcela"] = df["vlVenda"] / df["qtParcelas"]
df

# %%
# Criando uma coluna com a ordem das parcelas em uma lista
df["ordemParcela"] = df.apply(lambda row: [i for i in range(row['qtParcelas'])], axis=1)
df

# %%
# Explodindo a lista da ordem das parcelas
df_explode = df.explode("ordemParcela")
df_explode

# %%
# Criando uma coluna com a data de cada parcela, feita somada a ordem da parcela com o mês da transação
def calcDtParcela(row):
    dt = row["dtTransacao"] + pd.DateOffset(months=row["ordemParcela"])
    dt =  f"{dt.year}-{dt.month}"
    return dt

df_explode["dtParcela"] = df_explode.apply(calcDtParcela, axis=1)
df_explode
# %%
# Agrupando por idCliente e a data da parcela. Somando os valores da parcela em tal mês de cada cliente
# E transformando em uma pivot_table
(df_explode.groupby(["idCliente", "dtParcela"])
           ['vlParcela'].sum()
           .reset_index()
           .pivot_table(index='idCliente',
                        columns='dtParcela',
                        values='vlParcela',
                        fill_value=0))