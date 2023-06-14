from sia_scrapper import SiaScrapper
from coursera_scrapper import CourseraScrapper
import json
import os
from apikey import apikey
import streamlit as st 

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.show()

        os.environ['OPENAI_API_KEY'] = apikey
        self.set_llm()
    
    def fetch_sia_courses():
        sia = SiaScrapper()
        courses = sia.scrap()

        # Write courses to JSON file
        with open('sia_courses.json', 'w') as f:
            json.dump(courses, f)
            f.close()

        return courses
    
    def fetch_coursera_courses():
        coursera = CourseraScrapper()
        courses = coursera.scrap()

        # Write courses to JSON file
        with open('coursera_courses.json', 'w') as f:
            json.dump(courses, f)
            f.close()

        return courses
    
    def get_sia_courses():
        with open('sia_courses.json', 'r') as f:
            courses = json.load(f)
            f.close()

        return courses

    def get_coursera_courses():
        with open('coursera_courses.json', 'r') as f:
            courses = json.load(f)
            f.close()

        return courses
    
    def set_llm(self):
        
        self.title_template = PromptTemplate(
            input_variables = ['topic'], 
            template='{topic}'
        )

        self.script_template = PromptTemplate(
            input_variables = ['title'], 
            template='dame los temas que se necesitarian para entender la siguiente informacion INFORMACION: {title}'
        )

        self.llm = OpenAI(temperature=0.9) 

        self.title_chain = LLMChain(llm = self.llm, prompt = self.title_template, verbose = True, output_key = 'title')
        self.script_chain = LLMChain(llm = self.llm, prompt = self.script_template, verbose = True, output_key = 'script')
        self.sequential_chain = SequentialChain(chains = [self.title_chain, self.script_chain], 
                                                input_variables = ['topic'], 
                                                output_variables = ['title', 'script'], 
                                                verbose = True)
    
    def process_imput(self, input):

        response = self.sequential_chain({'topic': input})
        st.write(response['title'])
        st.write(response['script'])
