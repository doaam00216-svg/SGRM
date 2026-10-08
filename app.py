import base64
import os
import streamlit as st

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Smart Grid Roadmap (SGRM)",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)


# -----------------------------------------------------------------------------
# 2. HELPER FUNCTION & CSS BACKGROUND OVERLAYS
# -----------------------------------------------------------------------------
def get_base64_image(image_path):
    """Converts a local image file to a Base64 string for CSS background rendering."""
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    return ""


# Load Base64 strings for background overlays
skyline_b64 = get_base64_image("images/bg_city_skyline.png")
eehc_b64 = get_base64_image("images/bg_eehc_banner.png")
asset_rec_b64 = get_base64_image(
    "images/01_Strategic_objectives_Asset_record.png"
)

# Inject custom CSS styles and background overlays
css_code = f"""
<style>
/* App background color & default fonts */
.stApp {{
    background-color: #F8FAFC !important;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
}}

/* Background 3: City Skyline Watermark (Fixed Bottom Right) */
.stApp::after {{
    content: "";
    position: fixed;
    bottom: 0;
    right: 0;
    width: 100%;
    height: 120px;
    background-image: url('data:image/png;base64,{skyline_b64}');
    background-repeat: no-repeat;
    background-position: bottom right;
    background-size: contain;
    opacity: 0.18;
    pointer-events: none;
    z-index: 0;
}}

/* Background 2: Roadmap Dashboard Banner Header */
.roadmap-banner-bg {{
    background: linear-gradient(rgba(15, 23, 42, 0.88), rgba(15, 23, 42, 0.88)), 
                url('data:image/png;base64,{eehc_b64}');
    background-repeat: no-repeat;
    background-position: center right;
    background-size: cover;
    border-radius: 16px;
    padding: 28px 36px;
    color: white;
    margin-bottom: 24px;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.12);
}}
.roadmap-banner-bg h1 {{
    color: #FFFFFF !important;
    font-size: 2.2rem;
    font-weight: 800;
    margin: 0;
}}
.roadmap-banner-bg p {{
    color: #94A3B8;
    font-size: 1.05rem;
    margin-top: 6px;
    margin-bottom: 0;
}}

/* Background 1: Project Workspace Container Watermark */
.project-workspace-bg {{
    background-image: linear-gradient(rgba(255, 255, 255, 0.94), rgba(255, 255, 255, 0.94)), 
                url('data:image/png;base64,{asset_rec_b64}');
    background-repeat: no-repeat;
    background-position: center center;
    background-size: contain;
    padding: 24px;
    border-radius: 14px;
    border: 1px solid #E2E8F0;
}}
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 3. SIDEBAR NAVIGATION & FILTERS
# -----------------------------------------------------------------------------
with st.sidebar:
    # Branding Logo
    if os.path.exists("images/giz_logo.png"):
        st.image("images/giz_logo.png", use_container_width=True)

    st.title("⚡ SGRM Portal")
    st.markdown("---")

    main_view = st.radio(
        "Select View:",
        [
            "📊 Dashboard Overview",
            "🖼️ Implementation Gallery",
            "🛠️ Project Workspace",
        ],
    )

    st.markdown("---")
    st.markdown("### Quick Filters")
    selected_domain = st.selectbox(
        "Filter Domain:",
        [
            "All Domains",
            "IT Infrastructure (IF)",
            "Grid Operations (GO)",
            "Asset Management (AM)",
            "Commercial & Metering (CM)",
            "Planning & Renewable Energy (PR)",
        ],
    )

    selected_horizon = st.selectbox(
        "Filter Horizon:",
        ["All Horizons", "Short-Term", "Medium-Term", "Long-Term"],
    )


# -----------------------------------------------------------------------------
# 4. VIEW 1: DASHBOARD OVERVIEW
# -----------------------------------------------------------------------------
if main_view == "📊 Dashboard Overview":
    st.markdown(
        """
        <div class="roadmap-banner-bg">
            <h1>Smart Grid Roadmap (SGRM)</h1>
            <p>5 domains • 26 projects • 9 potential benefits | EEHC and Egypt's nine DISCOs</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # Key Metrics Bar
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Total Domains", value="5")
    m2.metric(label="Total Projects", value="26")
    m3.metric(label="Expected Benefits", value="9 Strategic Areas")
    m4.metric(label="Target Horizon", value="2026 – 2030+")

    st.markdown("---")

    # Overview Section with Image
    col_desc, col_img = st.columns([1.2, 1])
    with col_desc:
        st.subheader("Strategic Vision & Scope")
        st.write(
            """
        The Smart Grid Roadmap establishes a comprehensive modernization framework for Egyptian Electricity Holding Company (EEHC) 
        and its nine Electricity Distribution Companies (DISCOs). 

        It targets step-by-step technological digital transformation across GIS foundation establishing, medium and low-voltage network 
        digitization, automated outage handling, and advanced renewable integration.
        """
        )
    with col_img:
        if os.path.exists("images/01_Strategic_objectives_Asset_record.png"):
            st.image(
                "images/01_Strategic_objectives_Asset_record.png",
                caption="Strategic Objectives - Asset Record Schema",
                use_container_width=True,
            )


