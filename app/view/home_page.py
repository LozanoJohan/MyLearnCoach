import streamlit as st

def home_page(view):

    st.balloons()
    prompt = st.text_input('¿En que te puedo ayudar?') 
    
    if prompt:
        view.controller.process_input(prompt)

    # Sección de cursos
    st.header("Cursos")

    # Mostrar todos los cursos en 3 columnas
    i = 0
    # for rows in range(len(self.data['SIACourses'])//3):
    #     for col in st.columns(3):
    #         # Escribir nombre y código
    #         col.write(self.data['SIACourses'][i]["name"] + self.data['SIACourses'][i]["code"])
        #         i += 1