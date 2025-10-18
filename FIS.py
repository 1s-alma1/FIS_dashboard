
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Low-Carbon FIS Dashboard", page_icon="🌱", layout="wide")

st.title("🌱 Low-Carbon FIS Dashboard")
st.markdown("**Simulation and tracking of low-carbon strategy using FIS tool.**")

# Sidebar menu
menu = st.sidebar.radio(
    "Select module:",
    ["Simulation", "Mind Map", "Gamification"]
)

# -------------------------------------------------------------
# 1️⃣ Simulation Module
# -------------------------------------------------------------
if menu == "Simulation":
    st.header("📊 Low-Carbon Strategy Process by using FIS Tool")

    steps = ["Data Collection", "FIS Integration", "Other Tools", "Excel Analysis", "Corrective Actions"]

    fig = go.Figure(go.Sankey(
        node=dict(
            pad=20,
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

    fig.update_layout(title_text="Low-Carbon Strategy Flow", font_size=12)
    st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------------------
# 2️⃣ Mind Map Module
# -------------------------------------------------------------
elif menu == "Mind Map":
    st.header("Carbon Strategy Process - Mind Map")

    G = nx.DiGraph()
    edges = [
        ("Data Collection", "FIS Integration"),
        ("FIS Integration", "Other Tools"),
        ("Other Tools", "Excel Analysis"),
        ("Excel Analysis", "Corrective Actions")
    ]
    G.add_edges_from(edges)

    pos = nx.spring_layout(G, seed=42)
    colors = ["lightgreen", "lightblue", "gold", "violet", "salmon"]

    fig, ax = plt.subplots(figsize=(8,5))
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=3500,
            font_size=10, font_weight="bold", arrows=True)
    ax.set_title("Carbon Strategy Process - Mind Map", fontsize=14)
    st.pyplot(fig)

# -------------------------------------------------------------
# 3️⃣ Gamification Module
# -------------------------------------------------------------
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
