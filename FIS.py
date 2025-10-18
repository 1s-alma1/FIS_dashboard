import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# ---- PAGE CONFIG ----
st.set_page_config(page_title="FIS Low-Carbon Dashboard", page_icon="🌍", layout="wide")

# ---- LOGO HEADER ----
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.image("FIS_logo.png", width=100)  # ← Replace with your logo file
with col2:
    st.markdown("<h1 style='text-align:center; color:#2E7D32;'>Low-Carbon Strategy Dashboard</h1>", unsafe_allow_html=True)
with col3:
    st.image("FFS_logo.png", width=100)  # ← Replace with your logo file

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)

# ---- SIDEBAR ----
menu = st.sidebar.radio(
    "Select module:",
    ["Simulation", "Mind Map", "Gamification"]
)

# ============================================================
# 1️⃣ SIMULATION MODULE
# ============================================================
if menu == "Simulation":
    st.subheader("📊 Low-Carbon Strategy Process using FIS Tool")

    st.markdown("""
    <p style='font-size:16px; color:#444;'>
    This simulation represents the data flow across the low-carbon process using the FIS tool.  
    </p>
    """, unsafe_allow_html=True)

    steps = [
        "Data Collection",
        "FIS Integration",
        "Supporting Tools",
        "Excel Analysis",
        "Corrective Actions"
    ]

    # Create a smooth horizontal process design
    fig = go.Figure()
    for i, step in enumerate(steps):
        fig.add_trace(go.Scatter(
            x=[i], y=[0],
            mode='markers+text',
            text=[step],
            textposition="bottom center",
            marker=dict(size=60, color="#4CAF50" if i==0 else "#81C784"),
            hoverinfo="text"
        ))
        if i < len(steps) - 1:
            fig.add_annotation(
                x=i + 0.5, y=0,
                ax=i, ay=0,
                xref='x', yref='y',
                axref='x', ayref='y',
                showarrow=True,
                arrowhead=3, arrowsize=1.5,
                arrowwidth=2,
                arrowcolor="#2E7D32"
            )

    fig.update_layout(
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        plot_bgcolor="white",
        margin=dict(l=0, r=0, t=20, b=20),
        height=300
    )

    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# 2️⃣ MIND MAP MODULE
# ============================================================
elif menu == "Mind Map":
    st.subheader("🧠 Carbon Strategy Process - Mind Map")

    st.markdown("""
    <p style='font-size:16px; color:#444;'>
    A structured representation of the low-carbon process stages and their interconnections.
    </p>
    """, unsafe_allow_html=True)

    # Define nodes and relationships
    G = nx.Graph()
    edges = [
        ("Low-Carbon Strategy", "Data Collection"),
        ("Low-Carbon Strategy", "FIS Integration"),
        ("Low-Carbon Strategy", "Supporting Tools"),
        ("Low-Carbon Strategy", "Excel Analysis"),
        ("Low-Carbon Strategy", "Corrective Actions")
    ]
    G.add_edges_from(edges)

    pos = nx.shell_layout(G)
    node_colors = ["#66BB6A" if node != "Low-Carbon Strategy" else "#2E7D32" for node in G.nodes]

    fig, ax = plt.subplots(figsize=(7, 5))
    nx.draw(
        G, pos, with_labels=True, node_color=node_colors,
        node_size=3500, font_size=9, font_weight="bold", font_color="white",
        edge_color="#A5D6A7"
    )
    ax.set_title("Carbon Strategy Process", fontsize=13, fontweight="bold")
    st.pyplot(fig)

# ============================================================
# 3️⃣ GAMIFICATION MODULE
# ============================================================
elif menu == "Gamification":
    st.header("🎮 Gamification - Track Progress for Each Step")

    steps = ["Data Collection", "FIS Integration", "Other Tools", "Excel Analysis", "Corrective Actions"]
    progress_values = {}

    for step in steps:
        progress_values[step] = st.slider(f"Progress for {step} (%)", 0, 100, 0)

    st.markdown("### Current Progress:")
    for step, value in progress_values.items():
        st.progress(value)
        st.write(f"{step}: {value}%")
