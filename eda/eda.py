import sweetviz as sv
from src.data_loader import load_data

df = load_data('data/dataset.csv')
df_info = sv.analyze(df)
df_info.show_html('reports/eda_report.html')

print(df.info())
print(df.describe())
print(df.unique())