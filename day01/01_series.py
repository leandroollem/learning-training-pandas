# %%
import pandas as pd

idades = [20, 22, 50, 40, 80, 35, 40, 20, 
          21, 23, 27, 29, 45, 36, 71, 30
          ]

series_idades = pd.Series(idades)
series_idades

# %%
media_idades = series_idades.mean()
var_idades = series_idades.var()
summary_idades = series_idades.describe()
print(var_idades)
print(media_idades)
print(summary_idades)