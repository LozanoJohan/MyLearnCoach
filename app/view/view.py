import streamlit as st
from controllers.controller import Controller

class View:
    def __init__(self):
        self.controller = Controller()
        self.data = self.controller.get_data()
        
        self.quit_ugly_widgets()

    def show(self):
        st.title('MyLearnCoach')

        prompt = st.text_input('¿En que te puedo ayudar?') 
    
        if prompt:
            self.controller.process_input(prompt)

        # Sección de cursos
        st.header("Cursos")

        # Mostrar todos los cursos en 3 columnas
        i = 0
        # for rows in range(len(self.data['SIACourses'])//3):
        #     for col in st.columns(3):
        #         # Escribir nombre y código
        #         col.write(self.data['SIACourses'][i]["name"] + self.data['SIACourses'][i]["code"])
        #         i += 1
    
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