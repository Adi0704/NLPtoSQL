from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
def get_conversation_chain():
    llm=ChatOpenAI()
    memory = ConversationBufferMemory(
        memory_key='history', return_messages=True)
    conversation_chain = ConversationChain(
        llm=llm,
        memory=memory
    )
    return conversation_chain
def generate_sql(question,schema):
    template = f"""Based on the table Schema below, write a SQL Query that answers the user's question:
    {schema}

    Question:{question}
    SQL Query:
    """
    prompt = ChatPromptTemplate.from_template(template)
    llm=ChatOpenAI()
    sql_chain = (
            prompt
            | llm.bind(stop=["\nSQL Result:"])  # Stop generation at 'SQL Result:'
            | StrOutputParser()
    )

    # Invoke the pipeline with input values
    return sql_chain.invoke({"schema": schema, "question": question})



def get_response(question, schema, sql,data):
    template = """Based on the table schema, question, SQL query, and SQL response, provide a structured, human-readable response. 
       Extract only the fields available in the response and format them properly.

       {schema}

       Question: {question}
       SQL Query: {query}
       SQL Response: {response}

       --- Structure the output dynamically: ---
       Name : Name of the person or persons,
       Similarly for other fields present in response and frame them in sentences giving a summary
       ----------------------------------------

       Ensure the response is direct and structured with clear labels.Using the structured data.form sentences
       If a field is not present, do not include it.
       """
    prompt_response = ChatPromptTemplate.from_template(template)
    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI()
    sql_chain = (
            prompt
            | llm
            | StrOutputParser()
    )
    # Invoke the pipeline with input values
    return sql_chain.invoke({"schema": schema, "question": question, "query": sql, "response": data})
