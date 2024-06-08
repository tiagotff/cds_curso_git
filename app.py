import streamlit as st
from src.extraction import load_data

st.set_page_config(layout='wide')

def create_dataframe_section(df):
    st.title("Database section")
    
    col_1, col_2 = st.columns(2)
    
    col_1.header("Database")
    col_1.dataframe(df, height=530)
    
    col_2.header("Data Description")
    
    data_description = """
                        | Coluna | Descrição |
                        | :----- | --------: |
                        | ID | Identificador da linha/registro |
                        | name | fabricante e Modelo da Moto |
                        | selling_price | Preço de Venda |
                        | year | Ano de Fabricação da Moto |
                        | seller_type | Tipo de Vendedor - Se é vendedor pessoal ou revendedor |
                        | owner | Se é primeiro, segundo, terceiro ou quarto dono da moto |
                        | km_driven | Quantidade de Quilômetros percorridos pela moto |
                        | ex_showroom_price | Preço da motocicleta sem as taxas de seguro e registro |
                        | age | Quantidade de anos em que a moto está em uso |
                        | km_class | Classificação das motos conforme a quilometragem percorrida |
                        | km_per_year | Quantidade de quilômetros percorridos a cada ano |
                        | km_per_month | Quantidade de quilômetros percorridos por mês |
                        | company | Fabricante da Motocicleta |    
    """
    col_2.markdown(data_description)
    
    return None

def main():
    df_raw = load_data()
    
    st.dataframe(df_raw)
    
if __name__ == '__main__':
    main()
    