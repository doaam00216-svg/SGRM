import base64
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

# Inline SVG representations of logo & header graphics (No external files needed)
GIZ_LOGO_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 80" width="100%">
  <rect width="300" height="80" fill="#ffffff"/>
  <text x="20" y="50" font-family="Arial, sans-serif" font-size="36" font-weight="bold" fill="#d90429">giz</text>
  <text x="90" y="38" font-family="Arial, sans-serif" font-size="10" fill="#333333">Deutsche Gesellschaft</text>
  <text x="90" y="50" font-family="Arial, sans-serif" font-size="10" fill="#333333">für Internationale</text>
  <text x="90" y="62" font-family="Arial, sans-serif" font-size="10" fill="#333333">Zusammenarbeit (GIZ) GmbH</text>
</svg>"""

EEHC_BANNER_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 120" width="100%">
  <rect width="800" height="120" fill="#f8f9fa" rx="8"/>
  <text x="30" y="45" font-family="Segoe UI, Arial" font-size="22" font-weight="bold" fill="#0d3b66">EEHC Smart Grid Implementation Plan</text>
  <text x="30" y="75" font-family="Segoe UI, Arial" font-size="14" fill="#495057">Egyptian Electricity Holding Company | 9 Distribution Companies</text>
  <circle cx="700" cy="60" r="35" fill="#0d3b66" opacity="0.1"/>
  <path d="M700 35 L685 65 L700 65 L695 85 L715 55 L700 55 Z" fill="#d90429"/>
</svg>"""

SKYLINE_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 100" preserveAspectRatio="none" width="100%">
  <path d="M0,100 L0,80 L20,80 L20,50 L40,50 L40,80 L60,80 L60,30 L80,30 L80,80 L100,80 L100,60 L120,60 L120,100 Z" fill="#0d3b66" opacity="0.15"/>
  <path d="M150,100 L150,40 L180,20 L210,40 L210,100 Z" fill="#0d3b66" opacity="0.12"/>
  <path d="M250,100 L250,70 L280,70 L280,45 L310,45 L310,100 Z" fill="#0d3b66" opacity="0.15"/>
  <path d="M400,100 L400,20 L410,10 L420,20 L420,100 Z" fill="#0d3b66" opacity="0.2"/>
  <path d="M500,100 L500,60 L550,60 L550,100 Z" fill="#0d3b66" opacity="0.1"/>
  <path d="M650,100 L650,30 L690,30 L690,100 Z" fill="#0d3b66" opacity="0.15"/>
  <path d="M800,100 L800,50 L840,50 L840,100 Z" fill="#0d3b66" opacity="0.12"/>
  <path d="M950,100 L950,25 L970,10 L990,25 L990,100 Z" fill="#0d3b66" opacity="0.18"/>
  <path d="M1050,100 L1050,65 L1100,65 L1100,100 Z" fill="#0d3b66" opacity="0.1"/>
</svg>"""

skyline_b64 = base64.b64encode(SKYLINE_SVG.encode("utf-8")).decode("utf-8")
skyline_uri = f"data:image/svg+xml;base64,{skyline_b64}"

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
        height: 100px;
        background-image: url('{skyline_uri}');
        background-repeat: repeat-x;
        background-position: bottom center;
        background-size: contain;
        pointer-events: none;
        z-index: 0;
    }}

    /* Corporate Typography */
    h1, h2, h3, h4 {{
        color: #0d3b66 !important;
        font-family: 'Segoe UI', Arial, sans-serif;
        font-weight: 700;
    }}

    /* Phase Tabs Styling */
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
# 3. BRANDED HEADER BANNER
# =========================================================
head_col1, head_col2 = st.columns([1, 3.5])

with head_col1:
    st.markdown(
        f'<div style="text-align:center;">{GIZ_LOGO_SVG}</div>',
        unsafe_allow_html=True,
    )
    st.caption("In cooperation with GIZ")

with head_col2:
    st.markdown(
        f"<div>{EEHC_BANNER_SVG}</div>",
        unsafe_allow_html=True,
    )

st.markdown("---")

# =========================================================
# 4. DASHBOARD TITLE & METRICS
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


def render_map_card(title, caption, map_id):
    """Renders map cards cleanly with structured placeholder fallback."""
    st.markdown(f"#### {title}")
    st.markdown(
        f"""
        <div style="border: 2px dashed #cbd5e1; border-radius: 8px; padding: 25px; background-color: #f8fafc; text-align: center;">
            <p style="font-size: 28px; margin: 0;">🗺️</p>
            <p style="font-weight: bold; color: #0d3b66; margin: 5px 0;">{title}</p>
            <p style="color: #64748b; font-size: 13px; margin: 0;">Map Asset ID: <code>{map_id}.png</code></p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.caption(caption)


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
        render_map_card(
            "1. Asset Record Concept Map",
            "Red MV grid topology map with asset attribute records",
            "01_asset_record",
        )

        render_map_card(
            "3. MV Network Drawing & Acceptance Map",
            "GIS mapping canvas with MV network nodes along Mohamed Abu El Fetouh Hassab St.",
            "03_mv_drawing",
        )

    with col_s2:
        render_map_card(
            "2. Smouha GIS Web Interface",
            "OpenStreetMap vector view showing kiosk details in Smouha",
            "02_smouha_web",
        )

        render_map_card(
            "4. GIS Rollout Monitoring Dashboard",
            "City-wide feeder acceptance tracking across Capture, Verify, Approve stages",
            "04_gis_monitoring",
        )

    render_map_card(
        "5. Alexandria Regional Distribution Network Map",
        "Overview of Alexandria regional distribution network (منطقة الإسكندرية)",
        "05_alexandria_map",
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
        render_map_card(
            "6. Low-Voltage Network Expansion (Wall Boxes)",
            "Street-level mapping of LV wall distribution boxes along Qanal El Mahmoudeya St.",
            "06_lv_expansion",
        )

        render_map_card(
            "8. Fleet & Field Workforce Management",
            "Real-time field vehicle dispatching and work location routing",
            "08_fleet_workforce",
        )

        render_map_card(
            "10. Loss Analysis & Energy Cost Visibility",
            "Metered boundary zones and transformer imbalance investigation areas",
            "10_loss_analysis",
        )

        render_map_card(
            "12. Power Quality Assessment & Response",
            "Feeder trace monitoring for voltage events, unbalance, and harmonics",
            "12_power_quality",
        )

    with col_m2:
        render_map_card(
            "7. Asset Management Interface",
            "Interactive GIS view of transformer asset parameters (ELMACO 800 KVA)",
            "07_asset_mgmt",
        )

        render_map_card(
            "9. Outage Management System (OMS)",
            "Fault trace schematic isolating impacted customer areas and feeder switches",
            "09_oms",
        )

        render_map_card(
            "11. Renewable & EV Connection Screening",
            "Coastal grid headroom map highlighting constrained vs available capacity",
            "11_renewable",
        )

        render_map_card(
            "13. Battery Energy Storage System (BESS) Support",
            "Candidate battery storage siting along constrained distribution feeders",
            "13_battery_storage",
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
        render_map_card(
            "14. ADMS & Restoration Automation",
            "Automated fault section isolation and switching restoration paths",
            "14_adms",
        )

        render_map_card(
            "16. Smart AMI Integration",
            "Smart meter link mapping, outage indications, and load profile analytics",
            "16_ami_integration",
        )

    with col_l2:
        render_map_card(
            "15. Voltage Optimization & Peak Management",
            "Grid control assets, real-time voltage profiles, and demand trace curves",
            "15_voltage_optimization",
        )
