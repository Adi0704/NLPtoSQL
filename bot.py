from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
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
    template = """Based on the table schema below, question, sql query, and sql response, write a natural language response:
    {schema}

    Question: {question}
    SQL Query: {query}
    SQL Response: {response}"""
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
