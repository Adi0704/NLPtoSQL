import streamlit as st
from sql import get_schema,run_query
from dotenv import load_dotenv
from bot import generate_sql,get_response
from langchain_community.utilities import SQLDatabase
mysql_uri = ''
db = SQLDatabase.from_uri(mysql_uri)
load_dotenv()
st.set_page_config(page_title="Online NLP to SQL",
                       page_icon=":books:")
st.header("Ask questions related to your data")
user_question = st.text_input("Ask a question about your documents:")
if user_question:
    # Function which gets schema of the metadata of the database
    schema=get_schema(db)
    # Function to generate sql given user_question and schema
    sql=generate_sql(user_question,schema)
    # To get data from the database once we run the sql in database
    data=run_query(db,sql)
    # To generate human text back to user
    st.write(get_response(user_question,schema,sql,data))
else:
    st.write('Please reframe')