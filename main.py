from langchain_core.prompts import ChatPromptTemplate
template=f"""Based on the table Schema below, write a SQL Query that answers the user's question:
{schema}

Question:{question}
SQL Query:
"""

prompt=ChatPromptTemplate.from_template(template)