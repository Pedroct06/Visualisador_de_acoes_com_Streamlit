import streamlit as st
import pandas as pd
import yfinance as yf

@st.cache_data
def carregar_dados(empresa, tempo, fim):
    dados = yf.Ticker(empresa)
    cotacoes = dados.history(start = tempo, end = fim)
    cotacoes = cotacoes[["Close"]]
    return cotacoes

st.write("""
# Visualização de Ações
Grafico para ver o desempenho de ações ao longo do tempo, e sua variação         
""")

tempo = st.date_input( "Forneça o ano de início da análise")

fim = st.date_input("Forneça até onde será analisado")

ticker = st.text_input(
    "Digite o código da ação desejada (ex: PETR4.SA, VALE3.SA, AAPL)",
    placeholder = "Sua ação aqui."
)


if st.button("Buscar ação") or ticker:
    if ticker == "" or tempo == "" or fim == "":
        st.warning("Código inexistente ou errado, por favor verifique!")
    else:
        try:
            with st.spinner(f"Carregando dados de {ticker}"):
                 dados = carregar_dados(ticker,tempo,fim)
            if dados.empty:
               st.error("Nenhuma ação encontrada!")
            
            else:

                st.subheader(f"Desempenho da ação {ticker}")
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("Preço atual", f"R$ {dados['Close'].iloc[-1]:.2f}")
                with col2:                     
                    variacao = dados['Close'].iloc[-1] - dados['Close'].iloc[0]
                    st.metric("Variacao total", f"R$ {variacao:.2f}")
                with col3:
                    percentual = ((dados['Close'].iloc[-1] / dados['Close'].iloc[0]) -1) * 100
                    st.metric("Variacao %", f"{percentual:.2f}")
                
                
                st.line_chart(dados)

        except Exception as e:
            st.error[f"Erro ao carregar os dados {e}, verifique se as ações estão no formato certo"]
        
st.write("Fim da analise, obrigado!")