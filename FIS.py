import streamlit as st
import plotly.graph_objects as go
import networkx as nx
import matplotlib.pyplot as plt

# ---- PAGE CONFIG ----
st.set_page_config(page_title="FIS Low-Carbon Dashboard", page_icon="🌿", layout="wide")

# ---- HEADER WITH LOGOS ----
col1, col2, col3 = st.columns([1, 5, 1])
with col1:
    st.image("FIS_logo.png", width=90)
with col2:
    st.markdown(
        "<h1 style='text-align:center; color:#2E7D32;'>Low-Carbon Strategy Dashboard</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align:center; color:#555;'>Designed for data-driven sustainability management using the FIS Tool</p>",
        unsafe_allow_html=True,
    )
with col3:
    st.image("FFS_logo.png", width=90)

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)

# ---- SIDEBAR MENU ----
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
    This simulation shows the journey of data through each stage of the low-carbon process.  
    From raw data collection to corrective actions — all powered by the <b>FIS Tool</b>.
    </p>
    """, unsafe_allow_html=True)

    # --- PROCESS STEPS ---
    steps = ["Data Collection", "FIS Integration", "Supporting Tools", "Excel Analysis", "Corrective Actions"]
    colors = ["#4CAF50", "#66BB6A", "#81C784", "#A5D6A7", "#C8E6C9"]

    # --- Creative horizontal process design ---
    fig = go.Figure()

    for i, step in enumerate(steps):
        fig.add_trace(go.Scatter(
            x=[i], y=[0],
            mode="markers+text",
            text=[step],
            textfont=dict(size=14, color="#1B5E20"),
            textposition="bottom center",
            marker=dict(size=60, color=colors[i], line=dict(width=2, color="#2E7D32")),
            hoverinfo="text"
        ))

        # Arrows between steps
        if i < len(steps) - 1:
            fig.add_annotation(
                x=i + 0.5, y=0,
                ax=i + 0.1, ay=0,
                showarrow=True,
                arrowhead=3, arrowsize=1.3,
                arrowwidth=2,
                arrowcolor="#388E3C"
            )

    fig.update_layout(
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        plot_bgcolor="white",
        margin=dict(l=40, r=40, t=30, b=30),
        height=350,
        title=dict(text="FIS Process Flow", x=0.5, font=dict(size=20, color="#2E7D32"))
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success("Data successfully flows through all stages of the low-carbon process!")

# ============================================================
# 2️⃣ MIND MAP MODULE
# ============================================================
elif menu == "Mind Map":
    st.subheader("🧭 Carbon Strategy Process - Mind Map")

    st.markdown("""
    <p style='font-size:16px; color:#444;'>
    Visual representation of the low-carbon process, from data collection to corrective actions, 
    highlighting the interconnections of each component.
    </p>
    """, unsafe_allow_html=True)

    # --- Create graph ---
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
    node_colors = ["#2E7D32" if node == "Low-Carbon Strategy" else "#81C784" for node in G.nodes]

    fig, ax = plt.subplots(figsize=(7, 5))
    nx.draw(
        G, pos, with_labels=True, node_color=node_colors,
        node_size=3500, font_size=10, font_weight="bold", font_color="white",
        edge_color="#A5D6A7"
    )
    ax.set_title("Low-Carbon Process Mind Map", fontsize=14, color="#2E7D32", fontweight="bold")
    st.pyplot(fig)

# ============================================================
# 3️⃣ GAMIFICATION MODULE (kept as requested)
# ============================================================
elif menu == "Gamification":
    st.header("🎮 Gamification - Track Progress for Each Step")

    steps = ["Data Collection", "FIS Integration", "Other Tools", "Excel Analysis", "Corrective Actions"]
    progress_values = {}

    # --- Individual Step Sliders ---
    for step in steps:
        progress_values[step] = st.slider(f"Progress for {step} (%)", 0, 100, 0)

    st.markdown("### Current Progress:")
    for step, value in progress_values.items():
        st.progress(value)
        st.write(f"{step}: {value}%")

    # --- Global Progress Slider ---
    st.markdown("---")
    st.subheader("📈 Overall Process Completion")
    total_progress = st.slider("Total process completion (%)", 0, 100, 50)
    st.progress(total_progress)
    st.write(f"**Overall Low-Carbon Strategy Progress:** {total_progress}%")

    if total_progress == 100:
        st.success("🎉 Excellent! Your low-carbon strategy is fully implemented.")
    elif total_progress >= 70:
        st.info("🚀 You’re on the right path — keep improving sustainability actions.")
    elif total_progress >= 30:
        st.warning("⚙️ Initial steps complete — continue refining your strategy.")
    else:
        st.error("🛠️ Strategy still at early stage. Let’s take action soon!")

