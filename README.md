## AI driven automated process to fine tune any SQL query.

This project provides an AI-driven automated process to fine-tune any SQL query using PostgreSQL and AWS Bedrock. The application is built using Streamlit for the user interface.

### Features

- **User Input**: Enter any SQL query to be fine-tuned.
- **Explain Plan**: Retrieve and display the explain plan from the PostgreSQL database.
- **AI Analysis**: Use AWS Bedrock to analyze the query and explain plan, providing suggestions for optimization.
- **Interactive UI**: Built with Streamlit for an easy-to-use interface.

### Installation

To run this project, you need to install the following libraries:

```bash
pip install psycopg2-binary boto3 langchain streamlit
```

### Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fine-tune-sql-query.git
cd fine-tune-sql-query
```

2. Create a file named `file_name.py` and paste the following code:

```python
import psycopg2
import boto3
from langchain.llms.bedrock import Bedrock
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import streamlit as st

st.title("FineTune your SQL Query")
query = st.text_input("Enter your query")
if st.button("Process"):
    conn = psycopg2.connect(
        host='',
        port=5432,
        user='',
        password='',
        database=''
    )
    
    cursor = conn.cursor()
    cursor.execute(f'Explain {query}')
    expplan = str(cursor.fetchall())
    st.subheader("Explain plan from DB")
    st.info(expplan)
    
    bedrock = boto3.client(service_name='bedrock-runtime',
                           region_name="us-east-1",
                           aws_access_key_id='',
                           aws_secret_access_key=''
                           )
    llm = Bedrock(model_id="amazon.titan-text-express-v1", client=bedrock,
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
    
    input = Prompt.format(query=query, expplan=expplan)
    conversation = ConversationChain(
        llm=llm, verbose=True, memory=ConversationBufferMemory()
    )
    
    output = llm.invoke(input)
    st.subheader("Suggestions")
    st.success(output)
```

3. Run the Streamlit application:

```bash
streamlit run file_name.py
```

### License

This project is licensed under the MIT License.

---

Feel free to customize the description and details as needed! If you have any other questions or need further assistance, let me know.
