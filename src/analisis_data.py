import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.header("📊 Analisis Data")
    if 'data' in st.session_state:
        data = st.session_state['data']

        # Pilih jenis analisis
        st.sidebar.header("Pengaturan Analisis")
        pilihan = st.sidebar.selectbox(
            "Pilih Analisis:",
            ["Distribusi Penjualan", "Tren Penjualan"]
        )

        if pilihan == "Distribusi Penjualan":
            st.subheader("Distribusi Penjualan Berdasarkan Lokasi")
            loc_counts = data['store_location'].value_counts()
            fig, ax = plt.subplots()
            sns.barplot(x=loc_counts.index, y=loc_counts.values, ax=ax, palette='pastel')
            ax.set_title("Distribusi Penjualan per Lokasi")
            ax.set_ylabel("Jumlah Transaksi")
            ax.set_xlabel("Lokasi")
            st.pyplot(fig)

        elif pilihan == "Tren Penjualan":
            st.subheader("Tren Penjualan Bulanan")
            data['transaction_month'] = pd.to_datetime(data['transaction_date']).dt.to_period('M')
            monthly_sales = data.groupby('transaction_month').size()
            fig, ax = plt.subplots()
            monthly_sales.plot(ax=ax, marker='o', color='blue')
            ax.set_title("Tren Penjualan Bulanan")
            ax.set_ylabel("Jumlah Transaksi")
            ax.set_xlabel("Bulan")
            st.pyplot(fig)

    else:
        st.warning("Silakan unggah data terlebih dahulu di menu 'Unggah Data'.")
