
def run_query(db,query):
    return db.run(query)
def get_schema(db):
    return db.get_table_info()
