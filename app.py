import requests
import pandas as pd
from itertools import product

URL_PRODUTOS = 'https://case-1sbzivi17-henriques-projects-2cf452dc.vercel.app'

# buscar os produtos disponíveis
def buscar_produtos():
    response = requests.get(URL_PRODUTOS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar produtos: {response.status_code}")
        return []

# filtra produtos por categoria
def filtrar_produtos(produtos, categoria):
    return [p for p in produtos if p['Categoria'] == categoria]

# gera combinações possíveis entre os produtos
def gerar_combinacoes(pa, inv, ctrl):
    combinacoes = []
    for p in pa:
        for i in inv:
            for c in ctrl:
                if p['Potencia em W'] == i['Potencia em W'] == c['Potencia em W']:
                    combinacoes.append((p, i, c))
    return combinacoes

# DataFrame final
def criar_dataframe(combinacoes):
    geradores = []
    id_gerador = 11111
    for pa, inv, ctrl in combinacoes:
        geradores.append([id_gerador, pa['Potencia em W'], pa['Id'], pa['Produto'], 1])
        geradores.append([id_gerador, pa['Potencia em W'], inv['Id'], inv['Produto'], 1])
        geradores.append([id_gerador, pa['Potencia em W'], ctrl['Id'], ctrl['Produto'], 1])
        id_gerador += 1
    return pd.DataFrame(geradores, columns=["ID Gerador", "Potência", "ID Produto", "Nome Produto", "Quantidade"])

if __name__ == "__main__":
    produtos = buscar_produtos()
    paineis = filtrar_produtos(produtos, 'Painel Solar')
    inversores = filtrar_produtos(produtos, 'Inversor')
    controladores = filtrar_produtos(produtos, 'Controlador de carga')

    combinacoes = gerar_combinacoes(paineis, inversores, controladores)
    df = criar_dataframe(combinacoes)

    # CSV
    df.to_csv("geradores_configurados.csv", index=False)
    print(f"{len(combinacoes)} geradores configurados salvos em 'geradores_configurados.csv'")
