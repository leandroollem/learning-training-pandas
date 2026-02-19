# %%
import pandas as pd
df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %%
user = "000dc0f6-e4f2-4a42-b8cd-b586ed1c709a"

def last_id(x):
    return x.split("-")[-1]

last_id(user)

# %%
id_novo = []

for i in df["idCliente"]:
    novo = last_id(i)
    id_novo.append(novo)

df["id_novo"] = id_novo
df.head()

# %%
df["new_id"] = df["idCliente"].apply(last_id)
df
# %%
