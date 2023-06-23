import streamlit as st
from controllers.controller import Controller

def home_page(view):

    st.balloons()
    prompt = st.text_input('¿En que te puedo ayudar?') 
    
    if prompt:
        view.controller.process_input(prompt)

    # Sección de cursos
    st.header("Cursos")
    
    # Mostrar todos los cursos en 3 columnas
    i = 0

    sia_courses = Controller().get_sia_courses(None)

    for rows in range(len(sia_courses)//3):
        for col in st.columns(3):
            # Escribir nombre y código
            col.markdown(f'**{sia_courses[i].name}** {sia_courses[i].code}')
            i += 1

        st.divider()