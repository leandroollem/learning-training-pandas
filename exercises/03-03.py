# %%
# 03.03 - Quantas colunas do tipo object há no arquivo produtos.csv ?
import pandas as pd
df = pd.read_csv("../data/produtos.csv", sep=";")

# %%
df.info()
print("Há apenas 4 colunas do tipo object no arquivo produtos.csv")

