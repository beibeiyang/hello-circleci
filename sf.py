from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import pandas as pd
import os

engine = create_engine(URL(
    account = os.environ.get('SF_ACCOUNT'),
    user = os.environ.get('SF_USER'),
    password = os.environ.get('SF_PASSWORD'),
    database = os.environ.get('SF_DATABASE'),
    schema = os.environ.get('SF_SCHEMA'),
    warehouse = os.environ.get('SF_WAREHOUSE'),
    role = os.environ.get('SF_ROLE'),
))

try:
    query = """
    select sum("Net Sales Units") as "Unit Sales", "Inventory Name", "Retailer Name"
    from tablename
    where "Fiscal Week End Date"='2018-02-10'
    group by "Inventory Name", "Retailer Name"
    order by "Inventory Name", "Retailer Name"
    limit 10;
    """
    df = pd.read_sql_query(query, engine)
    print(df)
finally:
    engine.dispose()
