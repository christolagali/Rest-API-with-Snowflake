import snowflake.connector
from sqlalchemy import create_engine


class Connect:

    def __init__(self):
        self.user = None
        self.password = None
        self.account = None
        self.warehouse = None
        self.database = None
        self.snowflake_conn = None
    

    def getSnowflakeConnection(self,user,password,account,warehouse,dbname):
        
        snowflake_conn = snowflake.connector.connect(
                user=user,
                password=password,
                account=account,
                warehouse=warehouse,
                database=dbname
                )
        return snowflake_conn
    
    def execute_Query(self,query,conn):

        try:
            conn.cursor().execute(query)
        
        except Exception as e:
            print(e)
            