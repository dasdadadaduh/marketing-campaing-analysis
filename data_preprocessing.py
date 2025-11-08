import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """Load marketing dataset from CSV/Excel file."""
    return pd.read_csv(filepath)

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and preprocess raw marketing data."""
    df = df.dropna()
    df['Date'] = pd.to_datetime(df['Date'])
    return df
