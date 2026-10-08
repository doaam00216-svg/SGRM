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

# Direct GitHub repository asset URLs from your project README
GIZ_LOGO_URL = "https://github.com/user-attachments/assets/ee083587-4ccf-4a3b-b9fa-aecbc1b1d92a"
EEHC_BANNER_URL = "https://github.com/user-attachments/assets/6e2cbda8-2dbb-43fb-b3e1-d2f62cbbaab9"
SKYLINE_WATERMARK_URL = "https://github.com/user-attachments/assets/2c15ab31-e4eb-44c7-a9a3-c19d4b306fc2"

RAW_IMG_BASE = (
    "https://raw.githubusercontent.com/doaam00216-svg/SGRM/main/images/"
)


def display_img(file_name, caption=None, use_container_width=True):
    """Displays slide image with local/GitHub fallback."""
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
# 2. BRANDED HEADER & BACKGROUND CSS
# =========================================================
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: #ffffff !important;
        color: #1a202c !important;
    }}
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
        opacity: 0.25;
        pointer-events: none;
        z-index: 0;
    }}
    h1, h2, h3, h4 {{
        color: #0d3b66 !important;
        font-family: 'Segoe UI', Arial, sans-serif;
        font-weight: 700;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# Header Banner
head_col1, head_col2 = st.columns([1, 3.5])
with head_col1:
    st.image(
        GIZ_LOGO_URL, caption="In cooperation with GIZ", use_container_width=True
    )
with head_col2:
    st.image(EEHC_BANNER_URL, use_container_width=True)

st.markdown("---")

# Initialize session state for selected project
if "selected_project" not in st.session_state:
    st.session_state.selected_project = None

# Sidebar Navigation
st.sidebar.title("🧭 SGRM Navigation")
nav_choice = st.sidebar.radio(
    "Select View:", ["1. Master SGRM (26 Projects)", "2. Project IF2: GIS Detail View"]
)

# =========================================================
# VIEW 1: MASTER SGRM (THE 26 PROJECTS)
# =========================================================
if nav_choice == "1. Master SGRM (26 Projects)":
    st.title("⚡ EEHC Master Smart Grid Roadmap (SGRM)")
    st.markdown(
        "##### Egyptian Electricity Holding Company — 26 Strategic Smart Grid Projects"
    )

    st.info(
        "💡 **Interactive Tip:** Click on **IF2 (Enterprise GIS)** below or select it in the sidebar to view the detailed GIS implementation phase and map proofs."
    )

    # 26 Projects Category Columns
    col_if, col_so, col_am, col_sg = st.columns(4)

    with col_if:
        st.subheader("🏗️ Infrastructure (IF)")
        if st.button("📍 IF1: Substation Automation"):
            st.warning("IF1 selected.")
        if st.button("🗺️ **IF2: Enterprise GIS Integration**", type="primary"):
            st.session_state.selected_project = "IF2"
            st.rerun()
        if st.button("📡 IF3: Fiber/Telecom Network"):
            pass
        if st.button("🔒 IF4: OT Cybersecurity Framework"):
            pass
        if st.button("☁️ IF5: Central Data Center"):
            pass
        if st.button("🔄 IF6: Enterprise Integration Bus"):
            pass
        if st.button("⚡ IF7: Smart Meter Infrastructure"):
            pass

    with col_so:
        st.subheader("⚙️ Smart Operations (SO)")
        if st.button("🎮 SO1: SCADA/EMS Upgrade"):
            pass
        if st.button("⚡ SO2: Advanced DMS (ADMS)"):
            pass
        if st.button("🚨 SO3: Outage Management (OMS)"):
            pass
        if st.button("🔄 SO4: FLISR Automation"):
            pass
        if st.button("📊 SO5: Loss Reduction Analytics"):
            pass
        if st.button("📈 SO6: Demand Response (DR)"):
            pass
        if st.button("🔋 SO7: BESS/DER Integration"):
            pass

    with col_am:
        st.subheader("📊 Asset Mgmt (AM)")
        if st.button("🏭 AM1: Asset Lifecycle (EAM)"):
            pass
        if st.button("🌡️ AM2: Transformer Condition"):
            pass
        if st.button("👷 AM3: Workforce Dispatch"):
            pass
        if st.button("🛠️ AM4: Predictive Maintenance"):
            pass
        if st.button("📦 AM5: Smart Inventory"):
            pass
        if st.button("📋 AM6: Grid Asset Registry"):
            pass

    with col_sg:
        st.subheader("🌐 Grid Intelligence (GI)")
        if st.button("📉 GI1: Power Quality (PQM)"):
            pass
        if st.button("🔌 GI2: EV Charging Integration"):
            pass
        if st.button("☀️ GI3: Solar Interconnection"):
            pass
        if st.button("🤖 GI4: Grid Digital Twin"):
            pass
        if st.button("🧠 GI5: AI Load Forecasting"):
            pass
        if st.button("📈 GI6: Advanced Analytics"):
            pass

# =========================================================
# VIEW 2: DETAILED IF2 (ENTERPRISE GIS) ROADMAP & MAP PROOFS
# =========================================================
else:
    st.title("🗺️ Project IF2: Enterprise GIS Implementation Roadmap")
    st.markdown(
        "##### Deep-Dive Execution Plan and Visual Map Proofs for Project IF2"
    )

    tab_short, tab_medium, tab_long = st.tabs([
        "🚩 Short-Term Phase (2026 – 2027)",
        "🚀 Medium-Term Phase (2027 – 2030)",
        "🌐 Long-Term Phase (2030+)",
    ])

    # ---------------------------------------------------------
    # SHORT-TERM PHASE
    # ---------------------------------------------------------
    with tab_short:
        st.header("Short-Term: Central GIS Foundation & Network Records")
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
        st.header("Medium-Term: LV Expansion, OMS & Operational Applications")
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.markdown("#### 6. Low-Voltage Network Expansion")
            display_img(
                "06_lv_expansion.png",
                caption="Street-level mapping of LV wall distribution boxes",
            )
            st.markdown("#### 8. Fleet & Workforce Management")
            display_img(
                "08_fleet_workforce.png",
                caption="Real-time field vehicle dispatching and routing",
            )
            st.markdown("#### 10. Loss Analysis & Energy Costing")
            display_img(
                "10_loss_analysis.png",
                caption="Metered boundary zones and imbalance areas",
            )
            st.markdown("#### 12. Power Quality Response")
            display_img(
                "12_power_quality.png",
                caption="Feeder trace monitoring for voltage events",
            )

        with col_m2:
            st.markdown("#### 7. Asset Management Interface")
            display_img(
                "07_asset_mgmt.png",
                caption="Interactive GIS view of transformer parameters",
            )
            st.markdown("#### 9. Outage Management System (OMS)")
            display_img(
                "09_oms.png", caption="Fault trace schematic isolating outages"
            )
            st.markdown("#### 11. Renewable Connection Screening")
            display_img(
                "11_renewable.png",
                caption="Grid headroom map for solar/EV screening",
            )
            st.markdown("#### 13. Battery Storage Support")
            display_img(
                "13_battery_storage.png",
                caption="Candidate battery storage siting along feeders",
            )

    # ---------------------------------------------------------
    # LONG-TERM PHASE
    # ---------------------------------------------------------
    with tab_long:
        st.header("Long-Term: ADMS Integration & Smart Operations")
        col_l1, col_l2 = st.columns(2)
        with col_l1:
            st.markdown("#### 14. ADMS Restoration Automation")
            display_img(
                "14_adms.png",
                caption="Automated fault isolation and restoration switching",
            )
            st.markdown("#### 16. Smart AMI Integration")
            display_img(
                "16_ami_integration.png",
                caption="Smart meter mapping and real-time analytics",
            )

        with col_l2:
            st.markdown("#### 15. Voltage Optimization & Peak Management")
            display_img(
                "15_voltage_optimization.png",
                caption="Grid control assets and demand trace curves",
            )
