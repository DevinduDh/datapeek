import pandas as pd
from tabulate import tabulate

def dataframe_summary(df):
    """
    Prints a summary of the dataframe with:
    - Column name
    - Datatype
    - Total records
    - Unique values
    - Missing values
    """
    summary = []
    for col in df.columns:
        summary.append([
            col,
            df[col].dtype,
            df.shape[0],
            df[col].nunique(),
            df[col].isnull().sum()
        ])
    print(tabulate(
        summary,
        headers=["Column", "Datatype", "Total Records", "Unique Values", "Missing Values"],
        tablefmt="github"
    ))
