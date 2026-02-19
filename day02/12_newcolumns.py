# %%
import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head(10)

# %%
# Adicionando 100 em todos os pontos e criando uma coluna nova
df["pontos_100"] = df["qtdePontos"] + 100 
df.head()

# %%
df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()

# %%
# Saber se a pessoa tem email ou Twitch
df["flEmail"] * df["flTwitch"]

# %%
# Saber quantas redes sociais a pessoa tem, em uma nova coluna
df["qtSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df.head(10)

# %%
# Saber todas redes sociais, em uma nova coluna
df["allSocial"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]
df.head(10)

# %%
df["qtdePontos"].describe()

# %%
# Aplicando logaritmo na série "qtdePontos" - O +1 é para retirar os valores -inf
# Geralmente usa essa transformação para deixar mais próximos um dos outro
df["logPontos"] = np.log(df["qtdePontos"]+1)
df["logPontos"].describe()

# %%
# Plotando para mostrar a diferença de distribuição com log e sem log.
import matplotlib.pyplot as plt

plt.hist(df["qtdePontos"])
plt.grid()
plt.show

# %%
plt.hist(df["logPontos"])
plt.grid()
plt.show