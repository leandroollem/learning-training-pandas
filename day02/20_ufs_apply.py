# %%
import pandas as pd
import requests

# %%
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

response = requests.get(url, headers=headers)
dfs = pd.read_html(response.text)
# %%
uf = dfs[1]
uf.head()
# %%
def str_to_float(x:str):
    x = (x.replace(" ", "")
          .replace(",", ".")
          .replace("\xa0","")
        )
    return float(x)

# %%
uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)
# %%
def anos_to_float(x:str):
    return float(x.replace(",", ".")
                  .replace(" anos", ""))

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(anos_to_float)
# %%
# FAZER COM ALBETIZAÇÃO
def percentage_to_float(x:str):
    return float(x.replace("%", "").replace(",", "."))/100
uf["Alfabetização (2016)"] = uf["Alfabetização (2016)"].apply(percentage_to_float)

# %%
def uf_to_regiao(uf):
    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas", "Bahia", "Ceará","Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
        return "Norte"
    elif uf in ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"
    
uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao)
uf

# %%
# Se o PIB per capita > 30000 + mortalidade <  15/1000 + idh > 700  -> "Sounds Good" | "Doesn't Sounds Good"


# %%
# FAZER MORTALIDADE INFANTIL

def mortalidade_to_float(x:str):
    x = float(x.replace("‰", "").replace(",", "."))
    return x

uf["Mortalidade infantil (/1000)"] = uf["Mortalidade infantil (2016)"].apply(mortalidade_to_float)

# %%

def classify_good(row):
    return (row["PIB per capita (R$) (2015)"] > 30000 and 
            row["Mortalidade infantil (/1000)"] < 15 and 
            row["IDH (2010)"] > 700)

# Quando axis = 0 APLICA POR COLUNA, axis = 1 APLICA POR LINHA
uf["Classification"] = uf.apply(classify_good, axis=1)
uf

# %%
# Outra maneira de fazer a mesma coisa do de cima
uf["Classification"] = (uf["PIB per capita (R$) (2015)"] > 30000) & (uf["Mortalidade infantil (/1000)"] < 15) & (uf["IDH (2010)"] > 700)
uf

# %%
uf["Classification"] = uf["Classification"].replace({True : "Sounds Good", False : "Doenst Sounds Good"})
uf
