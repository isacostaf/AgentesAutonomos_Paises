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