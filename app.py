import os
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

# Base path for local image assets
IMAGE_DIR = "images"


def display_img(file_name, caption=None, use_container_width=True):
    """Displays slide image safely with local fallback handling."""
    path = os.path.join(IMAGE_DIR, file_name)
    if os.path.exists(path):
        st.image(path, caption=caption, use_container_width=use_container_width)
    elif os.path.exists(file_name):
        st.image(
            file_name, caption=caption, use_container_width=use_container_width
        )
    else:
        st.info(f"📌 **Map Visual:** `{file_name}` (Store in `images/` folder)")


# =========================================================
# 2. CLEAN WHITE PRESENTATION THEME (NO BOTTOM WATERMARK)
# =========================================================
st.markdown(
    """
    <style>
    /* Clean White Presentation Background */
    .stApp {
        background-color: #ffffff !important;
        color: #1a202c !important;
    }

    /* Corporate Typography */
    h1, h2, h3, h4 {
        color: #0d3b66 !important;
        font-family: 'Segoe UI', Arial, sans-serif;
        font-weight: 700;
    }

    /* Custom Phase Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #f8f9fa;
        border-bottom: 2px solid #dee2e6;
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #495057;
        font-weight: 600;
        padding: 12px 20px;
    }

    .stTabs [aria-selected="true"] {
        color: #d90429 !important; /* GIZ Red Highlight */
        background-color: #ffffff !important;
        border-bottom: 3px solid #d90429 !important;
    }

    /* Expander Container Styling */
    .streamlit-expanderHeader {
        background-color: #f1f5f9 !important;
        border-radius: 6px;
        color: #0f172a !important;
        font-weight: 600;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# 3. BRANDED HEADER BANNER (GIZ + EEHC GRAPHICS)
# =========================================================
head_col1, head_col2 = st.columns([1, 3.5])

with head_col1:
    display_img("giz_logo.png", caption="In cooperation with GIZ")

with head_col2:
    display_img("eehc_header_banner.png")

st.markdown("---")

# =========================================================
# 4. OVERALL SMART GRID ROADMAP (SGRM FOUNDATION)
# =========================================================
st.title("⚡ EEHC Enterprise Smart Grid Roadmap (SGRM)")
st.markdown(
    "##### Comprehensive Strategic Plan for Digital Transformation across Egyptian Electricity Distribution Companies (DISCOs)"
)

# Strategic Executive Metrics
m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Short-Term Horizon", "2026 – 2027", "Central Foundation")
m2.metric("Medium-Term Horizon", "2027 – 2030", "Operational Scale")
m3.metric("Long-Term Horizon", "2030+", "Smart Operations")
m4.metric("Scope", "9 DISCOs", "National Grid")
m5.metric("GIS Visual Proofs", "16 Artifacts", "Verified")

st.markdown("---")

# Overall SGRM Core Strategic Pillars
st.subheader("🏛️ SGRM Overall Strategic Pillars")
p1, p2, p3, p4 = st.columns(4)

with p1:
    st.markdown("""
    **1. Enterprise GIS Core**
    - Single source of grid truth
    - MV/LV asset vectorization
    - Dynamic network topology
    """)

with p2:
    st.markdown("""
    **2. SCADA & Automation**
    - Master Control Centers
    - Feeder Automation (RTUs)
    - Substation Monitoring
    """)

with p3:
    st.markdown("""
    **3. AMI & Metering**
    - Head-End System (HES)
    - Billing & MDMS Sync
    - High-Value Customer Meters
    """)

with p4:
    st.markdown("""
    **4. Smart Operations (ADMS)**
    - Outage Management (OMS)
    - FLISR Automated Restoration
    - DER & Solar Headroom
    """)

st.markdown("---")

# =========================================================
# 5. PHASE-BY-PHASE SGRM & GIS IMPLEMENTATION TABS
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
        "Short-Term Phase: Smart Grid Infrastructure & GIS Central Foundation"
    )

    with st.expander("📌 SGRM Strategic Scope & Action Items", expanded=True):
        col_s_a, col_s_b = st.columns(2)
        with col_s_a:
            st.markdown("""
            **Smart Grid Architecture & IT Readiness**
            - Establish Central Enterprise GIS Database Schema across EEHC.
            - Standardize data models for Medium Voltage (MV) grid topology.
            - SCADA master station upgrades in high-priority zones.
            """)
        with col_s_b:
            st.markdown("""
            **GIS Integration & Field Operations**
            - Execute digital vectorization for feeders, kiosks, and substations.
            - Deploy GIS Acceptance Dashboard to monitor DISCO digitizing progress.
            - Integrate Head-End System (HES) for commercial and industrial meters.
            """)

    st.markdown("---")
    st.subheader("🗺️ Short-Term Enterprise GIS Maps & Acceptance Screenshots")

    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.markdown("#### 1. Asset Record Concept Map")
        display_img(
            "01_asset_record.png",
            caption="Red MV grid topology map with asset attribute record fields",
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
        "Medium-Term Phase: Grid Operations, OMS & Low-Voltage Coverage"
    )

    with st.expander("📌 SGRM Strategic Scope & Action Items", expanded=True):
        col_m_a, col_m_b = st.columns(2)
        with col_m_a:
            st.markdown("""
            **Low-Voltage Mapping & Asset Management**
            - Complete street-level LV wall box mapping and service connection tracing.
            - Full parameter tracking for transformers, RMUs, and distribution cabinets.
            
            **Outage Management & Fleet Dispatch**
            - Deploy GIS-centric Outage Management System (OMS) for rapid fault location.
            - Real-time field vehicle dispatching and work order management.
            """)
        with col_m_b:
            st.markdown("""
            **Loss Analytics & Energy Balance**
            - Boundary Metering Zones for technical and commercial loss analysis.
            - Feeder trace monitoring for power quality, unbalance, and harmonics.
            
            **DER & Grid Flexibility**
            - Renewable screening maps for rooftop solar and EV charger connections.
            - Battery Energy Storage System (BESS) site selection on constrained feeders.
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
        "Long-Term Phase: Advanced ADMS, AMI Topology & Smart Grid Operations"
    )

    with st.expander("📌 SGRM Strategic Scope & Action Items", expanded=True):
        col_l_a, col_l_b = st.columns(2)
        with col_l_a:
            st.markdown("""
            **Advanced Distribution Management System (ADMS)**
            - Seamless integration of SCADA, GIS, and OMS into a unified ADMS engine.
            - Fault Location, Isolation, and Service Restoration (FLISR) automation.
            """)
        with col_l_b:
            st.markdown("""
            **Smart AMI & Voltage Optimization**
            - Automated Volt-VAR Optimization (VVO) and dynamic peak load shaving.
            - Meter-to-transformer link mapping with real-time AMI connectivity sync.
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
