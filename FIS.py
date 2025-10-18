import streamlit as st

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

# ---- PROGRESS TRACKER ----
st.header("📈 Progress Tracker")





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
from graphviz import Digraph

st.subheader("🌍 FIS Process Flow Simulation")

st.markdown("""
<p style='font-size:16px; color:#444;'>
A simple process flow showing the key stages of the Low-Carbon Strategy.
</p>
""", unsafe_allow_html=True)

dot = Digraph()
dot.attr(rankdir='LR', bgcolor="#f8fff8")

dot.node("A", "Data Collection", shape="box", style="filled", fillcolor="#66BB6A")
dot.node("B", "FIS Integration", shape="box", style="filled", fillcolor="#81C784")
dot.node("C", "Excel Analysis", shape="box", style="filled", fillcolor="#A5D6A7")
dot.node("D", "Corrective Actions", shape="box", style="filled", fillcolor="#C8E6C9")

dot.edges(["AB", "BC", "CD"])

st.graphviz_chart(dot)


