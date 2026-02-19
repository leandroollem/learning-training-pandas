# %%
import pandas as pd

# %% 
df = pd.DataFrame (
    {
        "nome": ["Lendro", "Robert", "Matheus", "Diego", "Robert"],
        "sobrenome": ["Mello", "Junior", "Lopes", "Mello", "Junior"],
        "salario": [1000 , 1500, 2000, 3000, 2500] 
    }
)
df

# %%
# Dropa AS LINHAS que são duplicadas, por default, mantém a primeira | df.drop_duplicates(keep="first")
df.drop_duplicates()
# %%
# Ao invés de manter a primeira, mantém a ultima duplicata
df.drop_duplicates(keep="last")

# %%
df.drop_duplicates(subset=["nome", "sobrenome"])

# %%
df.drop_duplicates(keep="last", subset=["nome", "sobrenome"])
# %%
df = (df.sort_values("salario", ascending=False)
      .drop_duplicates(keep="last", subset=["nome", "sobrenome"]))
df
# %%
