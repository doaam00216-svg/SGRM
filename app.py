import base64
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

# Base path configuration
IMAGE_DIR = "images"

# =========================================================
# 2. HELPER FUNCTIONS FOR ROBUST IMAGE & EMBEDDED RENDERING
# =========================================================


def get_base64_image(file_path):
    """Loads a local image and converts it to Base64 for CSS backgrounds."""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""


def safe_image(file_name, caption=None, use_container_width=True):
    """Safely renders slide images or fallback placeholders if missing."""
    path = os.path.join(IMAGE_DIR, file_name)
    if os.path.exists(path):
        st.image(path, caption=caption, use_container_width=use_container_width)
    elif os.path.exists(file_name):
        st.image(
            file_name, caption=caption, use_container_width=use_container_width
        )
    else:
        st.info(f"📍 **Map Graphic:** `{file_name}` (Place in `images/` folder)")


# Load background skyline base64 string
skyline_b64 = get_base64_image(os.path.join(IMAGE_DIR, "skyline_footer.png"))
bg_css_skyline = (
    f"data:image/png;base64,{skyline_b64}"
    if skyline_b64
    else "https://raw.githubusercontent.com/placeholder/skyline.png"
)

# =========================================================
# 3. PRESENTATION MATCHED WHITE THEME & BRANDING CSS
# =========================================================
st.markdown(
    f"""
    <style>
    /* Clean White Presentation Background */
    .stApp {{
        background-color: #ffffff !important;
        color: #1a202c !important;
    }}

    /* Fixed City Skyline Watermark at the bottom of the page */
    .stApp::after {{
        content: "";
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        height: 110px;
        background-image: url('{bg_css_skyline}');
        background-repeat: repeat-x;
        background-position: bottom center;
        background-size: contain;
        opacity: 0.25;
        pointer-events: none;
        z-index: 0;
    }}

    /* Typography & Corporate Headers */
    h1, h2, h3, h4 {{
        color: #0d3b66 !important;
        font-family: 'Segoe UI', Arial, sans-serif;
        font-weight: 700;
    }}

    /* Phase Tabs Custom Design */
    .stTabs [data-baseweb="tab-list"] {{
        background-color: #f8f9fa;
        border-bottom: 2px solid #dee2e6;
        gap: 8px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        color: #495057;
        font-weight: 600;
        padding: 12px 20px;
        border-radius: 4px 4px 0 0;
    }}

    .stTabs [aria-selected="true"] {{
        color: #d90429 !important; /* GIZ Red Highlight */
        background-color: #ffffff !important;
        border-bottom: 3px solid #d90429 !important;
    }}

    /* Expander Container Styling */
    .streamlit-expanderHeader {{
        background-color: #f1f5f9 !important;
        border-radius: 6px;
        color: #0f172a !important;
        font-weight: 600;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# 4. BRANDED HEADER BANNER (GIZ & EEHC GRAPHICS)
# =========================================================
head_col1, head_col2 = st.columns([1, 3.5])

with head_col1:
    safe_image("giz_logo.png", caption="In cooperation with GIZ")

with head_col2:
    safe_image("eehc_header_banner.png")

st.markdown("---")

# =========================================================
# 5. DASHBOARD TITLE & EXECUTIVE SUMMARY METRICS
# =========================================================
st.title("⚡ EEHC Smart Grid Roadmap (SGRM)")
st.markdown(
    "##### Egyptian Electricity Holding Company — Enterprise Smart Grid Implementation & GIS Integration Dashboard"
)

m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Short-Term", "Jan 2026 – Jun 2027", "Foundation")
m2.metric("Medium-Term", "Jun 2027 – May 2030", "Expansion")
m3.metric("Long-Term", "May 2030+", "Smart Grid Integration")
m4.metric("DISCO Network Scope", "9 Distribution Co.", "EEHC Grid")
m5.metric("Slide Visual Assets", "16 Map Proofs", "Verified")

st.markdown("---")

# =========================================================
# 6. FULL SMART GRID ROADMAP (PHASE TABS)
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

    # Full Smart Grid Scope Expanders
    with st.expander("📌 Smart Grid Strategic Pillars (Short-Term)", expanded=True):
        col_s_a, col_s_b = st.columns(2)
        with col_s_a:
            st.markdown("""
            **1. Geographic Information System (GIS)**
            - Establish Centralized Enterprise GIS Database Schema across EEHC.
            - Standardize data model for Medium Voltage (MV) grid topology.
            - Execute digital vectorization for feeders, kiosks, and substations.
            
            **2. SCADA & Substation Automation**
            - Complete SCADA master station upgrades in high-priority zones.
            - Integrate Remote Terminal Units (RTUs) for main MV distribution nodes.
            """)
        with col_s_b:
            st.markdown("""
            **3. Advanced Metering Infrastructure (AMI) & IT**
            - Finalize head-end system (HES) integration for commercial industrial meters.
            - Define IT/OT cybersecurity protocols and data governance framework.
            
            **4. Organizational Capability**
            - Establish DISCO GIS data verification teams and quality control workflows.
            """)

    st.markdown("---")
    st.subheader("🗺️ Short-Term Map Proofs & System Interfaces")

    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.markdown("#### 1. Asset Record Concept Map")
        safe_image(
            "01_asset_record.png",
            caption="Red MV grid topology map with asset attribute records",
        )

        st.markdown("#### 3. MV Network Drawing & Acceptance Map")
        safe_image(
            "03_mv_drawing.png",
            caption="GIS mapping canvas with MV network nodes along Mohamed Abu El Fetouh Hassab St.",
        )

    with col_s2:
        st.markdown("#### 2. Smouha GIS Web Interface")
        safe_image(
            "02_smouha_web.png",
            caption="OpenStreetMap vector view showing kiosk details in Smouha",
        )

        st.markdown("#### 4. GIS Rollout Monitoring Dashboard")
        safe_image(
            "04_gis_monitoring.png",
            caption="City-wide feeder acceptance tracking across Capture, Verify, Approve stages",
        )

    st.markdown("#### 5. Alexandria Regional Distribution Network Map")
    safe_image(
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
            **1. Low-Voltage Network Digitization & GIS**
            - Complete street-level LV wall box mapping and service connection tracing.
            - Integrate asset lifecycle maintenance interfaces (e.g., Transformer parameter logs).
            
            **2. Outage Management System (OMS) & Field Ops**
            - Deploy GIS-centric Outage Management Systems (OMS) for rapid fault identification.
            - Enable automated Fleet & Workforce Dispatch for maintenance crews.
            """)
        with col_m_b:
            st.markdown("""
            **3. Energy Loss & Power Quality Analytics**
            - Establish Boundary Metering Zones for commercial and technical loss calculations.
            - Continuous feeder trace monitoring for voltage events, unbalance, and harmonics.
            
            **4. Renewable & Distributed Energy Resource (DER) Integration**
            - Implement grid headroom screening maps for rooftop solar and EV charger interconnections.
            - Conduct candidate battery storage (BESS) site screening on overloaded feeders.
            """)

    st.markdown("---")
    st.subheader("🗺️ Medium-Term Operational GIS Applications")

    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.markdown("#### 6. Low-Voltage Network Expansion (Wall Boxes)")
        safe_image(
            "06_lv_expansion.png",
            caption="Street-level mapping of LV wall distribution boxes along Qanal El Mahmoudeya St.",
        )

        st.markdown("#### 8. Fleet & Field Workforce Management")
        safe_image(
            "08_fleet_workforce.png",
            caption="Real-time field vehicle dispatching and work location routing",
        )

        st.markdown("#### 10. Loss Analysis & Energy Cost Visibility")
        safe_image(
            "10_loss_analysis.png",
            caption="Metered boundary zones and transformer imbalance investigation areas",
        )

        st.markdown("#### 12. Power Quality Assessment & Response")
        safe_image(
            "12_power_quality.png",
            caption="Feeder trace monitoring for voltage events, unbalance, and harmonics",
        )

    with col_m2:
        st.markdown("#### 7. Asset Management & Maintenance Interface")
        safe_image(
            "07_asset_mgmt.png",
            caption="Interactive GIS view of transformer asset parameters (ELMACO 800 KVA)",
        )

        st.markdown("#### 9. Outage Management System (OMS)")
        safe_image(
            "09_oms.png",
            caption="Fault trace schematic isolating impacted customer areas and feeder switches",
        )

        st.markdown("#### 11. Renewable & EV Connection Screening")
        safe_image(
            "11_renewable.png",
            caption="Coastal grid headroom map highlighting constrained vs available capacity",
        )

        st.markdown("#### 13. Battery Energy Storage System (BESS) Support")
        safe_image(
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
            - Full integration of SCADA, GIS, and OMS into a unified ADMS control engine.
            - Deploy Fault Location, Isolation, and Service Restoration (FLISR) automation.
            
            **2. Voltage Optimization & Peak Management**
            - Automated Volt-VAR Optimization (VVO) across distribution substations.
            - Dynamic peak shaving using customer demand-response analytics.
            """)
        with col_l_b:
            st.markdown("""
            **3. Full AMI & Smart Meter Topology**
            - Complete meter-to-transformer link mapping with real-time AMI connectivity sync.
            - Automated low-voltage outage detection via smart meter last-gasp alerts.
            """)

    st.markdown("---")
    st.subheader("🗺️ Long-Term Advanced Operation Systems")

    col_l1, col_l2 = st.columns(2)
    with col_l1:
        st.markdown("#### 14. ADMS & Restoration Automation")
        safe_image(
            "14_adms.png",
            caption="Automated fault section isolation and switching restoration paths",
        )

        st.markdown("#### 16. Smart AMI Integration")
        safe_image(
            "16_ami_integration.png",
            caption="Smart meter link mapping, outage indications, and load profile analytics",
        )

    with col_l2:
        st.markdown("#### 15. Voltage Optimization & Peak Management")
        safe_image(
            "15_voltage_optimization.png",
            caption="Grid control assets, real-time voltage profiles, and demand trace curves",
        )
