from src.data_loader import load_data
from src.preprocessing import clean_data
from src.visualization import (
    plot_histograms,
    plot_bar_chart,
    plot_correlation_heatmap,
    plot_boxplot
)
from src.analysis import generate_statistics, generate_insights

file_path = 'data/customer_data.csv'
df = load_data(file_path)
df = clean_data(df)
print('\nFirst Five Rows:\n')
print(df.head())
print('\nDataset Information:\n')
print(df.info())
print('\nStatistical Summary:\n')
print(generate_statistics(df))
plot_histograms(df)
plot_bar_chart(df)
plot_correlation_heatmap(df)
plot_boxplot(df)
print('\nGenerated Insights:\n')
insights = generate_insights(df)
for insight in insights:
    print('-', insight)