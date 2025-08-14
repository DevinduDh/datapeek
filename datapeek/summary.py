import pandas as pd
from rich.console import Console
from rich.table import Table
from IPython.display import display

def dataframe_summary(df):
    """
    Display a summary table with columns as column names and rows as properties.
    - Terminal: Rich table
    - Jupyter Notebook: styled HTML
    """
    # Detect Jupyter Notebook
    try:
        shell = get_ipython().__class__.__name__
        in_jupyter = shell == "ZMQInteractiveShell"
    except NameError:
        in_jupyter = False

    # Prepare summary dictionary
    summary_dict = {
        "Datatype": [str(df[col].dtype) for col in df.columns],
        "Total Records": [df.shape[0] for _ in df.columns],
        "Unique Values": [df[col].nunique() for col in df.columns],
        "Missing Values": [df[col].isnull().sum() for col in df.columns],
    }

    if in_jupyter:
        # Jupyter: create transposed DataFrame
        summary_df = pd.DataFrame(summary_dict, index=df.columns).T

        # Style: missing values > 0 in red
        def highlight_missing(val):
            if val != 0 and isinstance(val, int):
                return 'color: red; font-weight: bold'
            return ''

        styled = summary_df.style.set_table_styles(
            [{'selector': 'th', 'props': [('background-color', '#4CAF50'), 
                                          ('color', 'white'),
                                          ('font-weight', 'bold')]}]
        ).set_properties(**{'text-align': 'center'}).applymap(highlight_missing, subset=pd.IndexSlice['Missing Values', :])

        display(styled)
    else:
        # Terminal: Rich table
        table = Table(title="DataPeek Summary", header_style="bold magenta")
        table.add_column("Property", style="bold yellow", justify="left")
        for col in df.columns:
            table.add_column(str(col), justify="center")

        for prop, values in summary_dict.items():
            row_values = []
            for v in values:
                if prop == "Missing Values" and v != 0:
                    row_values.append(f"[red]{v}[/red]")
                else:
                    row_values.append(str(v))
            table.add_row(prop, *row_values)

        console = Console()
        console.print(table)
