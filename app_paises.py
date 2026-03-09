import streamlit as st
import pandas as pd
from coletar_paises import coletar_paises

# ATENCAO
# ainda eh necessario limpar os dados e deixar eles no mesmo formato
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

    # remove espacos no coemco e final do texto, pra gente ter ctz 
    # # q os nomes dos paises sao o mesmo
    df_web["pais"] = df_web["pais"].str.strip()
    df_meu["pais"] = df_meu["pais"].str.strip()

    # mostrar data frames na tela
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
    # sai COMO TRUE OU FALSE
    df_atualizado["alteracoes"] = df_atualizado["populacao_antigo"] == df_atualizado["populacao_novo"]

    # slva no csv
    df_atualizado.to_csv("resultado.csv", index=False)