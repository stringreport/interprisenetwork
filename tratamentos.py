import pandas as pd 

# CONTAS A PAGAR ------------------------------------------------------------------------------
tabela_contas_pagar = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSId0_Zh0fAmLE4ia9-t9UIpsZ98V-0Tqc0ba0E-zNAOnfOA195bLJ7pSHpYCiFe2NowTyZIJ1B5nFk/pub?gid=910529611&single=true&output=csv', header=1)
tabela_contas_pagar[' VALOR '] = tabela_contas_pagar[' VALOR '].str.replace('.','').str.replace(',','.').str.slice(3).astype(float)
tabela_contas_pagar[' REFERENTE '] = tabela_contas_pagar['REFERENTE'].astype(str)
# tabela_contas_pagar = tabela_contas_pagar[tabela_contas_pagar['DT PAGAMENTO'].notna() ]
tabela_contas_pagar['DT PAGAMENTO'] = tabela_contas_pagar['DT PAGAMENTO'].str.strip()
tabela_contas_pagar['CLASSIFICAÇÃO'] = tabela_contas_pagar['CLASSIFICAÇÃO'].str.strip()
tabela_contas_pagar['MACRO EMPRESA'] = tabela_contas_pagar['MACRO EMPRESA'].str.strip()
tabela_contas_pagar['CATEGORIA'] = tabela_contas_pagar['CATEGORIA'].str.strip()
tabela_contas_pagar['VENCIMENTO'] = pd.to_datetime(tabela_contas_pagar['VENCIMENTO'], format='%d/%m/%Y').dt.date
tabela_contas_pagar['COMPETENCIA'] = pd.to_datetime(tabela_contas_pagar['COMPETENCIA'], format='%d/%m/%Y').dt.date
tabela_contas_pagar['PAGAMENTO'] = pd.to_datetime(tabela_contas_pagar['PAGAMENTO'], format='%d/%m/%Y').dt.date
# ----------------------------------------------------------------------------------------------

# CONCILIAÇÃO DE NOTAS -------------------------------------------------------------------------
transform_columns = ['LUPUS','VALOR VENDA','LUCRO BRUTO','CUSTO ADM','COMISSAO','LIQUIDO',' % ']

tabela_conciliacao_nfs = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vT4-fO1dCtnGNCaa2wK8ULj2Mgd5uKOPAUARs66Q4HpRQIQ0SSmXvSF0eOt-esIx_TBsMEWIHRUrcHI/pub?gid=1565722202&single=true&output=csv')
tabela_conciliacao_nfs['DATA EMISSAO'] = pd.to_datetime(tabela_conciliacao_nfs['DATA EMISSAO']  , format='%d/%m/%Y')
tabela_conciliacao_nfs[transform_columns] = tabela_conciliacao_nfs[transform_columns].apply(
    lambda col: col.str.replace('.','').str.replace(',','.').astype(float)
)



# lista_meses = sorted(tabela_contas_pagar['DT VENCIMENTO'].str.strip().unique())
# print(tabela_contas_pagar.info())
# print(tabela_conciliacao_nfs.head())

