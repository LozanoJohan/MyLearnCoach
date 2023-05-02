# Impoertar las dependencias
import streamlit as st
import json

# Cargar los datos
with open('cursos.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Título
st.title("s")

# Caja de texto para el chat
prompt = st.text_input("d") 

# Sección de cursos
st.header("Cursos")

# Mostrar todos los cursos en 3 columnas
i = 0
for rows in range(len(data)//3):
    for col in st.columns(3):
        # Escribir nombre y código
        col.write(data[i]["nombre"] + data[i]["codigo"])
        i += 1






# Quita algunos elementos molestos
st.markdown("""
<style>
    .css-9s5bis.edgvbvh3 {
        visibility: hidden;
    }
.css-h5rgaw 
{
    visibility: hidden;
}
""", unsafe_allow_html=True)