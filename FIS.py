import streamlit as st
import plotly.graph_objects as go

# ---- PAGE CONFIG ----
st.set_page_config(page_title="FIS Low-Carbon Strategy", page_icon="🌿", layout="centered")

st.markdown("<h1 style='text-align:center; color:#1B5E20;'>🌿 FIS Low-Carbon Strategy</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555;'>Explore each step of the sustainability journey</p>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)

# ======================================================
# 🌍 INTERACTIVE TIMELINE (NARRATIVE FLOW)
# ======================================================

st.subheader("🧭 Interactive Low-Carbon Plan")

steps = {
    "Data Collection": {
        "color": "#2E7D32",
        "description": """
        📊 **Data Collection Phase**  
        - Collecte des données sur les émissions : énergie, transport, matériel, événements.  
        - Normalisation et préparation pour intégration FIS.  
        - Objectif : créer une base carbone fiable et complète.
        """
    },
    "FIS Integration": {
        "color": "#43A047",
        "description": """
        🔗 **Integration with FIS Tools**  
        - Liaison du modèle FIS pour quantifier les impacts carbone.  
        - Synchronisation avec les données Excel et tableaux de bord.  
        - Objectif : visualiser les indicateurs clés.
        """
    },
    "Excel Analysis": {
        "color": "#66BB6A",
        "description": """
        📈 **Excel & KPI Analysis**  
        - Analyse des indicateurs carbone.  
        - Comparaison inter-saisons et par site (Annecy, Chamonix, etc.).  
        - Objectif : identifier les écarts et leviers d’amélioration.
        """
    },
    "Corrective Actions": {
        "color": "#A5D6A7",
        "description": """
        ⚙️ **Corrective & Strategic Actions**  
        - Mise en œuvre des actions : mobilité durable, énergies vertes, recyclage matériel.  
        - Suivi via KPI FIS + retours terrain.  
        - Objectif : atteindre la neutralité carbone.
        """
    }
}

# --- Interactive Step Selector ---
selected_step = st.radio(
    "Sélectionnez une étape du plan 👇",
    list(steps.keys()),
    horizontal=True
)

# --- Diagram (bubbles) ---
fig = go.Figure()

for i, (step, info) in enumerate(steps.items()):
    fig.add_trace(go.Scatter(
        x=[i], y=[0],
        mode="markers+text",
        text=[step],
        textposition="middle center",
        textfont=dict(size=14, color="white"),
        marker=dict(size=110, color=info["color"], line=dict(width=3, color="#1B5E20")),
        hoverinfo="text"
    ))
    if i < len(steps) - 1:
        fig.add_annotation(
            x=i + 0.5, y=0,
            ax=i + 0.1, ay=0,
            showarrow=True, arrowhead=3, arrowsize=1.5, arrowwidth=2, arrowcolor="#2E7D32"
        )

fig.update_layout(
    showlegend=False,
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    height=300,
    plot_bgcolor="rgba(245,255,245,1)",
    paper_bgcolor="rgba(245,255,245,1)",
    margin=dict(l=20, r=20, t=40, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# --- Display Step Description Dynamically ---
st.markdown(f"<div style='background-color:{steps[selected_step]['color']}; padding:20px; border-radius:12px;'>"
            f"<div style='color:white; font-size:16px;'>{steps[selected_step]['description']}</div></div>",
            unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)


