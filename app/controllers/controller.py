from controllers.apikey import apikey

from controllers.sia_scrapper import SiaScrapper
from controllers.coursera_scrapper import CourseraScrapper
from models.courses import SIACourse

import json
import os
import streamlit as st 

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

'''Esto en caso de que nos quedemos sin apykey y no tengamos plata pa pagarla'''

# from langchain.llms import GPT4All

# # Get GPT4All model
# local_path = (
#     "D:/Users/Usuario/Documents/GitHub/MyLearnCoach/app/GPT4All-13B-snoozy.ggmlv3.q4_0.bin"  # replace with your desired local file path
# )
json_path = '../app/data/courses_data.json'

class Controller:
    def __init__(self): # , view):
        # self.view = view

        # self.view.show()

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
    
    def fetch_coursera_courses(self):
        coursera = CourseraScrapper()
        courses = coursera.scrap()

        # Write courses to JSON file
        with open('coursera_courses.json', 'w') as f:
            json.dump(courses, f)
            f.close()

        return courses
    
    def get_data(self):
        # Read courses from JSON file
        with open(json_path, 'r') as f:
            courses = json.load(f)
            f.close()

        return courses
    
    def set_llm(self):
        
        template = """Question: {question}

        Respuesta:."""

        self.title_template = PromptTemplate(
            input_variables = ['topic'], 
            template='{topic}'
        )

        self.script_template = PromptTemplate(
            input_variables = ['title'], 
            template = 'Escribe la o las palabras principales para poder buscar acerca de este tema: {title}' #'dame los temas que se necesitarian para entender la siguiente informacion INFORMACION: {title}'
        )

        #self.llm = GPT4All(model=local_path, verbose=True)
        self.llm = OpenAI(verbose=True, temperature=0.7)

        self.title_chain = LLMChain(llm = self.llm, prompt = self.title_template, verbose = True, output_key = 'title')
        self.script_chain = LLMChain(llm = self.llm, prompt = self.script_template, verbose = True, output_key = 'script')
        
        self.sequential_chain = SequentialChain(chains = [self.title_chain, self.script_chain], 
                                                input_variables = ['topic'], 
                                                output_variables = ['title', 'script'], 
                                                verbose = True)
    
    def process_input(self, input):

        response = self.sequential_chain({'topic': input})
        st.write(response['title'])
        st.write(response['script'])
    

    def get_sia_courses(self, query):
        from pathlib import Path
        courses = []
        
        # Read from json file
        with open(json_path, "r") as file:
            data = json.load(file)
            for course in data['SIACourses']:
                course_data = list(course.values())[0]
                courses.append(SIACourse(course_data['name'], 
                                         "course_data['professor']", 
                                         "course_data['description']", 
                                         course_data['code'], 
                                         course_data['credits'], 
                                         course_data['type']))

        return courses
