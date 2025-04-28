# src/preprocessing.py

import pandas as pd

def load_data(filepath):
    """Load the dataset from the given file path."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Clean the dataset by handling missing values and encoding categories."""

    # Example: Drop rows with missing target (rating) - very important
    df = df.dropna(subset=['rating'])

    # Fill missing values for simple columns
    df['genre'] = df['genre'].fillna('Unknown')
    df['director'] = df['director'].fillna('Unknown')
    df['actors'] = df['actors'].fillna('Unknown')

    # Encode categorical variables (simple Label Encoding for now)
    df['genre_encoded'] = df['genre'].astype('category').cat.codes
    df['director_encoded'] = df['director'].astype('category').cat.codes

    return df

def save_cleaned_data(df, output_path):
    """Save the cleaned dataset to a new file."""
    df.to_csv(output_path, index=False)
