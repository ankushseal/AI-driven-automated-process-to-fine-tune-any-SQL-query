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
git clone https://github.com/ankushseal/AI-driven-automated-process-to-fine-tune-any-SQL-query.git
```

3. Run the Streamlit application:

```bash
streamlit run main.py
```

### License

This project is licensed under the MIT License.

---
