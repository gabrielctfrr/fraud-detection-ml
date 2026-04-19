import sweetviz as sv
from src.data_loader import load_data

df = load_data("data/dataset.csv")

report = sv.analyze(df)
report.show_html("reports/eda_report.html")
