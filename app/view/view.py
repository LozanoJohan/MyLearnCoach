import streamlit as st
from controllers.controller import Controller
from view.events_page import events_page
from view.home_page import home_page
from view.json_page import json_page

class View:
    def __init__(self):
        self.controller = Controller()
        self.data = self.controller.get_data()
        
        #self.quit_ugly_widgets()

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
            
        page_names_to_funcs[demo_name]()
    
    def quit_ugly_widgets(self):
        # Quita algunos elementos molestos
        st.set_page_config(layout="wide")

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