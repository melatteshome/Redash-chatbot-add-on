#importing libraries
from langchain.llms.openai import OpenAI
from dotenv import main
main.load_dotenv()
from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import AgentExecutor
from langchain.sql_database import SQLDatabase
import psycopg2
from langchain_community.llms import OpenAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.chat_models import ChatOpenAI
import os
api_key = os.environ.get('OPENAI_API_KEY')

#connecting to sql and creating an agent
db = SQLDatabase.from_uri('postgresql+psycopg2://postgres:postgres@localhost/YoutubeDB')
print(db)

# #intinializing the llm
# llm = OpenAI(model_name = 'gpt-3.5-turbo')

# #initialising the toolkit
# toolkit = SQLDatabaseToolkit(db=db, llm=llm)
# #creating the agent
# agent_executer= create_sql_agent(
#     llm=llm,
#     toolkit=toolkit,
#     verbose= True
# )
#loading the api_key
llm = llm = ChatOpenAI(openai_api_key= api_key
)
#creating a db chain
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

#using the chain to run a query
db_chain.run("show all tables in the YoutubeDB")

#creating a tempate for sql queries and responses
from langchain.prompts import PromptTemplate

TEMPLATE = """Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
Use the following format:

Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"
Only use the tables found in the YoutubeDB.

Some examples of SQL queries that correspond to questions are:

{few_shot_examples}

Question: {show all tables in the YoutubeDB}"""

CUSTOM_PROMPT = PromptTemplate(
    input_variables=["input", "few_shot_examples", "table_info", "dialect"],
    template=TEMPLATE,
)
