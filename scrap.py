import pandas as pd

df_d = pd.read_csv('../Data_Science_Post/survey_results_public.csv')
df_q = pd.read_csv('../Data_Science_Post/survey_results_schema.csv')

# Creating an excel spreadsheet for easier raw data visualization:

with pd.ExcelWriter('stack_data.xlsx',mode='w') as writer:
    df_d.to_excel(writer,sheet_name='Data',)
    df_q.to_excel(writer,sheet_name='Description')
