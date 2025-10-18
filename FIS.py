import streamlit as st
import plotly.graph_objects as go

# ---- PAGE CONFIG ----
st.set_page_config(page_title="FIS Low-Carbon Progress Tracker", page_icon="🌿", layout="centered")

# ---- HEADER ----
col1, col2, col3 = st.columns([1, 5, 1])
with col1:
    st.image("FIS_logo.png", width=80)
with col2:
    st.markdown("<h1 style='text-align:center; color:#1B5E20;'>🌿 Low-Carbon Strategy Progress</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#555;'>Track and visualize the sustainability implementation steps</p>", unsafe_allow_html=True)
with col3:
    st.image("FFS_logo.png", width=80)

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)

# ======================================================
# 🌍 FIS PROCESS SIMULATION (PLOTLY)
# ======================================================
st.subheader("🌍 FIS Low-Carbon Process Simulation")

st.markdown("""
<p style='font-size:16px; color:#444;'>
This diagram illustrates the key stages of the <b>Low-Carbon Strategy</b> using the <b>FIS Tool</b>.
</p>
""", unsafe_allow_html=True)

steps = ["Data Collection", "FIS Integration", "Excel Analysis", "Corrective Actions"]
colors = ["#2E7D32", "#43A047", "#66BB6A", "#A5D6A7"]

fig = go.Figure()

# Create circles for each step
for i, step in enumerate(steps):
    fig.add_trace(go.Scatter(
        x=[i], y=[0],
        mode="markers+text",
        text=[step],
        textfont=dict(size=15, color="white"),
        textposition="middle center",
        marker=dict(size=110, color=colors[i], line=dict(width=3, color="#1B5E20")),
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
    title=dict(text="FIS Workflow Simulation", x=0.5, font=dict(size=20, color="#1B5E20"))
)

st.plotly_chart(fig, use_container_width=True)

# ======================================================
# 📈 PROGRESS TRACKER
# ======================================================
st.header("📈 Progress Tracker")

st.markdown("""
<p style='font-size:16px; color:#444;'>
Adjust the completion percentage for each step in your <b>Low-Carbon Strategy</b>.  
The total progress updates automatically.
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

# Feedback
if total_progress == 100:
    st.success("🎉 Excellent! Your low-carbon strategy is fully implemented.")
elif total_progress >= 70:
    st.info("🚀 You’re on the right path — keep improving sustainability actions.")
elif total_progress >= 30:
    st.warning("⚙️ Initial steps complete — continue refining your strategy.")
else:
    st.error("🛠️ Strategy still at an early stage. Let’s take action soon!")

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align:center; color:#555; font-size:14px;'>
        La Fédération Française de Ski Annecy
    </div>
    <div style='text-align:right; color:#555; font-size:14px;'>
        Roman RIBOUD -- Salma ATAIBE
    </div>
    """,
    unsafe_allow_html=True
)
