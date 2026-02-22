# %%
import pandas as pd
df = pd.read_csv("../day04/homicidios-consolidados.csv", sep=";")
df.head()

# %%
# Empilhando a tabela
df_stack = (df.set_index(["nome", "período"])
              .stack())
df_stack = df_stack.reset_index()
df_stack.columns = ["nome", "período", "métrica", "valor"]
df_stack
# %%
# Desempilhando a tabela
df_unstack = (df_stack.set_index(["nome", "período", "métrica"])
         .unstack()
         .reset_index()
)
# %%
# Removendo o multi-index
metricas = df_unstack.columns.droplevel(0)[2:].to_list() # abaixando o level
df_unstack.columns = ["nome", "período"] + metricas
df_unstack
