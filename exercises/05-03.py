# 05.03 - Crie uma coluna que sinalize se a pessoa tem vínculo 
# com alguma (qualquer uma) plataforma de rede social.
# %%
import pandas as pd
df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %%
df["flag_social"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df["flag_social"] = df["flag_social"].values > 0
df.head(10)

