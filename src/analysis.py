def generate_statistics(df):
    return df.describe()


def generate_insights(df):
    insights = []
    avg_income = df['AnnualIncome'].mean()
    avg_purchase = df['PurchaseAmount'].mean()
    insights.append(f'Average Annual Income: {avg_income}')
    insights.append(f'Average Purchase Amount: {avg_purchase}')
    highest_spender = df.loc[df['PurchaseAmount'].idxmax()]
    insights.append(
        f'Highest spender belongs to city: {highest_spender["City"]}'
    )
    return insights
