from sqlalchemy import create_engine
from pandas.io import sql
import pandas as pd
data = pd.read_csv('input.csv')
engine = create_engine('sqlite:///:memory:')
# Store the Data in a relational table
data.to_sql('data_table', engine)
# Insert another row
sql.execute('INSERT INTO data_table VALUES(?,?,?,?,?,?)', engine, params=[('id',9,'Mahaveer',824.44,'2018-12-27','Electronics')])
# Read from the relational table
res = pd.read_sql_query('SELECT id,emp_name,emp_salary,start_date,dept FROM data_table', engine)
print(res)