import pandas as pd
import matplotlib as plt
import seaborn as sns 

df_villes = pd.read_csv("data/MA.txt", sep='\t', header=None, encoding='utf-8')

df_villes.columns = [
    'geonameid', 'name', 'asciiname', 'alternatenames', 'latitude',
    'longitude', 'feature_class', 'feature_code', 'country_code',
    'cc2', 'admin1_code', 'admin2_code', 'admin3_code', 'admin4_code',
    'population', 'elevation', 'dem', 'timezone', 'modification_date'
]
# Liste des codes GeoNames qui correspondent à des villes
codes_villes = ['PPL', 'PPLA', 'PPLA2', 'PPLA3', 'PPLA4', 'PPLC']
df_villes = df_villes[df_villes['feature_code'].isin(codes_villes)]
df_villes = df_villes[df_villes['population'] > 80000]
df_villes = df_villes.drop_duplicates(subset='name')
df_villes[['name']].to_csv('data/villes_maroc.csv', index=False)

