import streamlit as st 
import pandas as pd 

def clean_data(df):
    if not isinstance(df, pd.DataFrame):
        raise TypeError("L'objet fourni n'est pas un DataFrame pandas.")
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    df.drop_duplicates(inplace = True)
    
    numeric_col = df.select_dtypes(include='number').columns
    for col in numeric_col:
        df[col] = df[col].fillna(df[col].mean())
    return df

def compute_kpis(df):
    kpis = {
        "Nombre de lignes": df.shape[0],
        "Nombre de colonnes": df.shape[1],
        "Colonnes avec valeurs manquantes": df.isnull().sum()[df.isnull().sum() > 0].to_dict(),
        "Colonnes numériques": list(df.select_dtypes(include='number').columns),
        "Colonnes catégorielles": list(df.select_dtypes(include='object').columns)
    }
    return kpis

def generate_summary(df):

     # résumé statistique du DataFrame.
    return df.describe(include='all').transpose()