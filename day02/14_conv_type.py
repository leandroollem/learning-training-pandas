# %%
import pandas as pd
df = pd.read_csv("../data/clientes.csv", sep=";")
df

# %%
# Convertendo o tipo da série
# df["qtdePontos"].astype(str)
df["qtdePontos"].astype(str).astype(float) # Pode-se encadear a conversão das séries

# %%
# Convertendo a série para tipo DATETIME64 = pd.to_datetime
# Se tivermos datas "erradas", substituimos por um timestamp escolhinho
# Parecido com o CASE WHEN

replace = {
    "0000-00-00 00:00:00.000" : "2024-02-01 09:00:00.000",
    "2024-01-01 00:00:00.000" : "2024-02-01 09:00:00.000"
    }

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"]).replace(replace)

replace = {
    "0000-00-00 00:00:00.000" : "2024-02-01 09:00:00.000",
    "2024-01-01 00:00:00.000" : "2024-02-01 09:00:00.000"
    }

# df["DtCriacao"] = pd.to_datetime(df["DtCriacao"]).replace({
#     "0000-00-00 00:00:00.000" : "2024-02-01 09:00:00.000",
#     "2024-01-01 00:00:00.000" : "2024-02-01 09:00:00.000"
#     })
    

# %%
# Vizualizar a data em tal tipo
df["DtCriacao"].dt.month
# df["DtCriacao"].dt.day
# df["DtCriacao"].dt.month_name
# df["DtCriacao"].dt.day_of_week
# df["DtCriacao"].dt.date
# df["DtCriacao"].dt.day_of_year
# df["DtCriacao"].dt.hour
# df["DtCriacao"].dt.year

