# %%
import pandas as pd

df = pd.DataFrame({
    "cliente": [1,2,3,4,5],
    "nome": ["Lendro","Matheus","Roberto","Diego","Guilherme"]
})

df2 = pd.DataFrame({
    "cliente": [6,7,8],
    "nome": ["Sabugueiro","Zezeke","Popeyes"],
    "idade":[32,30,31]
})

df3 = pd.DataFrame({
    "idade":[32,34,19,54,33]
})
# pd.concat pega LISTAS
pd.concat([df, df2], ignore_index=True)

# %%
df3 = df3.sort_values(by="idade").reset_index(drop=True)
df3
# %%
pd.concat([df,df3], axis=1)
# %%
