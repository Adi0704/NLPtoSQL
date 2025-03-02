import streamlit as st
from sql import get_schema,run_query
from dotenv import load_dotenv
from bot import generate_sql,get_response,get_conversation_chain
from langchain_community.utilities import SQLDatabase
from htmlTemplates import css,bot_template,user_template
mysql_uri = ''
db = SQLDatabase.from_uri(mysql_uri)
load_dotenv()
st.set_page_config(page_title="Online NLP to SQL",
                       page_icon=":books:")
st.header("Ask Questions about your data 📊💬")

st.write(css,unsafe_allow_html=True)
if "conversation" not in st.session_state:
    st.session_state.conversation = get_conversation_chain()
if "messages" not in st.session_state:
    st.session_state.messages = []
user_question = st.text_input("Ask a question about your documents:")
if user_question:
    st.session_state.messages.append(("user", user_question))
    # Function which gets schema of the metadata of the database
    schema=get_schema(db)
    # Function to generate sql given user_question and schema
    sql=generate_sql(user_question,schema)
    # To get data from the database once we run the sql in database
    data=run_query(db,sql)
    # To generate human text back to user
    bot_response=get_response(user_question,schema,sql,data)
    st.session_state.messages.append(("bot", bot_response))

for role, msg in st.session_state.messages:
    if role == "user":
        st.write(user_template.replace("{{MSG}}", msg), unsafe_allow_html=True)
    else:
        st.write(bot_template.replace("{{MSG}}", msg), unsafe_allow_html=True)