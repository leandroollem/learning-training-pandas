# %%
import pandas as pd

idades = [20, 22, 50, 40, 80, 35, 40, 20, 
          21, 23, 27, 29, 45, 36, 71, 30
          ]

series_idades = pd.Series(idades) # Transformou em Series
series_idades

# %%
series_idades[0]

# %%
# organinzando a serie do menor para o menor
series_idades = series_idades.sort_values() 
series_idades

# %%
# iloc = muda o meio de navegação para posição (como a das lista) 
# ao inves de chave
series_idades.iloc[-1] 

# %%
series_idades.iloc[:3]
# %%
series_idades.iloc[::-1] # pegar do ultimo para o primeiro

# %%
idades = [20, 22, 50, 40, 80, 35, 40, 20]

indexs = ["A", "b", "c", "d", "e", "f","g", "f"]
series_idades = pd.Series(idades, index=indexs)
series_idades

# %%
series_idades.iloc[-1] # ignorando os indices e navegando pelas linhas/ordem das linhas
series_idades.loc["A"] # navegando pelos indices

# %%
