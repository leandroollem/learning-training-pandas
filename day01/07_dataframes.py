# %%
import pandas as pd
df = pd.read_csv("../data/clientes.csv", sep=";")
df.head(n=10) # = LIMIT do SQL
# %%
df.tail(n=10) # Mostra o final do dataset

# %%
df.sample(n=10) # Mostra aleatoriamente e embaralhado

# %%
df.shape # Mostra uma tupla (Número de linhas, Número de Colunos)
# %%
df.columns # Mostra todas as colunas

# %%
df.index # Mostra o range do index e o step(de quanto em quanto vai aumentando)

# %%
df.info() # Mostra informações gerais do DataFrame

# %%
# Mostra a info gerais mas mostra precisamente o quanto de momória esta usando
df.info(memory_usage="deep") 

# %%
df.info(memory_usage="deep", max_cols=2) 

# %%
# Mostra uma série onde os valores dentro da série é o tipo de cada coluna
df.dtypes

# %%
df.dtypes["flInstagram"]