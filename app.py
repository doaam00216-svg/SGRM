import streamlit as st

# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="EEHC Smart Grid Roadmap (SGRM)",
    layout="wide",
    page_icon="⚡",
    initial_sidebar_state="expanded",
)

# Direct URLs to images stored in your repository README
GIZ_LOGO_URL = "https://github.com/user-attachments/assets/ee083587-4ccf-4a3b-b9fa-aecbc1b1d92a"
EEHC_BANNER_URL = "https://github.com/user-attachments/assets/6e2cbda8-2dbb-43fb-b3e1-d2f62cbbaab9"
SKYLINE_WATERMARK_URL = "https://github.com/user-attachments/assets/2c15ab31-e4eb-44c7-a9a3-c19d4b306fc2"

# Local/GitHub fallback helper
RAW_IMG_BASE = (
    "https://raw.githubusercontent.com/doaam00216-svg/SGRM/main/images/"
)


def display_img(file_name, caption=None, use_container_width=True):
    """Displays slide image with fallback handling."""
    url = RAW_IMG_BASE + file_name
    try:
        st.image(url, caption=caption, use_container_width=use_container_width)
    except Exception:
        st.image(
            f"images/{file_name}",
            caption=caption,
            use_container_width=use_container_width,
        )


# =========================================================
# 2. PRESENTATION MATCHED WHITE THEME & SKYLINE BACKGROUND CSS
# =========================================================
st.markdown(
    f"""
    <style>
    /* Clean White Presentation Background */
    .stApp {{
        background-color: #ffffff !important;
        color: #1a202c !important;
    }}

    /* Fixed City Skyline Watermark at the bottom */
    .stApp::after {{
        content: "";
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        height: 110px;
        background-image: url('{SKYLINE_WATERMARK_URL}');
        background-repeat: repeat-x;
        background-position: bottom center;
        background-size: contain;
        opacity: 0.30;
        pointer-events: none;
        z-index: 0;
    }}

    /* Corporate Typography */
    h1, h2, h3, h4 {{
        color: #0d3b66 !important;
        font-family: 'Segoe UI', Arial, sans-serif;
        font-weight: 700;
    }}

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {{
        background-color: #f8f9fa;
        border-bottom: 2px solid #dee2e6;
        gap: 8px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        color: #495057;
        font-weight: 600;
        padding: 12px 20px;
    }}

    .stTabs [aria-selected="true"] {{
        color: #d90429 !important; /* GIZ Red Highlight */
        background-color: #ffffff !important;
        border-bottom: 3px solid #d90429 !important;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# 3. BRANDED HEADER BANNER (GIZ & EEHC GRAPHICS)
# =========================================================
head_col1, head_col2 = st.columns([1, 3.5])

with head_col1:
    st.image(
        GIZ_LOGO_URL,
        caption="In cooperation with GIZ",
        use_container_width=True,
    )

with head_col2:
    st.image(EEHC_BANNER_URL, use_container_width=True)

st.markdown("---")

# =========================================================
# 4. DASHBOARD TITLE & EXECUTIVE SUMMARY METRICS
# =========================================================
st.title("⚡ EEHC Smart Grid Roadmap (SGRM)")
st.markdown(
    "##### Egyptian Electricity Holding Company — Enterprise Smart Grid Implementation & GIS Integration Dashboard"
)

m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Short-Term", "Jan 2026 – Jun 2027", "Foundation")
m2.metric("Medium-Term", "Jun 2027 – May 2030", "Expansion")
m3.metric("Long-Term", "May 2030+", "Smart Operations")
m4.metric("DISCO Scope", "9 Distribution Co.", "EEHC Grid")
m5.metric("Slide Visual Assets", "16 Map Proofs", "Verified")

st.markdown("---")

# =========================================================
# 5. FULL SMART GRID ROADMAP (PHASE TABS)
# =========================================================
tab_short, tab_medium, tab_long = st.tabs([
    "🚩 Short-Term Phase (2026 – 2027)",
    "🚀 Medium-Term Phase (2027 – 2030)",
    "🌐 Long-Term Phase (2030+)",
])

# ---------------------------------------------------------
# SHORT-TERM PHASE
# ---------------------------------------------------------
with tab_short:
    st.header(
        "Short-Term Roadmap: Central GIS Foundation, Data Cleanup & Core Infrastructure"
    )

    with st.expander("📌 Smart Grid Strategic Pillars (Short-Term)", expanded=True):
        col_s_a, col_s_b = st.columns(2)
        with col_s_a:
            st.markdown("""
            **1. Enterprise GIS Foundation**
            - Establish Centralized GIS Schema across EEHC.
            - Standardize MV grid topology data model.
            - Execute digital vectorization for feeders, kiosks, and substations.
            
            **2. SCADA & Substation Automation**
            - SCADA master station upgrades in high-priority zones.
            - RTU integration for key MV distribution nodes.
            """)
        with col_s_b:
            st.markdown("""
            **3. AMI & IT Readiness**
            - Head-End System (HES) integration for commercial/industrial meters.
            - IT/OT cybersecurity and data governance framework setup.
            
            **4. Organizational Capacity**
            - Establish DISCO GIS verification teams and QC workflows.
            """)

    st.markdown("---")
    st.subheader("🗺️ Short-Term Map Proofs & Systems")

    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.markdown("#### 1. Asset Record Concept Map")
        display_img(
            "01_asset_record.png",
            caption="Red MV grid topology map with asset attribute records",
        )

        st.markdown("#### 3. MV Network Drawing & Acceptance Map")
        display_img(
            "03_mv_drawing.png",
            caption="GIS mapping canvas with MV network nodes along Mohamed Abu El Fetouh Hassab St.",
        )

    with col_s2:
        st.markdown("#### 2. Smouha GIS Web Interface")
        display_img(
            "02_smouha_web.png",
            caption="OpenStreetMap vector view showing kiosk details in Smouha",
        )

        st.markdown("#### 4. GIS Rollout Monitoring Dashboard")
        display_img(
            "04_gis_monitoring.png",
            caption="City-wide feeder acceptance tracking across Capture, Verify, Approve stages",
        )

    st.markdown("#### 5. Alexandria Regional Distribution Network Map")
    display_img(
        "05_alexandria_map.png",
        caption="Overview of Alexandria regional distribution network (منطقة الإسكندرية)",
    )

# ---------------------------------------------------------
# MEDIUM-TERM PHASE
# ---------------------------------------------------------
with tab_medium:
    st.header(
        "Medium-Term Roadmap: Operational Applications, OMS & Grid Coverage"
    )

    with st.expander(
        "📌 Smart Grid Strategic Pillars (Medium-Term)", expanded=True
    ):
        col_m_a, col_m_b = st.columns(2)
        with col_m_a:
            st.markdown("""
            **1. Low-Voltage Network Digitization**
            - Street-level LV wall box mapping and service connection tracing.
            - Asset lifecycle parameter tracking (Transformers, RMUs).
            
            **2. OMS & Field Workforce**
            - Deploy Outage Management Systems (OMS) for rapid fault isolation.
            - Automated fleet dispatch and work order tracking.
            """)
        with col_m_b:
            st.markdown("""
            **3. Loss Analysis & Power Quality**
            - Boundary Metering Zones for commercial and technical loss calculations.
            - Continuous feeder trace monitoring for voltage events and harmonics.
            
            **4. Renewable & DER Integration**
            - Grid headroom screening maps for rooftop solar/EV interconnections.
            - Battery storage (BESS) candidate site screening.
            """)

    st.markdown("---")
    st.subheader("🗺️ Medium-Term Operational GIS Applications")

    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.markdown("#### 6. Low-Voltage Network Expansion (Wall Boxes)")
        display_img(
            "06_lv_expansion.png",
            caption="Street-level mapping of LV wall distribution boxes along Qanal El Mahmoudeya St.",
        )

        st.markdown("#### 8. Fleet & Field Workforce Management")
        display_img(
            "08_fleet_workforce.png",
            caption="Real-time field vehicle dispatching and work location routing",
        )

        st.markdown("#### 10. Loss Analysis & Energy Cost Visibility")
        display_img(
            "10_loss_analysis.png",
            caption="Metered boundary zones and transformer imbalance investigation areas",
        )

        st.markdown("#### 12. Power Quality Assessment & Response")
        display_img(
            "12_power_quality.png",
            caption="Feeder trace monitoring for voltage events, unbalance, and harmonics",
        )

    with col_m2:
        st.markdown("#### 7. Asset Management Interface")
        display_img(
            "07_asset_mgmt.png",
            caption="Interactive GIS view of transformer asset parameters (ELMACO 800 KVA)",
        )

        st.markdown("#### 9. Outage Management System (OMS)")
        display_img(
            "09_oms.png",
            caption="Fault trace schematic isolating impacted customer areas and feeder switches",
        )

        st.markdown("#### 11. Renewable & EV Connection Screening")
        display_img(
            "11_renewable.png",
            caption="Coastal grid headroom map highlighting constrained vs available capacity",
        )

        st.markdown("#### 13. Battery Energy Storage System (BESS) Support")
        display_img(
            "13_battery_storage.png",
            caption="Candidate battery storage siting along constrained distribution feeders",
        )

# ---------------------------------------------------------
# LONG-TERM PHASE
# ---------------------------------------------------------
with tab_long:
    st.header(
        "Long-Term Roadmap: Advanced ADMS, AMI Integration & Smart Operations"
    )

    with st.expander("📌 Smart Grid Strategic Pillars (Long-Term)", expanded=True):
        col_l_a, col_l_b = st.columns(2)
        with col_l_a:
            st.markdown("""
            **1. Advanced Distribution Management System (ADMS)**
            - Unified ADMS control engine merging SCADA, GIS, and OMS.
            - Fault Location, Isolation, and Service Restoration (FLISR) automation.
            
            **2. Voltage Optimization & Peak Shaving**
            - Automated Volt-VAR Optimization (VVO).
            - Dynamic peak shaving using demand-response analytics.
            """)
        with col_l_b:
            st.markdown("""
            **3. Complete AMI Topology Sync**
            - Meter-to-transformer topology mapping with real-time sync.
            - Smart meter last-gasp automated outage detection.
            """)

    st.markdown("---")
    st.subheader("🗺️ Long-Term Advanced Operation Systems")

    col_l1, col_l2 = st.columns(2)
    with col_l1:
        st.markdown("#### 14. ADMS & Restoration Automation")
        display_img(
            "14_adms.png",
            caption="Automated fault section isolation and switching restoration paths",
        )

        st.markdown("#### 16. Smart AMI Integration")
        display_img(
            "16_ami_integration.png",
            caption="Smart meter link mapping, outage indications, and load profile analytics",
        )

    with col_l2:
        st.markdown("#### 15. Voltage Optimization & Peak Management")
        display_img(
            "15_voltage_optimization.png",
            caption="Grid control assets, real-time voltage profiles, and demand trace curves",
        )
