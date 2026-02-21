# Como podemos calcular as estatísticas descritivas dos pontos 
# das transações de cada usuário?
# %%
import pandas as pd
df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

# %%
(df.groupby(by="IdCliente", as_index=False)["QtdePontos"]
    .describe()
)

