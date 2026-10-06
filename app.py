import io
import fitz  # PyMuPDF
from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="EEHC GIS Strategic Roadmap", layout="wide", page_icon="⚡"
)

# ---------------------------------------------------------
# AUTO-LOAD IMAGES FROM PPTX
# ---------------------------------------------------------


@st.cache_data
def load_ppt_images(doc_path="SGRM.pptx"):
    try:
        doc = fitz.open(doc_path)
        imgs = []
        for page in doc:
            for img_info in page.get_images(full=True):
                xref = img_info[0]
                base_image = doc.extract_image(xref)
                imgs.append(Image.open(io.BytesIO(base_image["image"])))
        return imgs
    except Exception as e:
        return []


images = load_ppt_images("SGRM.pptx")

# ---------------------------------------------------------
# HEADER & OVERVIEW
# ---------------------------------------------------------
st.title("⚡ EEHC GIS Strategic Roadmap")
st.markdown(
    "### Egyptian Electricity Holding Company — Enterprise GIS Implementation Timeline"
)

st.write(
    """
This interactive dashboard outlines the phased rollout of the Enterprise Geographic Information System (GIS) 
across EEHC distribution networks, tracking strategic objectives, operational applications, and visual milestone maps.
"""
)

# High level KPI Summary Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Short-Term Horizon", "2026 – 2027", "Foundation")
col2.metric("Medium-Term Horizon", "2027 – 2030", "Expansion")
col3.metric("Long-Term Horizon", "2030+", "Smart Operations")
col4.metric("Total Visual Artifacts", f"{len(images)} Maps Loaded")

st.markdown("---")

# ---------------------------------------------------------
# PHASE TABS (ROADMAP + VISUALS)
# ---------------------------------------------------------
tab1, tab2, tab3 = st.tabs([
    "🚩 Short-Term Phase (2026 – 2027)",
    "🚀 Medium-Term Phase (2027 – 2030)",
    "🌐 Long-Term Phase (2030+)",
])

# =========================================================
# TAB 1: SHORT TERM
# =========================================================
with tab1:
    st.header("Short-Term Roadmap: Central GIS Foundation & Network Records")
    st.caption("Focus: Network record cleanup, MV topology, and acceptance")

    # Roadmap Details
    with st.expander("📌 Key Objectives & Deliverables", expanded=True):
        st.markdown("""
        - **Established Central GIS Foundation:** Core database initialization and schema setup.
        - **Medium-Voltage (MV) Drawing & Acceptance:** Digital mapping of MV feeders and kiosks.
        - **Rollout Monitoring:** Real-time tracking of acceptance workflows across Egyptian distribution zones.
        """)

    st.markdown("### Phase Visual Maps & Proofs")

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("1. Asset Record Concept")
        if len(images) > 0:
            st.image(
                images[0],
                caption="Red MV grid topology map with asset attribute record fields",
                use_container_width=True,
            )
        else:
            st.info("Asset record illustration")

        st.subheader("3. MV Network Drawing")
        if len(images) > 2:
            st.image(
                images[2],
                caption="GIS mapping canvas displaying MV nodes along Mohamed Abu El Fetouh Hassab St.",
                use_container_width=True,
            )
        else:
            st.info("MV Drawing map")

    with col_b:
        st.subheader("2. Smouha Web GIS Interface")
        if len(images) > 1:
            st.image(
                images[1],
                caption="Interactive vector map showing kiosk ALX-MAC-10-K0475 in Smouha",
                use_container_width=True,
            )
        else:
            st.info("Smouha Web GIS view")

        st.subheader("4. GIS Rollout Dashboard")
        if len(images) > 3:
            st.image(
                images[3],
                caption="City-wide monitoring showing Accepted, Under Review, and Exception feeders",
                use_container_width=True,
            )
        else:
            st.info("Rollout Monitoring Dashboard")

    st.subheader("5. Alexandria Distribution Network Map")
    if len(images) > 4:
        st.image(
            images[4],
            caption="Overview of Alexandria regional distribution network (منطقة الإسكندرية)",
            use_container_width=True,
        )

