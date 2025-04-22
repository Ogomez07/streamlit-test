import streamlit as st
st.set_page_config(page_title="Tasador")
st.title("🏘️ Predicción de precios de pisos")
st.subheader("que lo que")

tab1, tab2 = st.tabs(["resumen", "Conatcto"])

with tab1:
    st.subheader("Resumen del proyecto")
    st.write("Este proyecto predice precio de pisos en Madrid")
    pass

with tab2:
    st.subheader("Contacto")
    st.write("Autor: yo")
    st.write("Correo: mi_mail@gmail.es")
    pass
