# %%
import pandas as pd
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
url = "https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_PIB"
response = requests.get(url, headers=headers)

dfs = pd.read_html(response.text)
dfs

# %%
dfs[3]

# %%
df = dfs[3]
df.to_csv("regioes_por_PIB.csv", sep=";", index=False)