import matplotlib.pyplot as plt
import pandas as pd

def generate_plot(df: pd.DataFrame, x_col: str, y_col: str):
    """Generates a Matplotlib figure from the given DataFrame columns."""
    if x_col not in df.columns or y_col not in df.columns:
        return None  # Ensure we don't return a string

    fig, ax = plt.subplots(figsize=(6, 4))  # Ensure we return a figure
    ax.plot(df[x_col], df[y_col], marker='o', linestyle='-')
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(f"{y_col} vs {x_col}")
    
    return fig  # Return figure instead of string
