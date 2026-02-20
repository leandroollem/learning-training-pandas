# %%
import pandas as pd

idades = [32,44,12,54,67,32,23,34,32,12,45,43,28,73,29]
idades = pd.Series(idades)
idades

# %%
idades.sum()
idades.mean()
idades.min()
idades.max()
idades.describe()
# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes["flTwitch"].sum()
clientes["flTwitch"].mean()
# %%
# Agragação de série
socials = ["flEmail","flTwitch","flYouTube","flBlueSky","flInstagram"]
clientes[socials].mean()
# %%
# Pegando os indices em que as colunas são objects/string e transformando em uma lista
obj_columns = clientes.dtypes[(clientes.dtypes == "object")].index.to_list()
# %%
# Pegando os indices em que as colunas NÃO SÃO objects/string e transformando em uma lista
num_columns = clientes.dtypes[~(clientes.dtypes == "object")].index.to_list()

# %%
# Da as médias de cada coluna em uma série
clientes[num_columns].mean()
# %%
# Da as informações estatísticas em DataFrame
clientes[num_columns].describe()