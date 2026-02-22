# %%
import pandas as pd
df = pd.read_csv("../day04/homicidios-consolidados.csv", sep=";")
df.head()

# %%
df_stack = df.set_index(["nome", "período"]).stack().reset_index()
df_stack.columns = ["nome", "periodo", "metricas", "valor"]
df_stack

# %%
(df_stack.pivot_table(values="valor", 
                     index=["nome", "periodo"], 
                     columns="metricas")
        .reset_index()
)

# %%
# Tabela com média em cada estado
df_stack.pivot_table(values="valor", 
                    index="nome", 
                    columns="metricas",
                    aggfunc="mean")

# %%
df_stack.pivot_table(values="valor", 
                    index="nome", 
                    columns="metricas",
                    aggfunc="max")
# %%
(df_stack.pivot_table(values="valor", 
                    index="nome", 
                    columns="metricas",
                    aggfunc="max")
        .stack())
df_stack