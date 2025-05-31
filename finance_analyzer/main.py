import pandas as pd
import matplotlib.pyplot as plt

from finance_analyzer.constants import DB_NAME
from finance_analyzer.script.sql_storage import get_connection
from finance_analyzer.script.transform import transform_data, get_monthly_spending, get_data_by_category
from finance_analyzer.utils import display_df, project_headline, print_bold_message

project_headline()

# Ingestion of data from the raw sources.
df = pd.read_csv("./data_file/raw/data.csv")
print("1.EXTRACT: Original Dataframe")
display_df(df)

# Transformation
transformed_df = transform_data(df)
print_bold_message("2.TRANSFORM: Transformed Dataframe")
display_df(transformed_df, style='fancy_grid')

# Loading into Database
conn = get_connection(name=DB_NAME)
print(f"Connection is established to the database {DB_NAME}...")
transformed_df.to_sql('transactions', conn, if_exists='append', index=False)
print_bold_message(f"3.LOAD: Data is stored in the database {DB_NAME}")
conn.close()
print("Connection Terminated.\n")

# Aggregation of Data
print_bold_message("4. Data Aggregation")
## Monthly spending
print_bold_message("Monthly Spending")
monthly_spending = get_monthly_spending(transformed_df)
display_df(monthly_spending)

## By category
print_bold_message("Spending by Category")
by_category = get_data_by_category(transformed_df)
display_df(by_category)

# Visualization of Data.
print_bold_message("5. Visualization of Data")

by_category.plot(kind='bar')
plt.title('Spending by Category')
plt.savefig('visuals/spending_by_category.png')
print("Visual is stored at visuals/spending_by_category.png")

monthly_spending.plot(kind='bar')
plt.title('Monthly Spending')
plt.savefig('visuals/monthly_spending.png')
print("Visual is stored at visuals/monthly_spending.png\n")

print_bold_message("Project Ends!")
