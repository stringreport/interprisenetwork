import pandas as pd
import streamlit as st # type: ignore
from tratamentos import tabela_conciliacao_nfs
from datetime import datetime

st.set_page_config(layout="wide")

# Titulo da pagina
st.title('Relatórios - Planilha Carregamentos')

# Lista de opções de relatorios
list_report_options = ['PEDIDOS PENDENTES', 'COMPRA LUPUS', 'REPASSE LUPUS', 'REPASSE MARCIO MALTA']

input_report = st.selectbox('Selecione o relaório',list_report_options) # Escolher relatoio
st.markdown('<hr style="border-top: 1px solid #f0f0f0">', unsafe_allow_html=True)

if input_report == 'PEDIDOS PENDENTES':

    # Filtrando a tabela com os dados a ser trabalhados
    tabela_conciliacao_nfs = tabela_conciliacao_nfs[['CLIENTE','PEDIDO CLIENTE','DESTINO','PESO VENDA','STATUS']]
    tabela_conciliacao_nfs = tabela_conciliacao_nfs[(tabela_conciliacao_nfs['STATUS'] == ' PREVISTO ') | (tabela_conciliacao_nfs['STATUS'] == ' EM ROTA ') | (tabela_conciliacao_nfs['STATUS'] == ' CARREGADO ')  ]

    # Fzendo as contagens separadas por Status
    count_previsto = tabela_conciliacao_nfs[tabela_conciliacao_nfs['STATUS'] == ' PREVISTO ']
    count_emrota = tabela_conciliacao_nfs[tabela_conciliacao_nfs['STATUS'] == ' EM ROTA '] 
    count_carregado = tabela_conciliacao_nfs[tabela_conciliacao_nfs['STATUS'] == ' CARREGADO ']
    total_open_orders = count_previsto["STATUS"].count() + count_emrota["STATUS"].count() + count_carregado["STATUS"].count() # Soma dos 3 status

    st.markdown("<h6 style='text-align: left;'>Clientes que faltam entregar os pedidos</h6>", unsafe_allow_html=True)

    col_data1, col_data2 = st.columns(2)
    group_clients = tabela_conciliacao_nfs.groupby('CLIENTE')['PEDIDO CLIENTE'].count()
    col_data1.dataframe(group_clients, width=500)

    # DIV para mostrar o total de pedidos em aberto por STATUS
    div_status_order = """
    <div style="background-color: #f0f0f0; padding: 15px; border-radius: 5px;">
        <h6 style='text-align: left;'>Contagem por Status</h6>
        <p> PREVISTO : {} </br>
        EM ROTA : {} </br>
        CARREGADO : {}</p>
    </div>
    """.format(count_previsto["STATUS"].count(),count_emrota["STATUS"].count(),count_carregado["STATUS"].count())
    col_data2.markdown(div_status_order, unsafe_allow_html=True)

    col_data2.write('')

    # DIV para mostrar o total de pedidos em aberto
    div_total_order = """
    <div style="background-color: #F4D03F; padding-top: 5px; border-radius: 20px;">
        <p style="font-size: 20px; text-align: center;">Total de pedidos em aberto : {}</p>
    </div>
    """.format(total_open_orders)
    col_data2.markdown(div_total_order, unsafe_allow_html=True)
    

    st.markdown("<h5 style='text-align: left;'>Tabela</h5>", unsafe_allow_html=True)
    height_frame = 37 * len(tabela_conciliacao_nfs)
    st.dataframe(tabela_conciliacao_nfs, height=height_frame, width=1200)