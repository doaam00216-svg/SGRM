import io
import fitz  # PyMuPDF
from PIL import Image
import streamlit as st

st.set_page_config(page_title="EEHC GIS Rollout Strategy", layout="wide")
st.title("EEHC GIS Rollout Strategy")


# Function to extract images directly from SGRM.pptx in your GitHub repository
@st.cache_data
def load_presentation_images(doc_path="SGRM.pptx"):
    doc = fitz.open(doc_path)
    extracted_images = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        image_list = page.get_images(full=True)

        for img_info in image_list:
            xref = img_info[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            pil_img = Image.open(io.BytesIO(image_bytes))
            extracted_images.append(pil_img)

    return extracted_images


# Load images directly from SGRM.pptx
try:
    images = load_presentation_images("SGRM.pptx")
except Exception as e:
    st.error(
        f"Could not load 'SGRM.pptx' from repository. Make sure the file name in GitHub matches exactly! Error: {e}"
    )
    st.stop()

# Define tabs for the rollout timeline
tab_short, tab_medium, tab_long = st.tabs([
    "Short-Term (Jan 2026 – Jun 2027)",
    "Medium-Term (Jun 2027 – May 2030)",
    "Long-Term (May 2030+)",
])

# ==========================================
# 1. SHORT-TERM TAB
# ==========================================
with tab_short:
    st.header("Short-Term: Central GIS Foundation & Network Records")

    st.subheader("1. Asset Record Concept Map")
    if len(images) > 0:
        st.image(
            images[0],
            caption="Red medium-voltage grid topology map with asset attribute records",
            use_container_width=True,
        )

    st.subheader("2. Smouha GIS Web Interface")
    if len(images) > 1:
        st.image(
            images[1],
            caption="OpenStreetMap vector view showing kiosk asset details on Victor Emmanuel III St.",
            use_container_width=True,
        )

    st.subheader("3. MV Network Drawing & Acceptance Map")
    if len(images) > 2:
        st.image(
            images[2],
            caption="GIS mapping canvas with MV network nodes along Mohamed Abu El Fetouh Hassab St.",
            use_container_width=True,
        )

    st.subheader("4. GIS Rollout Monitoring Dashboard")
    if len(images) > 3:
        st.image(
            images[3],
            caption="City-wide feeder acceptance tracking across Capture, Verify, Approve, and Publish stages",
            use_container_width=True,
        )

    st.subheader("5. Alexandria Regional Distribution Network Map")
    if len(images) > 4:
        st.image(
            images[4],
            caption="Overview of Alexandria's regional electricity distribution network (منطقة الإسكندرية)",
            use_container_width=True,
        )

# ==========================================
# 2. MEDIUM-TERM TAB
# ==========================================
with tab_medium:
    st.header("Medium-Term: Coverage & Operating Applications")

    st.subheader("6. Low-Voltage Network Expansion (Wall Boxes)")
    if len(images) > 5:
        st.image(
            images[5],
            caption="Street-level mapping of LV wall distribution boxes along Qanal El Mahmoudeya St.",
            use_container_width=True,
        )

    st.subheader("7. Asset Management & Maintenance Interface")
    if len(images) > 6:
        st.image(
            images[6],
            caption="Interactive GIS view of transformer asset parameters (ELMACO 800 KVA)",
            use_container_width=True,
        )

    st.subheader("8. Fleet & Field Workforce Management")
    if len(images) > 7:
        st.image(
            images[7],
            caption="Real-time field vehicle dispatching and work location routing",
            use_container_width=True,
        )

    st.subheader("9. Outage Management System (OMS)")
    if len(images) > 8:
        st.image(
            images[8],
            caption="Fault trace schematic isolating impacted customer areas and feeder switches",
            use_container_width=True,
        )

    st.subheader("10. Loss Analysis & Energy Cost Visibility")
    if len(images) > 9:
        st.image(
            images[9],
            caption="Metered boundary zones and transformer imbalance investigation areas",
            use_container_width=True,
        )

    st.subheader("11. Renewable & EV Connection Screening")
    if len(images) > 10:
        st.image(
            images[10],
            caption="Coastal grid headroom map highlighting constrained vs available capacity",
            use_container_width=True,
        )

    st.subheader("12. Power Quality Assessment & Response")
    if len(images) > 11:
        st.image(
            images[11],
            caption="Feeder trace monitoring for voltage events, unbalance, and harmonics",
            use_container_width=True,
        )

    st.subheader("13. Battery Energy Storage System (BESS) Support")
    if len(images) > 12:
        st.image(
            images[12],
            caption="Candidate battery storage siting along constrained distribution feeders",
            use_container_width=True,
        )

# ==========================================
# 3. LONG-TERM TAB
# ==========================================
with tab_long:
    st.header("Long-Term: Coordinated Network Operations")

    st.subheader("14. ADMS & Restoration Automation")
    if len(images) > 13:
        st.image(
            images[13],
            caption="Automated fault section isolation and switching restoration paths",
            use_container_width=True,
        )

    st.subheader("15. Voltage Optimization & Peak Management")
    if len(images) > 14:
        st.image(
            images[14],
            caption="Grid control assets, real-time voltage profiles, and demand trace curves",
            use_container_width=True,
        )

    st.subheader("16. Advanced Metering Infrastructure (AMI) Integration")
    if len(images) > 15:
        st.image(
            images[15],
            caption="Smart meter link mapping, outage indications, and load profile analytics",
            use_container_width=True,
        )
