# %%
import pandas as pd
import os
def read_file(file_name:str):
    df = (pd.read_csv(f"../data/ipea/{file_name}.csv", sep=";")
             .rename(columns={"valor":file_name})
             .set_index(["nome", "período"])
             .drop(["cod"], axis=1)
)   
    return df
# %%
# O os.listdir passa uma lista dos arquivos que contém no diretório
file_names = os.listdir("../data/ipea")
file_names
# %%
dfs = []
for i in file_names:
    file_name = i.split(".")[0]
    dfs.append(read_file(file_name))
dfs
# %%
df_full = pd.concat(dfs, axis=1).reset_index().sort_values(["período", "nome"])
df_full
# %%
df_full.to_csv("../day04/homicidios-consolidados.csv", index=False, sep=";")
# %%
# Encontrando onde foi o csv
import os; print(os.getcwd())