# %%
import pandas as pd
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

# %%
# Remove TODAS AS LINHAS do NaN
clientes.dropna() # Traz uma view e podemos retribuir a clientes
# clientes.dropna(how="any") -> é a forma default | mesma coisa que clientes.dropna()
# %%
# Adicionando critério que a LINHA INTEIRA tem que ser NaN
clientes.dropna(how="all")

# %%
test = pd.DataFrame (
    {
        "nome": ["Lendro", None, "Matheus", "Diego"],
        "idade": [None, None, 21, 20],
        "salario": [2535, 3000, None, 4150],
    }
)
test.dropna(how="any")

# %%
test = pd.DataFrame (
    {
        "nome": ["Lendro", None, "Matheus", "Diego"],
        "idade": [None, None, 21, 20],
        "salario": [2535, 3000, None, 4150],
    }
)
# Drop a LINHA INTEIRA usando como critério a idade onde for NA
test.dropna(how="all", subset=["idade"])

# %%
test = pd.DataFrame (
    {
        "nome": ["Lendro", None, "Matheus", "Diego"],
        "idade": [None, None, 21, 20],
        "salario": [2535, 3000, None, 4150],
    }
)
# Drop a LINHA INTEIRA usando como critério a idade E O salario onde for NA
test.dropna(how="all", subset=["idade", "salario"]) 

# %%
test = pd.DataFrame (
    {
        "nome": ["Lendro", None, "Matheus", "Diego"],
        "idade": [None, None, 21, 20],
        "salario": [2535, 3000, None, 4150],
    }
)
# Drop a LINHA INTEIRA usando como critério a idade ou o salario onde for NA
test.dropna(how="any", subset=["idade", "salario"]) 

# %%
test = pd.DataFrame (
    {
        "nome": ["Lendro", None, "Matheus", "Diego"],
        "idade": [None, None, 21, 20],
        "salario": [2535, 3000, None, 4150],
    }
)

test.dropna(how="any", subset=["idade", "nome"]) 

# %%
test = pd.DataFrame (
    {
        "nome": ["Lendro", None, "Matheus", "Diego"],
        "idade": [None, None, 21, 20],
        "salario": [2535, 3000, None, 4150],
    }
)

test.dropna(how="all", subset=["idade", "nome"]) 


# %%
# Preenchendo os valores NA
test.fillna(0)

# %%
# Preenchendo os valores NA na coluna "idade"

test = pd.DataFrame (
    {
        "nome": ["Lendro", None, "Matheus", "Diego"],
        "idade": [None, None, 21, 20],
        "salario": [2535, 3000, None, 4150],
    }
)

test["idade"] = test["idade"].fillna(0)
test

# %%
# Substituindo os NA com valores escolhido por coluna
test.fillna({"nome" : "Alguem", "salario": 0})
# %%
# Substituindo os NA das colunas selecionadas com a média
test.fillna(test[["idade", "salario"]].mean())
# OU
medias = test[["idade", "salario"]].mean()
test.fillna(medias)

# %%
# Substituindo os valores somente da Coluna "idade" com a média da "idade"
test["idade"].fillna(test["idade"].mean()).mean()
