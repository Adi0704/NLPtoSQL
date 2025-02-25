from langchain_community.utilities import SQLDatabase
mysql_uri=''
db=SQLDatabase.from_uri(mysql_uri)
def get_schema(db):
    schema=db.get_table_info()
    return schema
print(get_schema(db))