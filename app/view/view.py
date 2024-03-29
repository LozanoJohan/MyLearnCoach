import streamlit as st
from controllers.controller import Controller
from view.events_page import events_page
from view.home_page import home_page
from view.json_page import json_page



class View:
    def __init__(self):
        self.controller = Controller()
        self.data = self.controller.get_data()
        
        self.quit_ugly_widgets()

    def show(self):
            
        st.title('🎓 MyLearnCoach')

        page_names_to_funcs = {
            "🏠 Inicio": lambda : home_page(self),
            "📅 Eventos": events_page,
            '📊 Datos': json_page,
        }

        with st.sidebar:
            st.header('Menú')
            
            demo_name = st.selectbox("Escoge una página", page_names_to_funcs.keys())

            custom_api_key =st.text_input('Tu OpenAI API key', type = 'password', placeholder='Requerido')

            if custom_api_key:
                self.controller.set_api_key(custom_api_key)
            
            st.write('Puedes usar esta hasta que se acabe')
            st.write(f':green[{st.secrets["openai_api_key"]}]')
            st.write('¿No funciona? Prueba con tu <a href="https://platform.openai.com/account/api-keys">API key</a>', unsafe_allow_html=True)
            
        page_names_to_funcs[demo_name]()
    
    def quit_ugly_widgets(self):
        # Quita algunos elementos molestos
        st.set_page_config(layout="wide")

        # st.markdown("""
        # <style>
        #     .css-9s5bis.edgvbvh3 {
        #         visibility: hidden;
        #     }
        # .css-h5rgaw 
        # {
        #     visibility: hidden;
        # }
        # """, unsafe_allow_html=True)