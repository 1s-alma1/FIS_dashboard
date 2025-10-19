# ======================================================
# 🌍 INTERACTIVE LOW-CARBON PLAN DIAGRAM
# ======================================================

st.subheader("🧭 FIS Low-Carbon Strategy — Interactive Overview")

st.markdown("""
<p style='font-size:16px; color:#444;'>
Explore each phase of the <b>Low-Carbon Strategy</b> by selecting a step below.  
Each stage reveals its detailed objectives and key sustainability actions.
</p>
""", unsafe_allow_html=True)

# --- Step data ---
steps_info = {
    "Data Collection": {
        "color": "#2E7D32",
        "description": """
        📊 **Data Collection Phase**  
        Collecte des données liées à l’énergie, au transport et au matériel sportif.  
        Objectif : établir une base carbone fiable et exhaustive.
        """
    },
    "FIS Integration": {
        "color": "#43A047",
        "description": """
        🔗 **Integration with FIS Tool**  
        Intégration du modèle FIS pour mesurer l’impact carbone global.  
        Objectif : synchroniser les données et visualiser les KPI environnementaux.
        """
    },
    "Excel Analysis": {
        "color": "#66BB6A",
        "description": """
        📈 **Excel Analysis**  
        Analyse des indicateurs carbone et comparaison des sites et saisons.  
        Objectif : identifier les leviers d’amélioration.
        """
    },
    "Corrective Actions": {
        "color": "#A5D6A7",
        "description": """
        ⚙️ **Corrective Actions**  
        Mise en œuvre d’actions concrètes : mobilité durable, énergies vertes, recyclage.  
        Objectif : tendre vers la neutralité carbone.
        """
    }
}

# --- Step selector (clickable buttons) ---
selected_step = st.radio(
    "Sélectionnez une étape du plan 👇",
    list(steps_info.keys()),
    horizontal=True
)

# --- Create interactive bubble diagram ---
import plotly.graph_objects as go

fig = go.Figure()

for i, (step, data) in enumerate(steps_info.items()):
    fig.add_trace(go.Scatter(
        x=[i], y=[0],
        mode="markers+text",
        text=[step],
        textposition="middle center",
        textfont=dict(size=15, color="white"),
        marker=dict(
            size=120 if step == selected_step else 100,  # plus grande si sélectionnée
            color=data["color"],
            line=dict(width=4 if step == selected_step else 2, color="#1B5E20"),
            opacity=1 if step == selected_step else 0.6
        ),
        hoverinfo="text"
    ))
    # Flèches entre les bulles
    if i < len(steps_info) - 1:
        fig.add_annotation(
            x=i + 0.5, y=0,
            ax=i + 0.1, ay=0,
            showarrow=True, arrowhead=3, arrowsize=1.5, arrowwidth=2, arrowcolor="#2E7D32"
        )

fig.update_layout(
    showlegend=False,
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    height=350,
    plot_bgcolor="rgba(245,255,245,1)",
    paper_bgcolor="rgba(245,255,245,1)",
    margin=dict(l=40, r=40, t=40, b=40),
)

st.plotly_chart(fig, use_container_width=True)

# --- Display the selected step description dynamically ---
st.markdown(
    f"""
    <div style='background-color:{steps_info[selected_step]["color"]}; 
                color:white; padding:20px; border-radius:15px; margin-top:15px;'>
        {steps_info[selected_step]["description"]}
    </div>
    """,
    unsafe_allow_html=True
)
