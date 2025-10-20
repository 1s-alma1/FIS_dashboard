import streamlit as st
import plotly.graph_objects as go
import json
import os

# ======================================================
# 🌿 FILE FOR SAVING STATE
# ======================================================
STATE_FILE = "progress_state.json"

# ======================================================
# 🌿 PAGE CONFIGURATION
# ======================================================
st.set_page_config(
    page_title="FIS Low-Carbon Strategy",
    page_icon="🌿",
    layout="centered"
)

# ======================================================
# 🌿 HEADER SECTION (FIXED ONE-LINE TITLE)
# ======================================================
col1, col2, col3 = st.columns([1, 5, 1])
with col1:
    st.image("FIS_logo.png", width=80)
with col2:
    st.markdown(
        """
        <h1 style='text-align:center; color:#1B5E20; white-space:nowrap;'>
            🌿 Low-Carbon Strategy
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align:center; color:#555;'>Track and visualize the sustainability implementation steps</p>",
        unsafe_allow_html=True
    )
with col3:
    st.image("FFS_logo.png", width=80)

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)

# ======================================================
# 🌍 INTERACTIVE LOW-CARBON PLAN DIAGRAM
# ======================================================
st.subheader("🌍 FIS Low-Carbon Process Simulation")

st.markdown(
    """
<p style='font-size:16px; color:#444;'>
Click on each step below to view details of the <b>Low-Carbon Strategy</b> process.
</p>
""",
    unsafe_allow_html=True
)

# ======================================================
# 📘 STEP INFORMATION WITH CREATIVE COLORS
# ======================================================
steps_info = {
    "Data Collection": {
        "color": "#7EE8FA",  # Aqua Mint
        "description": """
📊 **Data Collection Phase**  
Collect all relevant data and information whithin LOCs/NSA and stakeholders responsible for key deliverables related to the organisation, product, or service including energy consumption, transportation, materials, and other sustainability-related factors.
"""
    },
    "FIS Integration": {
        "color": "#E6CBA8",  # Desert Clay
        "description": """
🔗 **Integration with FIS Tool**  
Integrate the collected data into the FIS CO₂ Calculator to quantify emissions following international standards, ensuring traceability and comparability.
"""
    },
    "Excel Analysis": {
        "color": "#A0E418",  # Vibrant Lime Green
        "description": """
📈 **Excel Analysis**  
Analyze FIS results to pinpoint high-emission hotspots and determine which areas contribute most to the overall carbon footprint.  
This insight enables focused sustainability improvements.
"""
    },
    "Corrective Actions": {
        "color": "#CBA6E3",  # Orchid Mauve
        "description": """
⚙️ **Corrective Actions**  
Implement targeted corrective measures based on analysis outcomes to minimize carbon emissions and improve sustainability performance.  
These actions support the organization’s commitment to achieving a low-carbon transition.
"""
    }
}

# ======================================================
# 🔘 INTERACTIVE STEP SELECTOR
# ======================================================
selected_step = st.radio(
    "Select a step 👇",
    list(steps_info.keys()),
    horizontal=True
)

# ======================================================
# 🔵 BUBBLE DIAGRAM (Plotly)
# ======================================================
fig = go.Figure()

for i, (step, data) in enumerate(steps_info.items()):
    fig.add_trace(go.Scatter(
        x=[i],
        y=[0],
        mode="markers+text",
        text=[step],
        textposition="middle center",
        textfont=dict(size=14, color="#1B1B1B"),
        marker=dict(
            size=120 if step == selected_step else 100,
            color=data["color"],
            line=dict(width=4 if step == selected_step else 2, color="#2E2E2E"),
            opacity=1 if step == selected_step else 0.9
        ),
        hoverinfo="text"
    ))

    # Arrows between bubbles
    if i < len(steps_info) - 1:
        fig.add_annotation(
            x=i + 0.5, y=0,
            ax=i + 0.1, ay=0,
            showarrow=True,
            arrowhead=3,
            arrowsize=1.5,
            arrowwidth=2,
            arrowcolor="#2E2E2E"
        )

fig.update_layout(
    showlegend=False,
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    height=350,
    plot_bgcolor="rgba(250,250,250,1)",
    paper_bgcolor="rgba(250,250,250,1)",
    margin=dict(l=40, r=40, t=40, b=40),
)

st.plotly_chart(fig, use_container_width=True)

# ======================================================
# 📝 DYNAMIC DESCRIPTION DISPLAY
# ======================================================
st.markdown(
    f"""
<div style='background-color:{steps_info[selected_step]["color"]};
            color:#1B1B1B; padding:20px; border-radius:15px; margin-top:15px;'>
    {steps_info[selected_step]["description"]}
</div>
""",
    unsafe_allow_html=True
)

st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)

# ======================================================
# 📈 PROGRESS TRACKER (Persistent)
# ======================================================
st.header("📈 Progress Tracker")

st.markdown(
    """
<p style='font-size:16px; color:#444;'>
Adjust the completion percentage for each step in your <b>Low-Carbon Strategy</b>.  
The total progress updates automatically and is saved locally.
</p>
""",
    unsafe_allow_html=True
)

# Load saved progress
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        saved_state = json.load(f)
else:
    saved_state = {}

tracker_steps = ["Data Collection", "FIS Integration", "Excel Analysis", "Corrective Actions"]
progress_values = {}

# Create sliders
for step in tracker_steps:
    key = step.replace(" ", "_").lower()
    default_value = saved_state.get(key, 0)
    progress_values[step] = st.slider(step, 0, 100, value=default_value, key=key)

# Save progress
save = {step.replace(" ", "_").lower(): progress_values[step] for step in tracker_steps}
with open(STATE_FILE, "w") as f:
    json.dump(save, f)

# Calculate overall progress
total_progress = int(sum(progress_values.values()) / len(tracker_steps))

st.markdown("---")
st.subheader("🌍 Overall Process Completion")
st.progress(total_progress)
st.write(f"**Overall Progress:** {total_progress}%")

# Feedback based on progress
if total_progress == 100:
    st.success("🎉 Excellent! Your low-carbon strategy is fully implemented.")
elif total_progress >= 70:
    st.info("🚀 You’re on the right path — keep improving sustainability actions.")
elif total_progress >= 30:
    st.warning("⚙️ Initial steps complete — continue refining your strategy.")
else:
    st.error("🛠️ Strategy still at an early stage. Let’s take action soon!")


# ======================================================
# 📊 ADD THE IMAGE AT THE END (AFTER FOOTER TEXT)
# ======================================================
import os
from PIL import Image, ImageEnhance

# Title above the image
st.markdown(
    "<br><h3 style='text-align:center; color:#1B5E20;'>Déplacement des équipes selon le type d’événement</h3>",
    unsafe_allow_html=True
)

# Debug (optional): show current directory and files if image not found
# st.write("Current directory:", os.getcwd())
# st.write("Files here:", os.listdir())

try:
    # Open and slightly enhance brightness for clarity
    image = Image.open("IMG_2388.png")
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.15)  # Increase brightness by 15%

    # Display with full width and light frame
    st.markdown(
        """
        <div style='background-color:#f9f9f9;
                    border:2px solid #ccc;
                    border-radius:10px;
                    padding:10px;
                    text-align:center;
                    margin-top:10px;'>
        """,
        unsafe_allow_html=True
    )

    st.image(image, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

except FileNotFoundError:
    st.error("⚠️ Image file 'IMG_2388.png' not found in the current directory.")


# ======================================================
# 📍 FOOTER
# ======================================================
st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)
st.markdown(
    """
<div style='text-align:center; color:#555; font-size:14px;'>
    Fédération Française de Ski — Annecy
</div>
<div style='text-align:right; color:#555; font-size:14px;'>
    Roman RIBOUD &nbsp; | &nbsp; Salma ATTAIBE
</div>
""",
    unsafe_allow_html=True
)

