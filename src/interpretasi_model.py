import streamlit as st
import shap
import matplotlib.pyplot as plt

def app():
    st.header("🔍 Interpretasi Model")
    
    # Pastikan model dan X_test sudah ada di session_state
    if 'model' in st.session_state and 'X_test' in st.session_state:
        model = st.session_state['model']
        X_test = st.session_state['X_test']

        # Membuat explainer SHAP
        explainer = shap.Explainer(model.predict, X_test)
        shap_values = explainer(X_test)

        # SHAP Summary Plot
        st.subheader("SHAP Summary Plot")
        fig, ax = plt.subplots()
        shap.summary_plot(shap_values, X_test, plot_type='bar')
        st.pyplot(fig)
    else:
        st.warning("Model belum dilatih. Silakan latih model terlebih dahulu di bagian 'Klasifikasi Data'.")
