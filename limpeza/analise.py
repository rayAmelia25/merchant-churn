import pandas as pd
from data_profiling import ProfileReport

dados = 'data/merchant_churn.csv'
df = pd.read_csv(dados)
#print(df.head())
#print(df.info())

profile = ProfileReport(df, title="Profiling Report")
profile.to_file("reports/eda.html")