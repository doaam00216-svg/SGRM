import os
import streamlit as st

# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="EEHC GIS Strategic Roadmap", layout="wide", page_icon="⚡"
)

# Set base folder path for images
IMAGE_DIR = "images"


# Helper function to render images safely without raising FileNotFoundError
def safe_image(file_name, caption=None, use_container_width=True):
    path = os.path.join(IMAGE_DIR, file_name)
    if os.path.exists(path):
        st.image(path, caption=caption, use_container_width=use_container_width)
    elif os.path.exists(file_name):  # Check root directory as fallback
        st.image(
            file_name, caption=caption, use_container_width=use_container_width
        )
    else:
        st.info(f"📷 Image `{file_name}` (Upload to `images/` directory)")


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
    safe_image("giz_logo.png", caption="In cooperation with GIZ")

with header_col2:
    safe_image("eehc_header_banner.png")

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
        safe_image(
            "01_asset_record.png",
            caption="Red MV grid topology map with asset attribute record fields",
        )

        st.markdown("#### 3. MV Network Drawing")
        safe_image(
            "03_mv_drawing.png",
            caption="GIS mapping canvas displaying MV nodes along Mohamed Abu El Fetouh Hassab St.",
        )

    with col_s2:
        st.markdown("#### 2. Smouha Web GIS Interface")
        safe_image(
            "02_smouha_web.png",
            caption="Interactive vector map showing kiosk ALX-MAC-10-K0475 in Smouha",
        )

        st.markdown("#### 4. GIS Rollout Dashboard")
        safe_image(
            "04_gis_monitoring.png",
            caption="City-wide monitoring showing Accepted, Under Review, and Exception feeders",
        )

    st.markdown("#### 5. Alexandria Distribution Network Map")
    safe_image(
        "05_alexandria_map.png",
        caption="Overview map of Alexandria regional distribution network (منطقة الإسكندرية)",
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
        safe_image(
            "06_lv_expansion.png",
            caption="Wall box mapping along Qanal El Mahmoudeya Street",
        )

        st.markdown("#### 8. Field Workforce Dispatch")
        safe_image(
            "08_fleet_workforce.png",
            caption="Vehicle dispatching and route tracking interface",
        )

        st.markdown("#### 10. Loss Analysis & Energy Costing")
        safe_image(
            "10_loss_analysis.png",
            caption="Metered boundaries and transformer imbalance zones",
        )

        st.markdown("#### 12. Power Quality Response")
        safe_image(
            "12_power_quality.png",
            caption="Feeder trace for voltage events and harmonics",
        )

    with col_m2:
        st.markdown("#### 7. Asset Management Interface")
        safe_image(
            "07_asset_mgmt.png",
            caption="Transformer attribute interface (ELMACO 800 KVA)",
        )

        st.markdown("#### 9. Outage Management System (OMS)")
        safe_image(
            "09_oms.png",
            caption="Fault isolation and impacted customer tracing",
        )

        st.markdown("#### 11. Renewable Connection Screening")
        safe_image(
            "11_renewable.png",
            caption="Grid capacity headroom map for solar/EV screening",
        )

        st.markdown("#### 13. Battery Storage (BESS) Support")
        safe_image(
            "13_battery_storage.png",
            caption="BESS candidate site screening along constrained feeders",
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
        safe_image(
            "14_adms.png",
            caption="Automated fault isolation and restoration switching option path",
        )

        st.markdown("#### 16. Smart AMI Integration")
        safe_image(
            "16_ami_integration.png",
            caption="Smart meter mapping, real-time load profiles, and outage indications",
        )

    with col_l2:
        st.markdown("#### 15. Voltage & Peak Management")
        safe_image(
            "15_voltage_optimization.png",
            caption="Voltage profile control and demand trace curve analytics",
        )
