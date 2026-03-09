import streamlit as st
import pandas as pd
from coletar_paises import coletar_paises

# titulo
st.title("Coletor de paises")

# se apertar o botao
if st.button("Coletar dados"):

    # dados sao os dados retornados da funcao coletar_advogados
    dados = coletar_paises()

    # transofrmamos esses dados em uma tabela (antes era um dicionario)
    df = pd.DataFrame(dados)

    # mostra a tabela no navegador
    st.dataframe(df)

    # slaav em um arquivo sv essa tabela, index falso pra nao salvar o index
    df.to_csv("paises_insights.csv", index=False)

    # imprime mensagem
    st.success("Dados coletados e salvos!")

    df_web = pd.DataFrame(dados)
    df_meu = pd.read_csv("meu_dataset.csv")

    df_web["pais"] = df_web["pais"].str.strip()
    df_meu["pais"] = df_meu["pais"].str.strip()

    st.write(df_meu)
    st.write(df_web)

    # join as duas tabelas
    # a nova tabela chama df_atualizado
    # on = pais: usar pais como chave de comparacao
    # prioridade da esquerda, ou seja mantenha tudo da tabela original, 
    # mesmo q um dado n exista na nova
    # suffixes, ja q as duas tem nome siguais agnt vai diferir c um sufixo
    # nesse caso _antigo e _novo
    df_atualizado = df_meu.merge(
    df_web,
    on="pais",
    how="left",
    suffixes=("_antigo", "_novo")
)
    # criamos uma nova coluna que eh:
    # a populacao_novo so q se nao existir um valor nela pegamos o valor antigo
    # .fillna() = se for NaN → substitua por outro valor
    # "se populacao_novo estiver vazio
    # use populacao_antigo"
    df_atualizado["populacao"] = df_atualizado["populacao_novo"].fillna(df_atualizado["populacao_antigo"])

    # cria um df novo q eh apenas as colunas     quqeremos, tiramos as novas e as velhas
    df_final = df_atualizado[["pais","sigla","populacao","continente"]]

    # slva no csv
    df_final.to_csv("dataset_atualizado.csv", index=False)