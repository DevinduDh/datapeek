import pandas as pd
from rich.console import Console
from rich.table import Table
from IPython.display import display

def dataframe_summary(df):
    """
    Display a nice summary table for a pandas DataFrame.
    - Terminal: Rich table with colors
    - Jupyter Notebook: Styled HTML DataFrame
    """
    # Detect Jupyter Notebook
    try:
        shell = get_ipython().__class__.__name__
        in_jupyter = shell == "ZMQInteractiveShell"
    except NameError:
        in_jupyter = False

    # Prepare summary data
    data = []
    for col in df.columns:
        data.append([
            col,
            str(df[col].dtype),
            df.shape[0],
            df[col].nunique(),
            df[col].isnull().sum()
        ])

    if in_jupyter:
        # Jupyter: show styled HTML table
        summary_df = pd.DataFrame(data, columns=[
            "Column", "Datatype", "Total Records", "Unique Values", "Missing Values"
        ])
        styled = summary_df.style.set_table_styles(
            [{'selector': 'th', 'props': [('background-color', '#4CAF50'), 
                                          ('color', 'white'),
                                          ('font-weight', 'bold')]}]
        ).set_properties(**{'text-align': 'center'})
        display(styled)
    else:
        # Terminal: show Rich table
        table = Table(title="DataPeek Summary", header_style="bold magenta")
        for header in ["Column", "Datatype", "Total Records", "Unique Values", "Missing Values"]:
            table.add_column(header, style="cyan" if header != "Missing Values" else "red", justify="center")

        for row in data:
            table.add_row(*[str(x) for x in row])

        console = Console()
        console.print(table)
