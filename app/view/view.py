import streamlit as st
from controller import Controller

class View:
    def __init__(self):
        self.controller = Controller()
        
        self.quit_ugly_widgets()

    def show(self, controller, model):
        st.title('MyLearnCoach')

        prompt = st.text_input('¿En que te puedo ayudar?') 
    
        if prompt:
            controller.process_input(prompt)

        # Sección de cursos
        st.header("Cursos")

        # Mostrar todos los cursos en 3 columnas
        i = 0
        for rows in range(len(data)//3):
            for col in st.columns(3):
                # Escribir nombre y código
                col.write(data[i]["nombre"] + data[i]["codigo"])
                i += 1
    
    def quit_ugly_widgets(self):
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