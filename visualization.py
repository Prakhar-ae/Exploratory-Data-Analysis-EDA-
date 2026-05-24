import matplotlib.pyplot as plt
import seaborn as sns

def plot_histograms(df):
    df.hist(figsize=(12, 8))
    plt.tight_layout()
    plt.savefig('images/histogram.png')
    plt.show()

def plot_bar_chart(df):
    sns.countplot(x='Gender', data=df)
    plt.title('Gender Distribution')
    plt.savefig('images/bar_chart.png')
    plt.show()

def plot_correlation_heatmap(df):
    plt.figure(figsize=(10, 6))
    correlation = df.corr(numeric_only=True)
    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.savefig('images/heatmap.png')
    plt.show()

def plot_boxplot(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df['PurchaseAmount'])
    plt.title('Purchase Amount Boxplot')
    plt.savefig('images/boxplot.png')
    plt.show()