# -----------------------------------------------------------------------------
# 5. VIEW 2: IMPLEMENTATION GALLERY (ALL 16 PRESENTATION IMAGES)
# -----------------------------------------------------------------------------
elif main_view == "🖼️ Implementation Gallery":
    st.markdown("## 🖼️ Implementation Gallery")
    st.write(
        "Structured step-by-step visualization of all roadmap implementation deliverables."
    )

    # SHORT-TERM HORIZON
    if selected_horizon in ["All Horizons", "Short-Term"]:
        st.markdown("### 🟡 Short-Term Horizon (Jan 2026 – Jun 2027)")
        st.caption(
            "Establishing central GIS foundations, MV connectivity, and monitoring infrastructure."
        )

        st1, st2 = st.columns(2)
        with st1:
            if os.path.exists(
                "images/02_Established_central_GIS_foundation.jpg"
            ):
                st.image(
                    "images/02_Established_central_GIS_foundation.jpg",
                    caption="1. Established Central GIS Foundation (Smouha Proof)",
                    use_container_width=True,
                )
            if os.path.exists(
                "images/03_MV_network_drawing_and_acceptance.jpg"
            ):
                st.image(
                    "images/03_MV_network_drawing_and_acceptance.jpg",
                    caption="2. MV Network Drawing and Connectivity Acceptance",
                    use_container_width=True,
                )

        with st2:
            if os.path.exists(
                "images/04_Continuous_updates_and_rollout_monitoring.png"
            ):
                st.image(
                    "images/04_Continuous_updates_and_rollout_monitoring.png",
                    caption="3. Continuous Updates and Rollout Monitoring",
                    use_container_width=True,
                )
            if os.path.exists(
                "images/05_Expected_short_term_network_record.png"
            ):
                st.image(
                    "images/05_Expected_short_term_network_record.png",
                    caption="4. Expected Short-Term Network Record (Alexandria)",
                    use_container_width=True,
                )

        st.markdown("---")

    # MEDIUM-TERM HORIZON
    if selected_horizon in ["All Horizons", "Medium-Term"]:
        st.markdown("### 🔵 Medium-Term Horizon (Jun 2027 – May 2030)")
        st.caption(
            "LV network expansion, asset health, workforce management, and OMS integration."
        )

        mt1, mt2 = st.columns(2)
        with mt1:
            if os.path.exists("images/06_LV_network_expansion.jpg"):
                st.image(
                    "images/06_LV_network_expansion.jpg",
                    caption="5. LV Network Expansion – Pillar & Wall Box Mapping",
                    use_container_width=True,
                )
            if os.path.exists(
                "images/07_Asset_Management_and_Maintenance.jpg"
            ):
                st.image(
                    "images/07_Asset_Management_and_Maintenance.jpg",
                    caption="6. Asset Management & Maintenance - Transformer Status",
                    use_container_width=True,
                )
            if os.path.exists(
                "images/08_Fleet_and_Field_Workforce_Management.jpg"
            ):
                st.image(
                    "images/08_Fleet_and_Field_Workforce_Management.jpg",
                    caption="7. Fleet and Field Workforce Management",
                    use_container_width=True,
                )
            if os.path.exists("images/09_Outage_Management_System.png"):
                st.image(
                    "images/09_Outage_Management_System.png",
                    caption="8. Outage Management System (OMS) Incident Isolation",
                    use_container_width=True,
                )

        with mt2:
            if os.path.exists(
                "images/10_Loss_Analysis_and_Energy_Cost_Visibility.png"
            ):
                st.image(
                    "images/10_Loss_Analysis_and_Energy_Cost_Visibility.png",
                    caption="9. Loss Analysis & Energy Cost Visibility",
                    use_container_width=True,
                )
            if os.path.exists(
                "images/11_Renewable_Energy_and_EV_Connection_Planning.png"
            ):
                st.image(
                    "images/11_Renewable_Energy_and_EV_Connection_Planning.png",
                    caption="10. Renewable Energy & EV Connection Planning",
                    use_container_width=True,
                )
            if os.path.exists(
                "images/12_Power_Quality_Assessment_and_Response.png"
            ):
                st.image(
                    "images/12_Power_Quality_Assessment_and_Response.png",
                    caption="11. Power Quality Assessment & Response",
                    use_container_width=True,
                )
            if os.path.exists(
                "images/13_Battery_Energy_Storage_for_Grid_Support.png"
            ):
                st.image(
                    "images/13_Battery_Energy_Storage_for_Grid_Support.png",
                    caption="12. Battery Energy Storage for Grid Support",
                    use_container_width=True,
                )

        st.markdown("---")

    # LONG-TERM HORIZON
    if selected_horizon in ["All Horizons", "Long-Term"]:
        st.markdown("### 🟢 Long-Term Horizon (May 2030 Onward)")
        st.caption(
            "Fully automated distribution (ADMS), peak management, and AMI smart metering."
        )

        lt1, lt2 = st.columns(2)
        with lt1:
            if os.path.exists(
                "images/14_ADMS_and_Restoration_Automation.png"
            ):
                st.image(
                    "images/14_ADMS_and_Restoration_Automation.png",
                    caption="13. ADMS & Restoration Automation",
                    use_container_width=True,
                )
            if os.path.exists(
                "images/15_Voltage_Optimization_and_Peak_Management.png"
            ):
                st.image(
                    "images/15_Voltage_Optimization_and_Peak_Management.png",
                    caption="14. Voltage Optimization & Peak Management",
                    use_container_width=True,
                )

        with lt2:
            if os.path.exists(
                "images/16_Advanced_Metering_Infrastructure_Integration.png"
            ):
                st.image(
                    "images/16_Advanced_Metering_Infrastructure_Integration.png",
                    caption="15. Advanced Metering Infrastructure (AMI) Integration",
                    use_container_width=True,
                )


