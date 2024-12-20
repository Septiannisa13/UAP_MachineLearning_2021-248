import streamlit as st
from multiapp import MultiApp  
from upload_data import app as upload_data_app
from analisis_data import app as analisis_data_app
from klasifikasi_data import app as klasifikasi_data_app
from interpretasi_model import app as interpretasi_model_app

st.set_page_config(
    page_title="Dashboard Analisis & Klasifikasi Penjualan",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Dashboard Analisis & Klasifikasi Penjualan")
st.markdown("""
Selamat datang di aplikasi analisis dan klasifikasi penjualan. 
Gunakan menu navigasi di bawah untuk mengeksplorasi data, melakukan analisis, 
membangun model prediksi, dan memahami hasil dengan interpretasi model!
""")

# Inisialisasi MultiApp
app = MultiApp()
app.add_app("Unggah Data", upload_data_app)  # Changed from upload_app to upload_data_app
app.add_app("Analisis Data", analisis_data_app)  # Changed from analisis_app to analisis_data_app
app.add_app("Klasifikasi Data", klasifikasi_data_app)  # Changed from klasifikasi_app to klasifikasi_data_app
app.add_app("Interpretasi Model", interpretasi_model_app)  # Changed from interpretasi_model.py to interpretasi_model_app

app.run()
