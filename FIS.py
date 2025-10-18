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
    st.markdown("<p style='text-align:center; color:#555;'>Visualizing sustainability progress using the FIS Tool</p>", unsafe_allow_html=True)
with col3:
    st.image("FFS_logo.png", width=90)

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)

# ---- SIDEBAR ----
menu = st.sidebar.radio("Select module:", ["Simulation", "Mind Map", "Gamification"])

# ============================================================
# 1️⃣ SIMULATION MODULE - Creative and clean flow
# ============================================================
if menu == "Simulation":
    st.subheader("📊 Low-Carbon Strategy Process Simulation")

    st.markdown("""
    <p style='font-size:16px; color:#444;'>
    This simulation illustrates the complete low-carbon workflow using the FIS Tool — 
    from data collection to implementing corrective actions.
    </p>
    """, unsafe_allow_html=True)

    steps = [
        "Data Collection",
        "FIS Integration",
        "Supporting Tools",
        "Excel Analysis",
        "Corrective Actions"
    ]

    # coordinates for flow layout
    x = [0, 1, 2, 3, 4]
    y = [0, 0, 0, 0, 0]
    colors = ["#2E7D32", "#388E3C", "#43A047", "#66BB6A", "#A5D6A7"]

    fig = go.Figure()

    # add circles for each step
    for i, step in enumerate(steps):
        fig.add_trace(go.Scatter(
            x=[x[i]], y=[y[i]],
            mode="markers+text",
            text=[step],
            textfont=dict(size=16, color="white"),
            textposition="middle center",
            marker=dict(size=120, color=colors[i], line=dict(width=4, color="#1B5E20")),
            hoverinfo="text"
        ))

        # arrows between circles
        if i < len(steps) - 1:
            fig.add_annotation(
                x=x[i] + 0.5, y=0,
                ax=x[i] + 0.1, ay=0,
                showarrow=True, arrowhead=3, arrowsize=2, arrowwidth=3, arrowcolor="#2E7D32"
            )

    fig.update_layout(
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        height=400,
        plot_bgcolor="linear-gradient(to right, #E8F5E9, #F1F8E9)",
        paper_bgcolor="rgba(240,255,240,1)",
        margin=dict(l=30, r=30, t=40, b=30),
        title=dict(text="FIS Process Flow", x=0.5, font=dict(size=22, color="#1B5E20"))
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("✨ The process visually demonstrates how FIS integrates multiple sustainability steps efficiently.")

# ============================================================
# 2️⃣ MIND MAP MODULE - Redesigned beautiful creative map
# ============================================================
elif menu == "Mind Map":
    st.subheader("🧭 Low-Carbon Strategy - Mind Map")

    st.markdown("""
    <p style='font-size:16px; color:#444;'>
    This interactive mind map visualizes the core structure of the Low-Carbon Strategy — 
    each branch connects back to the central sustainability goal.
    </p>
    """, unsafe_allow_html=True)

    main = "Low-Carbon Strategy"
    branches = ["Data Collection", "FIS Integration", "Supporting Tools", "Excel Analysis", "Corrective Actions"]
    sub_branches = {
        "Data Collection": ["Sensors", "Manual Entry", "IoT Devices"],
        "FIS Integration": ["Database", "APIs"],
        "Supporting Tools": ["GIS", "PowerBI", "Carbon Tracker"],
        "Excel Analysis": ["Data Cleaning", "Pivot Reports", "Trend Analysis"],
        "Corrective Actions": ["Energy Efficiency", "Renewable Projects"]
    }

    # define positions (radial layout)
    angles = np.linspace(0, 2 * np.pi, len(branches), endpoint=False)
    x_main, y_main = 0, 0
    radius = 2.5
    x_branches = radius * np.cos(angles)
    y_branches = radius * np.sin(angles)

    fig = go.Figure()

    # main node
    fig.add_trace(go.Scatter(
        x=[x_main], y=[y_main],
        mode="markers+text",
        text=[main],
        textfont=dict(size=16, color="white"),
        textposition="middle center",
        marker=dict(size=160, color="#2E7D32", line=dict(width=3, color="#1B5E20"))
    ))

    # branches and sub-branches
    for i, branch in enumerate(branches):
        fig.add_trace(go.Scatter(
            x=[x_main, x_branches[i]], y=[y_main, y_branches[i]],
            mode="lines",
            line=dict(color="#A5D6A7", width=3)
        ))

        # branch node
        fig.add_trace(go.Scatter(
            x=[x_branches[i]], y=[y_branches[i]],
            mode="markers+text",
            text=[branch],
            textfont=dict(size=14, color="#1B5E20"),
            textposition="middle center",
            marker=dict(size=100, color="#66BB6A", line=dict(width=3, color="#1B5E20"))
        ))

        # sub-branches around each branch
        subs = sub_branches.get(branch, [])
        if subs:
            angle_offset = np.linspace(-0.5, 0.5, len(subs))
            for j, sub in enumerate(subs):
                sx = x_branches[i] + 1.0 * np.cos(angles[i] + angle_offset[j])
                sy = y_branches[i] + 1.0 * np.sin(angles[i] + angle_offset[j])
                fig.add_trace(go.Scatter(
                    x=[x_branches[i], sx],
                    y=[y_branches[i], sy],
                    mode="lines",
                    line=dict(color="#C8E6C9", width=2)
                ))
                fig.add_trace(go.Scatter(
                    x=[sx], y=[sy],
                    mode="markers+text",
                    text=[sub],
                    textfont=dict(size=12, color="#1B5E20"),
                    textposition="middle center",
                    marker=dict(size=70, color="#A5D6A7", line=dict(width=2, color="#2E7D32"))
                ))

    fig.update_layout(
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        height=650,
        plot_bgcolor="rgba(240,255,240,1)",
        paper_bgcolor="rgba(240,255,240,1)",
        margin=dict(l=10, r=10, t=30, b=10),
        title=dict(text="Low-Carbon Strategy Mind Map", x=0.5, font=dict(size=22, color="#1B5E20"))
    )

    st.plotly_chart(fig, use_container_width=True)

# ============================================================
# 3️⃣ GAMIFICATION MODULE - Simplified (no current progress list)
# ============================================================
elif menu == "Gamification":
    st.header("🎮 Gamification - Track Progress for Each Step")

    st.markdown("""
    <p style='font-size:16px; color:#444;'>
    Adjust the progress for each stage and monitor your total sustainability performance automatically.
    </p>
    """, unsafe_allow_html=True)

    steps = ["Data Collection", "FIS Integration", "Other Tools", "Excel Analysis", "Corrective Actions"]
    progress_values = {}

    # Individual Step Sliders
    for step in steps:
        progress_values[step] = st.slider(f"{step}", 0, 100, 0)

    # Automatic overall progress (average)
    total_progress = int(sum(progress_values.values()) / len(steps))
    st.markdown("---")
    st.subheader("📈 Overall Process Completion")
    st.progress(total_progress)
    st.write(f"**Overall Low-Carbon Strategy Progress:** {total_progress}%")

    if total_progress == 100:
        st.success("🎉 Excellent! Your low-carbon strategy is fully implemented.")
    elif total_progress >= 70:
        st.info("🚀 You’re on the right path — keep improving sustainability actions.")
    elif total_progress >= 30:
        st.warning("⚙️ Initial steps complete — continue refining your strategy.")
    else:
        st.error("🛠️ Strategy still at an early stage. Let’s take action soon!")
