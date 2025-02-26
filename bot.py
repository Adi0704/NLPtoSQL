from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
def get_response(question,schema):
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