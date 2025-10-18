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
    st.markdown("<h1 style='text-align:center; color:#2E7D32;'>Low-Carbon Strategy Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#555;'>Visualizing sustainability progress using the FIS Tool</p>", unsafe_allow_html=True)
with col3:
    st.image("FFS_logo.png", width=90)

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)

# ---- SIDEBAR ----
menu = st.sidebar.radio("Select module:", ["Simulation", "Mind Map", "Gamification"])

# ============================================================
# 1️⃣ SIMULATION MODULE
# ============================================================
if menu == "Simulation":
    st.subheader("📊 Low-Carbon Strategy Process Simulation")

    st.markdown("""
    <p style='font-size:16px; color:#444;'>
    This section illustrates how data flows through the different steps of the low-carbon strategy.  
    From collection to corrective actions, everything integrates through the <b>FIS Tool</b>.
    </p>
    """, unsafe_allow_html=True)

    steps = ["Data Collection", "FIS Integration", "Supporting Tools", "Excel Analysis", "Corrective Actions"]
    colors = ["#2E7D32", "#43A047", "#66BB6A", "#81C784", "#A5D6A7"]

    # Create better process flow with Plotly annotations
    fig = go.Figure()

    for i, step in enumerate(steps):
        fig.add_trace(go.Scatter(
            x=[i], y=[0],
            mode="markers+text",
            text=[step],
            textfont=dict(size=16, color="white"),
            textposition="top center",
            marker=dict(size=80, color=colors[i], line=dict(width=3, color="#1B5E20")),
            hoverinfo="text"
        ))
        if i < len(steps) - 1:
            fig.add_annotation(
                x=i + 0.5, y=0,
                ax=i + 0.1, ay=0,
                xref="x", yref="y",
                showarrow=True,
                arrowhead=3, arrowsize=1.5, arrowwidth=2, arrowcolor="#2E7D32"
            )

    fig.update_layout(
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        plot_bgcolor="rgba(245, 255, 245, 1)",
        paper_bgcolor="rgba(245, 255, 245, 1)",
        height=400,
        title=dict(text="FIS Process Flow", x=0.5, font=dict(size=22, color="#1B5E20"))
    )

    st.plotly_chart(fig, use_container_width=True)
    st.success("✅ Data successfully flows through the Low-Carbon Strategy process.")

# ============================================================
# 2️⃣ MIND MAP MODULE
# ============================================================
elif menu == "Mind Map":
    st.subheader("🧭 Low-Carbon Strategy - Mind Map")

    st.markdown("""
    <p style='font-size:16px; color:#444;'>
    A visual representation of the Low-Carbon process. Each node represents a stage connected to the main strategy center.
    </p>
    """, unsafe_allow_html=True)

    main = "Low-Carbon Strategy"
    branches = ["Data Collection", "FIS Integration", "Supporting Tools", "Excel Analysis", "Corrective Actions"]

    # Define positions (radial layout)
    angles = np.linspace(0, 2 * np.pi, len(branches), endpoint=False)
    x_main, y_main = 0, 0
    x_branches = np.cos(angles)
    y_branches = np.sin(angles)

    # Plot with Plotly
    fig = go.Figure()

    # Add central node
    fig.add_trace(go.Scatter(
        x=[x_main], y=[y_main],
        mode="markers+text",
        text=[main],
        textfont=dict(size=16, color="white"),
        textposition="middle center",
        marker=dict(size=130, color="#2E7D32", line=dict(width=3, color="#1B5E20"))
    ))

    # Add branches and connections
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
            marker=dict(size=90, color="#81C784", line=dict(width=3, color="#2E7D32"))
        ))

    fig.update_layout(
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        plot_bgcolor="rgba(245, 255, 245, 1)",
        paper_bgcolor="rgba(245, 255, 245, 1)",
        margin=dict(l=10, r=10, t=10, b=10),
        height=500,
        title=dict(text="Low-Carbon Strategy Mind Map", x=0.5, font=dict(size=20, color="#1B5E20"))
    )

    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# 3️⃣ GAMIFICATION MODULE (auto total progress)
# ============================================================
elif menu == "Gamification":
    st.header("🎮 Gamification - Track Progress for Each Step")

    st.markdown("""
    <p style='font-size:16px; color:#444;'>
    Adjust the progress of each phase and monitor your overall low-carbon implementation rate automatically.
    </p>
    """, unsafe_allow_html=True)

    steps = ["Data Collection", "FIS Integration", "Other Tools", "Excel Analysis", "Corrective Actions"]
    progress_values = {}

    # Individual Step Sliders
    for step in steps:
        progress_values[step] = st.slider(f"Progress for {step} (%)", 0, 100, 0)

    st.markdown("### Current Progress:")
    for step, value in progress_values.items():
        st.progress(value)
        st.write(f"{step}: {value}%")

    # Automatic overall progress
    total_progress = int(sum(progress_values.values()) / len(steps))
    st.markdown("---")
    st.subheader("📈 Overall Process Completion")
    st.progress(total_progress)
    st.write(f"**Overall Low-Carbon Strategy Progress:** {total_progress}%")

    # Feedback messages
    if total_progress == 100:
        st.success("🎉 Excellent! Your low-carbon strategy is fully implemented.")
    elif total_progress >= 70:
        st.info("🚀 You’re on the right path — keep improving sustainability actions.")
    elif total_progress >= 30:
        st.warning("⚙️ Initial steps complete — continue refining your strategy.")
    else:
        st.error("🛠️ Strategy still at an early stage. Let’s take action soon!")
