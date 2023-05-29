import os
from apikey import apikey
import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

os.environ['OPENAI_API_KEY'] = apikey
st.title('MyLearnCoach')
prompt = st.text_input('¿En que te puedo ayudar?') 

title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='{topic}'
)

script_template = PromptTemplate(
    input_variables = ['title'], 
    template='dame los temas que se necesitarian para entender la siguiente informacion INFORMACION: {title}'
)


llm = OpenAI(temperature=0.9) 
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title')
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script')
sequential_chain = SequentialChain(chains=[title_chain,script_chain], input_variables=['topic'], output_variables=['title', 'script'], verbose=True)

if prompt:
    response= sequential_chain({'topic':prompt})
    st.write(response['title'])
    st.write(response['script'])
