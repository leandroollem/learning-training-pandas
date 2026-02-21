# Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.
# %%
import pandas as pd
df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head(10)

# %%
((df.groupby(by="IdCliente",as_index=False)["IdTransacao"])
                            .count()
                            .sort_values(by="IdTransacao",ascending=False)
                            .head(10)
)
                                    