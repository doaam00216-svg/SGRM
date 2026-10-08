import streamlit as st

# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="EEHC GIS Strategic Roadmap", layout="wide", page_icon="⚡"
)

# Base GitHub raw URL for images (replace <YOUR_GITHUB_USERNAME> and <YOUR_REPO_NAME> if needed)
IMAGE_BASE_URL = "images/"

# =========================================================
# 2. WHITE THEME & SKYLINE BACKGROUND CSS
# =========================================================
st.markdown(
    """
    <style>
    /* Clean White Application Background */
    .stApp {
        background-color: #ffffff !important;
        color: #1a1a1a !important;
    }

    /* Fixed Footer Skyline Watermark at the bottom */
    .stApp::after {
        content: "";
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        height: 110px;
        background-image: url('images/skyline_footer.png');
        background-repeat: repeat-x;
        background-position: bottom center;
        background-size: contain;
        opacity: 0.30;
        pointer-events: none;
        z-index: 0;
    }

    /* Main Headings Styling */
    h1, h2, h3, h4 {
        color: #0d3b66 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700;
    }

    /* Tab Styling matching presentation colors */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #f8f9fa;
        border-bottom: 2px solid #e9ecef;
        gap: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #495057;
        font-weight: 600;
        padding-top: 10px;
        padding-bottom: 10px;
    }

    .stTabs [aria-selected="true"] {
        color: #d90429 !important; /* GIZ Red Highlight */
        border-bottom-color: #d90429 !important;
    }

    /* Image Caption Styling */
    .stImage caption {
        color: #555555 !important;
        font-size: 13px;
        font-weight: 500;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# 3. TOP BRANDING HEADER BANNER (GIZ + EEHC Network Graphic)
# =========================================================
header_col1, header_col2 = st.columns([1, 4])

with header_col1:
    # GIZ Skyline & Logo
    st.image(
        IMAGE_BASE_URL + "giz_logo.png",
        use_container_width=True,
        caption="In cooperation with GIZ",
    )

with header_col2:
    # EEHC Distribution Network Map Banner
    st.image(IMAGE_BASE_URL + "eehc_header_banner.png", use_container_width=True)

st.markdown("---")

# =========================================================
# 4. DASHBOARD TITLE & METRICS
# =========================================================
st.title("⚡ Egyptian Electricity Holding Company (EEHC)")
st.markdown("### Strategic Enterprise GIS Roadmap & Implementation Dashboard")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Short-Term Horizon", "2026 – 2027", "Central Foundation")
col2.metric("Medium-Term Horizon", "2027 – 2030", "Operational Systems")
col3.metric("Long-Term Horizon", "2030+", "Smart Operations")
col4.metric("Loaded Proof Maps", "16 Artifacts", "Verified")

st.markdown("---")

# =========================================================
# 5. ROADMAP PHASES & GIS SECTIONS
# =========================================================
tab_short, tab_medium, tab_long = st.tabs([
    "🚩 Short-Term Phase (2026 – 2027)",
    "🚀 Medium-Term Phase (2027 – 2030)",
    "🌐 Long-Term Phase (2030+)",
])

# ---------------------------------------------------------
# TAB 1: SHORT TERM
# ---------------------------------------------------------
with tab_short:
    st.header("Short-Term Roadmap: Central GIS Foundation & Network Records")

    with st.expander("📌 Phase Objectives & Scope", expanded=True):
        st.markdown("""
        - **Established Central GIS Foundation:** Initial database schema setup and centralized enterprise repository.
        - **Medium-Voltage (MV) Drawing & Acceptance:** Standardized digitizing and verification for MV lines and kiosks.
        - **Rollout Monitoring Dashboard:** Tracking acceptance progress across Egyptian distribution companies.
        """)

    st.markdown("---")
    st.subheader("🗺️ Short-Term GIS Network Records & Proof Maps")

    col_s1, col_s2 = st.columns(2)

    with col_s1:
        st.markdown("#### 1. Asset Record Concept")
        st.image(
            IMAGE_BASE_URL + "01_asset_record.png",
            caption="Red MV grid topology map with asset attribute record fields",
            use_container_width=True,
        )

        st.markdown("#### 3. MV Network Drawing")
        st.image(
            IMAGE_BASE_URL + "03_mv_drawing.png",
            caption="GIS mapping canvas displaying MV nodes along Mohamed Abu El Fetouh Hassab St.",
            use_container_width=True,
        )

    with col_s2:
        st.markdown("#### 2. Smouha Web GIS Interface")
        st.image(
            IMAGE_BASE_URL + "02_smouha_web.png",
            caption="Interactive vector map showing kiosk ALX-MAC-10-K0475 in Smouha",
            use_container_width=True,
        )

        st.markdown("#### 4. GIS Rollout Dashboard")
        st.image(
            IMAGE_BASE_URL + "04_gis_monitoring.png",
            caption="City-wide monitoring showing Accepted, Under Review, and Exception feeders",
            use_container_width=True,
        )

    st.markdown("#### 5. Alexandria Distribution Network Map")
    st.image(
        IMAGE_BASE_URL + "05_alexandria_map.png",
        caption="Overview map of Alexandria regional distribution network (منطقة الإسكندرية)",
        use_container_width=True,
    )

# ---------------------------------------------------------
# TAB 2: MEDIUM TERM
# ---------------------------------------------------------
with tab_medium:
    st.header("Medium-Term Roadmap: Coverage & Operational Applications")

    with st.expander("📌 Phase Objectives & Scope", expanded=True):
        st.markdown("""
        - **Low-Voltage (LV) Expansion:** Street-level mapping of LV wall boxes and service drops.
        - **Asset Management & Maintenance:** Complete lifecycle parameter tracking for transformers and RMUs.
        - **Fleet & Field Workforce Management:** Real-time crew location, vehicle routing, and work order tracking.
        - **Outage Management System (OMS):** Automated fault tracing and customer impact boundary identification.
        - **Loss Analysis & Energy Costing:** Transformer load balancing and boundary metering analytics.
        """)

    st.markdown("---")
    st.subheader("🗺️ Medium-Term Operational GIS Applications")

    col_m1, col_m2 = st.columns(2)

    with col_m1:
        st.markdown("#### 6. LV Network Expansion")
        st.image(
            IMAGE_BASE_URL + "06_lv_expansion.png",
            caption="Wall box mapping along Qanal El Mahmoudeya Street",
            use_container_width=True,
        )

        st.markdown("#### 8. Field Workforce Dispatch")
        st.image(
            IMAGE_BASE_URL + "08_fleet_workforce.png",
            caption="Vehicle dispatching and route tracking interface",
            use_container_width=True,
        )

        st.markdown("#### 10. Loss Analysis & Energy Costing")
        st.image(
            IMAGE_BASE_URL + "10_loss_analysis.png",
            caption="Metered boundaries and transformer imbalance zones",
            use_container_width=True,
        )

        st.markdown("#### 12. Power Quality Response")
        st.image(
            IMAGE_BASE_URL + "12_power_quality.png",
            caption="Feeder trace for voltage events and harmonics",
            use_container_width=True,
        )

    with col_m2:
        st.markdown("#### 7. Asset Management Interface")
        st.image(
            IMAGE_BASE_URL + "07_asset_mgmt.png",
            caption="Transformer attribute interface (ELMACO 800 KVA)",
            use_container_width=True,
        )

        st.markdown("#### 9. Outage Management System (OMS)")
        st.image(
            IMAGE_BASE_URL + "09_oms.png",
            caption="Fault isolation and impacted customer tracing",
            use_container_width=True,
        )

        st.markdown("#### 11. Renewable Connection Screening")
        st.image(
            IMAGE_BASE_URL + "11_renewable.png",
            caption="Grid capacity headroom map for solar/EV screening",
            use_container_width=True,
        )

        st.markdown("#### 13. Battery Storage (BESS) Support")
        st.image(
            IMAGE_BASE_URL + "13_battery_storage.png",
            caption="BESS candidate site screening along constrained feeders",
            use_container_width=True,
        )

# ---------------------------------------------------------
# TAB 3: LONG TERM
# ---------------------------------------------------------
with tab_long:
    st.header("Long-Term Roadmap: Coordinated Network Operations")

    with st.expander("📌 Phase Objectives & Scope", expanded=True):
        st.markdown("""
        - **ADMS & Restoration Automation:** Automated fault section isolation and restoration switching paths.
        - **Voltage Optimization & Peak Management:** Dynamic reactive power control and peak load shaving.
        - **Advanced Metering Infrastructure (AMI):** Meter-to-transformer connectivity mapping and real-time alerts.
        """)

    st.markdown("---")
    st.subheader("🗺️ Long-Term Advanced Operation Systems")

    col_l1, col_l2 = st.columns(2)

    with col_l1:
        st.markdown("#### 14. ADMS Restoration Automation")
        st.image(
            IMAGE_BASE_URL + "14_adms.png",
            caption="Automated fault isolation and restoration switching option path",
            use_container_width=True,
        )

        st.markdown("#### 16. Smart AMI Integration")
        st.image(
            IMAGE_BASE_URL + "16_ami_integration.png",
            caption="Smart meter mapping, real-time load profiles, and outage indications",
            use_container_width=True,
        )

    with col_l2:
        st.markdown("#### 15. Voltage & Peak Management")
        st.image(
            IMAGE_BASE_URL + "15_voltage_optimization.png",
            caption="Voltage profile control and demand trace curve analytics",
            use_container_width=True,
        )