# -----------------------------------------------------------------------------
# 6. VIEW 3: PROJECT WORKSPACE
# -----------------------------------------------------------------------------
else:
    # Encapsulated inside Background Image 1 Container
    st.markdown('<div class="project-workspace-bg">', unsafe_allow_html=True)

    st.title("🛠️ Project Details Workspace")
    st.write(
        "Select an active project module below to view technical specification, architectural layout, and deliverables."
    )

    project_id = st.selectbox(
        "Choose Project Module:",
        [
            "IF2: Asset Management Design & Implementation (GIS Rollout)",
            "GO1: Advanced Distribution Management System (ADMS)",
            "AM1: Condition-Based Asset Maintenance",
            "CM1: Smart Metering & AMI Rollout",
        ],
    )

    st.markdown("---")

    if "IF2" in project_id:
        st.subheader(
            "IF2: Asset Management Design & Implementation (GIS Rollout)"
        )

        tabs = st.tabs(["📋 Overview", "🖼️ System Visuals", "📊 Milestones"])

        with tabs[0]:
            st.write(
                """
            **Domain:** IT Infrastructure (IF)  
            **Lead Target:** Alexandria Electricity Distribution Company (AEDC) & Central GIS  
            **Objective:** Establish unified central GIS data models for MV and LV distribution network assets.
            """
            )

        with tabs[1]:
            col_a, col_b = st.columns(2)
            with col_a:
                if os.path.exists(
                    "images/02_Established_central_GIS_foundation.jpg"
                ):
                    st.image(
                        "images/02_Established_central_GIS_foundation.jpg",
                        caption="Smouha Proof of Connection Interface",
                        use_container_width=True,
                    )
            with col_b:
                if os.path.exists(
                    "images/03_MV_network_drawing_and_acceptance.jpg"
                ):
                    st.image(
                        "images/03_MV_network_drawing_and_acceptance.jpg",
                        caption="MV Network Drawing Acceptance Model",
                        use_container_width=True,
                    )

        with tabs[2]:
            st.markdown(
                """
            - [x] Central GIS Schema Finalized (Short-Term)
            - [x] Smouha Proof-of-Concept Connected (Short-Term)
            - [ ] LV Network Pillars Mapping (Medium-Term)
            - [ ] Full DISCO Integration (Long-Term)
            """
            )

    else:
        st.subheader(project_id)
        st.info("Select project deliverables available in the main gallery.")

    st.markdown("</div>", unsafe_allow_html=True)