# =========================================================
# TAB 2: MEDIUM TERM
# =========================================================
with tab2:
    st.header("Medium-Term Roadmap: Coverage & Operating Applications")
    st.caption(
        "Focus: Low-Voltage expansion, workforce, OMS, and loss analysis"
    )

    with st.expander("📌 Key Objectives & Deliverables", expanded=True):
        st.markdown("""
        - **Low-Voltage (LV) Expansion:** Digitizing distribution wall boxes and customer connection points.
        - **Asset Management & Maintenance:** Complete lifecycle parameter records for transformers and RMUs.
        - **Fleet & Field Workforce Management:** Real-time vehicle location and work order assignment routing.
        - **Outage Management System (OMS):** Automated fault tracing and customer impact estimation.
        - **Energy Loss & Cost Visibility:** Transformer balancing and boundary metering analytics.
        """)

    st.markdown("### Phase Visual Maps & Systems")

    m_col1, m_col2 = st.columns(2)
    with m_col1:
        st.subheader("6. LV Network Expansion")
        if len(images) > 5:
            st.image(
                images[5],
                caption="Wall box mapping along Qanal El Mahmoudeya Street",
                use_container_width=True,
            )

        st.subheader("8. Field Workforce Dispatch")
        if len(images) > 7:
            st.image(
                images[7],
                caption="Vehicle dispatching and route tracking interface",
                use_container_width=True,
            )

        st.subheader("10. Loss Analysis & Energy Costing")
        if len(images) > 9:
            st.image(
                images[9],
                caption="Metered boundaries and transformer imbalance zones",
                use_container_width=True,
            )

        st.subheader("12. Power Quality Response")
        if len(images) > 11:
            st.image(
                images[11],
                caption="Feeder trace for voltage events and harmonics",
                use_container_width=True,
            )

    with m_col2:
        st.subheader("7. Asset Management Interface")
        if len(images) > 6:
            st.image(
                images[6],
                caption="Transformer attribute interface (ELMACO 800 KVA)",
                use_container_width=True,
            )

        st.subheader("9. Outage Management System")
        if len(images) > 8:
            st.image(
                images[8],
                caption="Fault isolation and impacted customer tracing",
                use_container_width=True,
            )

        st.subheader("11. Renewable Connection Screening")
        if len(images) > 10:
            st.image(
                images[10],
                caption="Grid capacity headroom map for solar/EV screening",
                use_container_width=True,
            )

        st.subheader("13. Battery Storage (BESS) Support")
        if len(images) > 12:
            st.image(
                images[12],
                caption="BESS candidate site screening along constrained feeders",
                use_container_width=True,
            )

# =========================================================
# TAB 3: LONG TERM
# =========================================================
with tab3:
    st.header("Long-Term Roadmap: Coordinated Network Operations")
    st.caption("Focus: ADMS integration, smart automation, and AMI metering")

    with st.expander("📌 Key Objectives & Deliverables", expanded=True):
        st.markdown("""
        - **ADMS & Restoration Automation:** Automated fault section isolation and remote switching.
        - **Voltage Optimization:** Dynamic reactive power control and peak load shaving.
        - **Advanced Metering Infrastructure (AMI):** Real-time meter-to-transformer link mapping and load profiles.
        """)

    st.markdown("### Advanced Operations Systems")

    l_col1, l_col2 = st.columns(2)
    with l_col1:
        st.subheader("14. ADMS Restoration Automation")
        if len(images) > 13:
            st.image(
                images[13],
                caption="Automated fault isolation and restoration switching option path",
                use_container_width=True,
            )

        st.subheader("16. Smart AMI Integration")
        if len(images) > 15:
            st.image(
                images[15],
                caption="Smart meter mapping, real-time load profiles, and outage indications",
                use_container_width=True,
            )

    with l_col2:
        st.subheader("15. Voltage & Peak Management")
        if len(images) > 14:
            st.image(
                images[14],
                caption="Voltage profile control and demand trace curve analytics",
                use_container_width=True,
            )
