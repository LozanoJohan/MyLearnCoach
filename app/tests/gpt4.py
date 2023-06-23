from getpass import getpass
from langchain import LLMChain, HuggingFaceHub, PromptTemplate
from langchain.llms import GPT4All

local_path = (
    "C:/Users/Usuario/AppData/Local/nomic.ai/GPT4All/ggml-mpt-7b-chat.bin"  # replace with your desired local file path
)

llm = GPT4All(model=local_path, verbose=True)



# HUGGINGFACEHUB_API_TOKEN = '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'

# import os

# os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN
# print(HUGGINGFACEHUB_API_TOKEN)

# repo_id = "stabilityai/stablelm-tuned-alpha-3b"
# llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0, "max_length": 64})



template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "Who won the FIFA World Cup in the year 1994? "

llm_chain = LLMChain(prompt=prompt, llm=llm)
print(llm_chain.run(question))