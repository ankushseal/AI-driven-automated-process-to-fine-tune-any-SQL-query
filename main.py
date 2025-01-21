import psycopg2
import boto3
from langchain.llms.bedrock import Bedrock
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import streamlit as st
#while True :
  
st.title("FineTune your SQL Query")
query= st.text_input("Enter your query")
if st.button("Process"):
  conn = psycopg2.connect(
    host='',
    port=5432,
    user='',
    password='',
    database=''
  )
  
  #query = " select count(*) from customers"
  # Create a cursor object to execute SQL commands
  cursor = conn.cursor()
  cursor.execute(f'Explain {query}')
  expplan = str(cursor.fetchall())
  print("========================================")
  print(expplan)
  st.subheader("Explain plan from DB")
  st.info(expplan)
  
  bedrock=boto3.client(service_name='bedrock-runtime',
                       region_name="us-east-1",
                       aws_access_key_id= '',
                       aws_secret_access_key=''
                       )
  llm=Bedrock(model_id="amazon.titan-text-express-v1",client=bedrock,
                  model_kwargs={"maxTokenCount": 5000})
  
  Prompt = """
  We are providing you with a PostgreSQL query and an explain plan generated with the `EXPLAIN` statement from a PostgreSQL DB. Analyze the query with the explain plan to fine-tune the query. Mention all the specific steps that need to be taken to fine-tune the query. If modification of the query is possible, provide the modified query. If no modification is required, indicate so.
  **Query**:
  ```sql
  {query}
  ```
  **Explain Plan**:
  ```sql
  {expplan}
  ```
  Provide the steps to fine-tune the query. If you suggest any query modifications, use proper spacing so it's easy to distinguish. 
  """
  
  input = Prompt.format(query=query,expplan=expplan)
  conversation = ConversationChain(
    llm=llm, verbose=True, memory=ConversationBufferMemory()
  )
  
  output=llm.invoke(input)
  st.subheader("Suggestions")
  st.success(output)
