import streamlit as st 
import pandas as pd
from utils import clean_data, compute_kpis, generate_summary

st.set_page_config(page_title="Nettoyage et Analyse de Données", layout="wide")
st.title('🧼 Application de nettoyage et analyse de données')

# Téléversement de fichier
uploaded_file = st.file_uploader("📂 Choisis un fichier CSV ou Excel", type=["csv", "xlsx"])
# Lecture du fichier
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.subheader("📄 Aperçu des données chargées :")
        st.dataframe(df.head())

        # 3. Bouton de nettoyage
        if st.button("🚀 Lancer le nettoyage"):
            df_clean = clean_data(df)

            st.success("Nettoyage terminé ✅")

            st.subheader("🧹 Données après nettoyage :")
            st.dataframe(df_clean.head())

            # 4. Afficher les KPIs
            st.subheader("📊 Statistiques descriptives :")
            st.dataframe(compute_kpis(df_clean))

            # 5. Bouton pour télécharger
            csv = df_clean.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ Télécharger le fichier nettoyé",
                data=csv,
                file_name="data_nettoyee.csv",
                mime="text/csv"
            )
    except Exception as e:
        st.error(f"Erreur lors de la lecture ou du traitement du fichier : {e}")
 