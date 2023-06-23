from dotenv import load_dotenv

from controllers.sia_scrapper import SiaScrapper
from controllers.coursera_scrapper import CourseraScrapper
from models.courses import SIACourse
from models.courses import CourseraCourse

import json
import os

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

'''Esto en caso de que nos quedemos sin apykey y no tengamos plata pa pagarla'''

from pathlib import Path
# Obtener la ruta absoluta del archivo 
json_path = Path(__file__).resolve().parent.parent / 'data' / 'courses_data.json'


class Controller:
    def __init__(self):

        load_dotenv()
        api_key = os.getenv('OPENAI_API_KEY')

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
            template = 'Escribe la o las palabras principales para poder buscar acerca de este tema: {title}'
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
        return response
    

    def get_sia_courses(self, query_type, query):
        courses = []

        # Read from json file
        with open(json_path, "r") as file:
            data = json.load(file)

        if query_type == 'Nombre':

            for course in data['SIACourses']:
                course_data = list(course.values())[0]

                if course_data['name'] == query:
                    courses.append(SIACourse(course_data['name'], 
                                         "course_data['professor']", 
                                         "course_data['description']", 
                                         course_data['code'], 
                                         course_data['credits'], 
                                         course_data['type']))
            
        elif query_type == 'Código':

            for course in data['SIACourses']:
                course_data = list(course.values())[0]

                if course_data['code'] == query:
                    courses.append(SIACourse(course_data['name'], 
                                         "course_data['professor']", 
                                         "course_data['description']", 
                                         course_data['code'], 
                                         course_data['credits'], 
                                         course_data['type']))
                    
        else:

            for course in data['SIACourses']:
                course_data = list(course.values())[0]
                courses.append(SIACourse(course_data['name'], 
                                         "course_data['professor']", 
                                         "course_data['description']", 
                                         course_data['code'], 
                                         course_data['credits'], 
                                         course_data['type']))

        return courses
    
    def get_coursera_courses(self, query:str):
        courses = []
        #import streamlit as st

        query = query.replace('"', '').lower()
        try:
            _ = query.split(':')
            #st.write(_[1])
            keywords = _[1].split(',')
        except:
            keywords = query.split(',')
        
        #for keyword in keywords:
            # st.write(keyword)
            # st.write(keyword in 'Introduction to Data Science')
        # Read from json file
        with open(json_path, "r") as file:
            data = json.load(file)

        for course_data in data['CourseraCourses']:

            for keyword in keywords:
                
                # st.write(course_data['name'].lower())
                # st.write('Keword:', keyword, 'Nombre:', course_data['name'].lower(), keyword in course_data['name'].lower())
                if keyword in course_data['name'].lower():

                    course = CourseraCourse(course_data['name'], 
                                         "course_data['professor']", 
                                         "course_data['description']", 
                                         course_data['url'], 
                                         "course_data['skills']", 
                                         course_data['score'],
                                         course_data['reviews']
                                         )
                    courses.append(course)

                    #st.markdown(f"**{course}**")
            
            
        return courses, keywords

