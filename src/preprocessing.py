import pandas as pd
def clean_data(df):
    df = df.drop_duplicates()
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

    for column in numeric_columns:
        df[column].fillna(df[column].mean(), inplace=True)
    categorical_columns = df.select_dtypes(include=['object']).columns

    for column in categorical_columns:
        df[column].fillna(df[column].mode()[0], inplace=True)
    return df
