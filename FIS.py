import streamlit as st
import plotly.graph_objects as go
import numpy as np

# ---- PAGE CONFIG ----
st.set_page_config(page_title="FIS Low-Carbon Dashboard", page_icon="🌿", layout="wide")

# ---- HEADER ----
col1, col2, col3 = st.columns([1, 5, 1])
with col1:
    st.image("FIS_logo.png", width=90)
with col2:
    st.markdown("<h1 style='text-align:center; color:#1B5E20;'>🌿 Low-Carbon Strategy Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#555;'>Simplified view of sustainability progress using the FIS Tool</p>", unsafe_allow_html=True)
with col3:
    st.image("FFS_logo.png", width=90)

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)

# ---- SIDEBAR ----
menu = st.sidebar.radio("Select module:", ["Simulation", "Mind Map", "Progress"])

# ============================================================
# 1️⃣ SIMULATION MODULE - simple, clean, clear
# ============================================================
if menu == "Simulation":
    st.subheader("📊 Low-Carbon Strategy Process Simulation")

    st.markdown("""
    <p style='font-size:16px; color:#444;'>
    This simplified diagram shows the key stages of the Low-Carbon Strategy workflow using the <b>FIS Tool</b>.
    </p>
    """, unsafe_allow_html=True)

    steps = ["Data Collection", "FIS Integration", "Excel Analysis", "Corrective Actions"]
    colors = ["#2E7D32", "#43A047", "#66BB6A", "#A5D6A7"]

    fig = go.Figure()

    for i, step in enumerate(steps):
        fig.add_trace(go.Scatter(
            x=[i], y=[0],
            mode="markers+text",
            text=[step],
            textfont=dict(size=15, color="white"),
            textposition="middle center",
            marker=dict(size=100, color=colors[i], line=dict(width=3, color="#1B5E20")),
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
        height=350,
        plot_bgcolor="rgba(245,255,245,1)",
        paper_bgcolor="rgba(245,255,245,1)",
        margin=dict(l=40, r=40, t=40, b=40),
        title=dict(text="FIS Process Flow", x=0.5, font=dict(size=20, color="#1B5E20"))
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success("✅ Simulation completed — process successfully visualized.")

# ============================================================
# 2️⃣ MIND MAP MODULE - simple and elegant
# ============================================================
elif menu == "Mind Map":
    st.subheader("🧭 Low-Carbon Strategy - Mind Map")

    st.markdown("""
    <p style='font-size:16px; color:#444;'>
    Simple conceptual map connecting each stage of the Low-Carbon Strategy.
    </p>
    """, unsafe_allow_html=True)

    main = "Low-Carbon Strategy"
    branches = ["Data Collection", "FIS Integration", "Excel Analysis", "Corrective Actions"]

    # circular layout
    angles = np.linspace(0, 2 * np.pi, len(branches), endpoint=False)
    radius = 2.5
    x_main, y_main = 0, 0
    x_branches = radius * np.cos(angles)
    y_branches = radius * np.sin(angles)

    fig = go.Figure()

    # central node
    fig.add_trace(go.Scatter(
        x=[x_main], y=[y_main],
        mode="markers+text",
        text=[main],
        textfont=dict(size=16, color="white"),
        textposition="middle center",
        marker=dict(size=140, color="#2E7D32", line=dict(width=3, color="#1B5E20"))
    ))

    # branches
    for i, branch in enumerate(branches):
        fig.add_trace(go.Scatter(
            x=[x_main, x_branches[i]], y=[y_main, y_branches[i]],
            mode="lines",
            line=dict(color="#A5D6A7", width=3)
        ))
        fig.add_trace(go.Scatter(
            x=[x_branches[i]], y=[y_branches[i]],
            mode="markers+text",
            text=[branch],
            textfont=dict(size=14, color="#1B5E20"),
            textposition="middle center",
            marker=dict(size=90, color="#66BB6A", line=dict(width=3, color="#1B5E20"))
        ))

    fig.update_layout(
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        height=500,
        plot_bgcolor="rgba(245,255,245,1)",
        paper_bgcolor="rgba(245,255,245,1)",
        margin=dict(l=10, r=10, t=30, b=10),
        title=dict(text="Low-Carbon Strategy Mind Map", x=0.5, font=dict(size=20, color="#1B5E20"))
    )

    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# 3️⃣ PROGRESS MODULE - clean and automatic
# ============================================================
elif menu == "Progress":
    st.header("📈 Progress - Track Sustainability Implementation")

    st.markdown("""
    <p style='font-size:16px; color:#444;'>
    Adjust the progress for each step of your Low-Carbon Strategy.  
    The total completion rate updates automatically.
    </p>
    """, unsafe_allow_html=True)

    steps = ["Data Collection", "FIS Integration", "Excel Analysis", "Corrective Actions"]
    progress_values = {}

    # Individual Step Sliders
    for step in steps:
        progress_values[step] = st.slider(f"{step}", 0, 100, 0)

    # Automatic total progress
    total_progress = int(sum(progress_values.values()) / len(steps))

    st.markdown("---")
    st.subheader("🌍 Overall Process Completion")
    st.progress(total_progress)
    st.write(f"**Overall Progress:** {total_progress}%")

    if total_progress == 100:
        st.success("🎉 Excellent! Your low-carbon strategy is fully implemented.")
    elif total_progress >= 70:
        st.info("🚀 You’re on the right path — keep improving sustainability actions.")
    elif total_progress >= 30:
        st.warning("⚙️ Initial steps complete — continue refining your strategy.")
    else:
        st.error("🛠️ Strategy still at an early stage. Let’s take action soon!")

