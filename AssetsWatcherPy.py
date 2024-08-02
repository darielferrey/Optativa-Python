import streamlit as st
import pandas as pd
import yfinance as yf
import datetime

# Título de la aplicación
st.title("AssetsWatcherPy")

# Lista de criptomonedas y acciones (puedes personalizarlas)
criptomonedas = ['BTC-USD', 'ETH-USD', 'ADA-USD', 'BNB-USD', 'SOL-USD', 'DOT-USD', 'DOGE-USD', 'XRP-USD', 'LTC-USD', 'LINK-USD', 'TRX-USD', 'TON-USD', 'AVAX-USD', 'SHIB-USD', 'BCH-USD', 'XMR-USD', 'XLM-USD', 'ATOM-USD', 'MATIC-USD', 'CRO-USD']  # Nota: Se incluyen los pares con USD para yfinance
acciones = ['AAPL', 'INTC', 'NVDA', 'TSLA', 'F', 'AMD', 'BAC', 'AAL', 'PLUG', 'MARA', 'GOOGL', 'PFE', 'AMZN', 'NIO', 'T', 'CLSK', 'PLTR', 'LCID', 'NWL', 'BMY']

# Selección del tipo de activo
tipo_activo = st.selectbox("Selecciona el tipo de activo", ["Criptomonedas", "Acciones"])

# Secciones condicionales basadas en la selección
if tipo_activo == "Criptomonedas":
    # Selección de la fecha inicial
    fecha_inicial = st.date_input("Selecciona la fecha inicial", datetime.date(2014, 1, 1))

    # Selección de la criptomoneda
    cripto = st.selectbox("Selecciona una criptomoneda", criptomonedas)

    # Obtención de los datos históricos
    data = yf.download(cripto, start=fecha_inicial)

    # Gráfico de la criptomoneda
    st.line_chart(data['Close'])

else:
    # Selección de la fecha inicial
    fecha_inicial = st.date_input("Selecciona la fecha inicial", datetime.date(2014, 1, 1))

    # Selección de la acción
    accion = st.selectbox("Selecciona una acción", acciones)

    # Obtención de los datos históricos
    data = yf.download(accion, start=fecha_inicial)

    # Gráfico de la acción
    st.line_chart(data['Close'])