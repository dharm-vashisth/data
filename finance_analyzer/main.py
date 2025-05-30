import pandas as pd

from finance_analyzer.script.sql_storage import get_connection
from finance_analyzer.script.transform import transform_data, get_monthly_spending, get_data_by_category
from finance_analyzer.utils import display_df, project_headline

print("Program Started...")
project_headline()

# Extracting
df = pd.read_csv("./data_file/raw/data.csv")
print("Original Dataframe")
display_df(df)

# Transformation
transformed_df = transform_data(df)
print("Transformed Dataframe")
display_df(transformed_df, style='fancy_grid')

# Loading into Database
conn = get_connection()
transformed_df.to_sql('transactions', conn, if_exists='append', index=False)
conn.close()

print("Project Ends")
