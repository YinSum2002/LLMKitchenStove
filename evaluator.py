import os
import openai

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Store the API key in a variable called OPEN_API_KEY
OPEN_API_KEY = "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"
# Set the openai.api_key using the OPEN_API_KEY variable
openai.api_key = OPEN_API_KEY

# Set the environment variable OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = OPEN_API_KEY

llm = ChatOpenAI()
command = ""


def photo_analysis(command, topic):
    prompt = ChatPromptTemplate.from_template(command)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.predict(input=topic)
