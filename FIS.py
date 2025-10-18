requirements.txt
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Configuration générale
st.set_page_config(page_title="FIS Dashboard App", page_icon="💡", layout="wide")

st.title("💡 FIS Dashboard App")
st.markdown("**Simulation complète du processus FIS : de la collecte des données aux actions correctives.**")

# Menu de navigation
menu = st.sidebar.radio(
    "🧭 Choisis un module :",
    ["Simulation", "Carte Mentale", "Storytelling", "Gamification", "IA Prédictive"]
)

# -------------------------------------------------------------
# 1️⃣ MODULE : Simulation interactive
# -------------------------------------------------------------
if menu == "Simulation":
    st.header("📊 Simulation du flux de données - Processus FIS")

    steps = ["Collecte des données", "Intégration FIS", "Autres outils", "Analyse Excel", "Actions correctives"]

    fig = go.Figure(go.Sankey(
        node=dict(
            pad=15,
            thickness=30,
            label=steps,
            color=["#4CAF50", "#2196F3", "#FFC107", "#9C27B0", "#E91E63"]
        ),
        link=dict(
            source=[0, 1, 2, 3],
            target=[1, 2, 3, 4],
            value=[10, 8, 6, 4]
        )
    ))

    st.plotly_chart(fig, use_container_width=True)

    st.info("Simulation du flux des données à travers les différentes étapes du processus FIS.")
    st.progress(100)
    st.success("✅ Processus complété avec succès !")

# -------------------------------------------------------------
# 2️⃣ MODULE : Carte mentale dynamique
# -------------------------------------------------------------
elif menu == "Carte Mentale":
    st.header("🧠 Carte mentale du processus FIS")

    G = nx.DiGraph()
    edges = [
        ("Collecte des données", "Intégration FIS"),
        ("Intégration FIS", "Autres outils"),
        ("Autres outils", "Analyse Excel"),
        ("Analyse Excel", "Actions correctives")
    ]
    G.add_edges_from(edges)

    pos = nx.spring_layout(G, seed=42)
    colors = ["lightgreen", "lightblue", "gold", "violet", "salmon"]

    fig, ax = plt.subplots(figsize=(7,5))
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=3000, font_size=9, font_weight="bold", arrows=True)
    ax.set_title("Carte mentale du flux de traitement FIS")
    st.pyplot(fig)
    st.caption("Visualisation des connexions logiques entre les étapes du processus.")

# -------------------------------------------------------------
# 3️⃣ MODULE : Storytelling visuel
# -------------------------------------------------------------
elif menu == "Storytelling":
    st.header("🎬 Storytelling - Évolution du processus FIS")

    df = pd.DataFrame({
        "Étape": ["Collecte", "FIS", "Autres outils", "Excel", "Actions"],
        "Progression": [10, 40, 60, 80, 100]
    })

    fig = px.bar(
        df, 
        x="Étape", 
        y="Progression", 
        text="Progression",
        title="📊 Évolution du processus FIS",
        animation_frame="Étape", 
        range_y=[0, 100]
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    ### 🧩 Description :
    - **Collecte** → Rassemblement des données brutes  
    - **FIS** → Intégration et nettoyage  
    - **Autres outils** → Analyses détaillées  
    - **Excel** → Synthèse des KPI  
    - **Actions** → Propositions correctives  
    """)

# -------------------------------------------------------------
# 4️⃣ MODULE : Dashboard Gamifié
# -------------------------------------------------------------
elif menu == "Gamification":
    st.header("🎮 Dashboard Gamifié - Progression du processus FIS")

    stages = {
        "Collecte des données": 1,
        "Intégration FIS": 2,
        "Autres outils": 3,
        "Analyse Excel": 4,
        "Actions correctives": 5
    }

    completed = st.slider("📈 Niveau de progression global :", 0, 5, 3)
    st.progress(completed / 5)

    for i, step in enumerate(stages, start=1):
        if i <= completed:
            st.success(f"✅ {step} - Terminée")
        else:
            st.warning(f"⏳ {step} - En attente")

    if completed == 5:
        st.balloons()
        st.success("🎉 Félicitations ! Toutes les étapes sont complétées avec succès !")

# -------------------------------------------------------------
# 5️⃣ MODULE : Simulation IA Prédictive
# -------------------------------------------------------------
elif menu == "IA Prédictive":
    st.header("🤖 Simulation IA - Impact des actions correctives")

    data = pd.DataFrame({
        "actions_correctives": [1, 2, 3, 4, 5],
        "taux_erreur": [20, 15, 10, 6, 3]
    })

    X = data[["actions_correctives"]]
    y = data["taux_erreur"]
    model = LinearRegression().fit(X, y)
    pred = model.predict(X)

    fig, ax = plt.subplots()
    ax.plot(X, y, "o-", label="Données réelles")
    ax.plot(X, pred, "--", label="Prédiction IA")
    ax.set_title("Impact des actions correctives sur le taux d’erreur")
    ax.set_xlabel("Nombre d’actions correctives")
    ax.set_ylabel("Taux d’erreur (%)")
    ax.legend()
    st.pyplot(fig)
    st.info("Cette simulation montre comment les actions correctives peuvent réduire les erreurs dans le système FIS.")
