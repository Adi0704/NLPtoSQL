import streamlit as st
from sql import get_schema
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
mysql_uri = ''
db = SQLDatabase.from_uri(mysql_uri)
load_dotenv()
st.set_page_config(page_title="Online NLP to SQL",
                       page_icon=":books:")
st.header("Ask questions related to your data")
user_question = st.text_input("Ask a question about your documents:")
if user_question:
    st.write(get_schema(db))
else:
    st.write('Please reframe')