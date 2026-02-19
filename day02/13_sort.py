# %%
import pandas as pd
clientes = pd.read_csv("../data/clientes.csv", sep=";")

max_points = clientes["qtdePontos"].max()
filter = clientes["qtdePontos"] == max_points
clientes[filter]


# %%
# .sort_values() ordenando a SÉRIE do menor para o maior
clientes["qtdePontos"].sort_values()

# %%
# Ordenando o DataFrame do maior para o menor. E pegando os cinco primeiros
# O .head funciona porque é um DataFrame, não série
top_5 = (clientes.sort_values(by="qtdePontos", ascending=False)
        .head(5)["idCliente"]) # Aqui estou pegou uma Série de um dataframe ordenado

# %%
test = pd.DataFrame (
    {
        "nome": ["Lendro", "Robert", "Matheus", "Diego"],
        "idade": [24, 28, 21, 20],
        "salario": [2535, 3000, 3000, 4150],
    }
)

# Vai ordenar primeiro pelo salário e depois pela idade
# O salario por ordem DESCRESCENTE e a idade por ordem CRESCENTE
test.sort_values(by=["salario", "idade"], ascending=[False, True])


