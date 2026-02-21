# Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?
# %%
import pandas as pd
df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %%
df["totalSocials"] = (df["flEmail"]+
                      df["flTwitch"]+
                      df["flYouTube"]+
                      df["flBlueSky"]+
                      df["flInstagram"])

media = df["totalSocials"].mean()
variancia = df["totalSocials"].var()
maximo = df["totalSocials"].max()

print(f"Média: {media}")
print(f"Variância: {variancia}")
print(f"Máximo: {maximo}")

# socials = [
#     "flEmail",
#     "flTwitch",
#     "flYouTube",
#     "flBlueSky",
#     "flInstagram",
# ]

# df[socials].sum(axis=1).describe()