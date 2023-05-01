from pruebas.grid import Grid
import os

import streamlit as st

import json



# import plotly.graph_objects as go
import streamlit as st
#from plotly import express as px
#from plotly.subplots import make_subplots

with open('cursos.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

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
st.title("s")
prompt = st.text_input("d") 

st.header("Cursos")

i = 0

for rows in range(len(data)//3):
    #col1, col2, col3 = st.columns(3)
    for col in st.columns(3):
        col.write(data[i]["nombre"] + data[i]["codigo"])
        i += 1

#st.json(data)
from barfi import st_barfi, barfi_schemas, Block
import streamlit as st

from barfi import Block

feed = Block(name='Feed')
feed.add_output()
def feed_func(self):
    self.set_interface(name='Output 1', value=4)
feed.add_compute(feed_func)

splitter = Block(name='Splitter')
splitter.add_input()
splitter.add_output()
splitter.add_output()
def splitter_func(self):
    in_1 = self.get_interface(name='Input 1')
    value = (in_1/2)
    self.set_interface(name='Output 1', value=value)
    self.set_interface(name='Output 2', value=value)
splitter.add_compute(splitter_func)

mixer = Block(name='Mixer')
mixer.add_input()
mixer.add_input()
mixer.add_output()
def mixer_func(self):
    in_1 = self.get_interface(name='Input 1')
    in_2 = self.get_interface(name='Input 2')
    value = (in_1 + in_2)
    self.set_interface(name='Output 1', value=value)
mixer.add_compute(mixer_func)

result = Block(name='Result')
result.add_input()
def result_func(self):
    in_1 = self.get_interface(name='Input 1')
result.add_compute(result_func)

load_schema = st.selectbox('Select a saved schema:', barfi_schemas())

compute_engine = st.checkbox('Activate barfi compute engine', value=False)

barfi_result = st_barfi(base_blocks=[feed, result, mixer, splitter],
                    compute_engine=compute_engine, load_schema=load_schema)

if barfi_result:
    st.write(barfi_result)





with Grid("1 1 1") as grid:
        grid.cell(
            class_="a",
            grid_column_start=2,
            grid_column_end=3,
            grid_row_start=1,
            grid_row_end=2,
        ).markdown(data[0]["codigo"])
        grid.cell("b", 2, 3, 2, 3).text(data[0]["codigo"])
        grid.cell("e", 3, 4, 1, 2).markdown(
            "Try changing the **block container style** in the sidebar!"
        )
        grid.cell("f", 1, 3, 3, 4).text(
            "The cell to the right is a matplotlib svg image"
        )

