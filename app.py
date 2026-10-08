import base64
import glob
import os
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="EEHC Smart Grid Roadmap Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Helper function to find existing file regardless of single/double extensions (.jpg.png, .png.png, etc.)
def find_existing_image(base_path):
    if os.path.exists(base_path):
        return base_path

    # Extract base name without any extension
    folder, filename = os.path.split(base_path)
    clean_name = filename.split(".")[0]

    # Look for matching pattern in the images directory
    search_pattern = os.path.join(folder, f"{clean_name}*")
    matches = glob.glob(search_pattern)

    if matches:
        return matches[0]

    return None


# Helper function to safely encode local images to Base64
def get_base64_image(image_path):
    real_path = find_existing_image(image_path)
    if real_path and os.path.exists(real_path):
        with open(real_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    return ""


# Helper function to safely render local images with custom width option
def display_safe_image(file_path, caption="", width=None):
    real_path = find_existing_image(file_path)

    if real_path and os.path.exists(real_path):
        if width:
            st.image(real_path, caption=caption, width=width)
        else:
            st.image(real_path, caption=caption, use_container_width=True)
    else:
        st.warning(f"⚠️ Image file missing: `{file_path}`")


# Base64 background assets
skyline_b64 = get_base64_image("images/bg_city_skyline.png")
eehc_b64 = get_base64_image("images/bg_eehc_banner.png")
asset_rec_b64 = get_base64_image(
    "images/01_Strategic_objectives_Asset_record.png"
)

# 2. Custom CSS Styles
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: #F8FAFC !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }}
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
    .top-banner {{
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%), 
                    url('data:image/png;base64,{eehc_b64}');
        background-repeat: no-repeat;
        background-position: center right;
        background-size: cover;
        border-radius: 16px;
        padding: 24px 32px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
    }}
    .top-banner h1 {{
        color: #FFFFFF !important;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
    }}
    .top-banner p {{
        color: #94A3B8;
        font-size: 1.05rem;
        margin-top: 6px;
        margin-bottom: 0;
    }}
    .domain-header {{
        border-radius: 12px 12px 0 0;
        padding: 12px 14px;
        color: white;
        font-weight: 700;
        font-size: 0.85rem;
        text-transform: uppercase;
    }}
    .dh-1 {{ background: #DC2626; }}
    .dh-2 {{ background: #0284C7; }}
    .dh-3 {{ background: #D97706; }}
    .dh-4 {{ background: #B91C1C; }}
    .dh-5 {{ background: #15803D; }}

    .benefit-card {{
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 12px 14px;
        margin-bottom: 10px;
    }}
    .benefit-code {{
        font-weight: 800;
        font-size: 1rem;
        color: #D9381E;
    }}
    .benefit-title {{
        font-size: 0.85rem;
        color: #334155;
        font-weight: 600;
    }}
    .gis-highlight {{
        background: #EFF6FF;
        border: 2px solid #2563EB !important;
        border-radius: 8px;
        padding: 4px;
        margin-bottom: 8px;
    }}
    .horizon-box {{
        background: white;
        border-left: 6px solid #2563EB;
        padding: 18px 24px;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }}
    .image-caption-card {{
        background: #F1F5F9;
        border-radius: 8px;
        padding: 10px 14px;
        margin-top: 8px;
        font-size: 0.85rem;
        color: #475569;
        border-left: 3px solid #0EA5E9;
    }}
    .project-workspace-container {{
        background-color: #FFFFFF;
        background-image: linear-gradient(rgba(255, 255, 255, 0.94), rgba(255, 255, 255, 0.94)), 
                    url('data:image/png;base64,{asset_rec_b64}');
        background-repeat: no-repeat;
        background-position: center center;
        background-size: contain;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# 3. Roadmap Data
DOMAINS = [
    {
        "id": 1,
        "title": "1. POLICY AND REGULATORY SUPPORT",
        "count": "4 PROJECTS",
        "header_class": "dh-1",
        "projects": [
            {
                "code": "PS1",
                "name": "Policy and regulatory review",
                "type": "support",
            },
            {
                "code": "PS2",
                "name": "Technical standards and regulation",
                "type": "support",
            },
            {
                "code": "PS3",
                "name": "Privacy and customer data ownership",
                "type": "support",
            },
            {"code": "PS4", "name": "Cybersecurity", "type": "support"},
        ],
    },
    {
        "id": 2,
        "title": "2. ORGANIZATIONAL SUPPORT",
        "count": "4 PROJECTS",
        "header_class": "dh-2",
        "projects": [
            {
                "code": "OS1",
                "name": "Business goals and use cases",
                "type": "support",
            },
            {"code": "OS2", "name": "Organizational KPIs", "type": "support"},
            {
                "code": "OS3",
                "name": "Asset management strategy",
                "type": "support",
            },
            {
                "code": "OS4",
                "name": "Smart grid governance",
                "type": "support",
            },
        ],
    },
    {
        "id": 3,
        "title": "3. INFRASTRUCTURE",
        "count": "6 PROJECTS",
        "header_class": "dh-3",
        "projects": [
            {
                "code": "IF1",
                "name": "Smart meters: commercial and industrial",
                "type": "direct",
            },
            {
                "code": "IF2",
                "name": "Asset management design and implementation",
                "type": "support",
                "active": True,
                "tag": "Includes GIS",
            },
            {
                "code": "IF3",
                "name": "Smart meters: residential >200 kWh/month",
                "type": "direct",
            },
            {
                "code": "IF4",
                "name": "Asset management and monitoring",
                "type": "direct",
            },
            {
                "code": "IF5",
                "name": "Smart Meter Plus: residential <200 kWh/month",
                "type": "direct",
            },
            {
                "code": "IF6",
                "name": "Phasor measurement units",
                "type": "direct",
            },
        ],
    },
    {
        "id": 4,
        "title": "4. TECHNOLOGY",
        "count": "7 PROJECTS",
        "header_class": "dh-4",
        "projects": [
            {
                "code": "TE1",
                "name": "Technology evaluation and selection",
                "type": "support",
            },
            {
                "code": "TE2",
                "name": "Integrated solution selection",
                "type": "support",
            },
            {
                "code": "TE3",
                "name": "Smart meter analytics",
                "type": "direct",
            },
            {"code": "TE4", "name": "PV and EV monitoring", "type": "direct"},
            {"code": "TE5", "name": "Demand response", "type": "direct"},
            {
                "code": "TE6",
                "name": "Demand-side management pilot",
                "type": "direct",
            },
            {"code": "TE7", "name": "Energy storage pilots", "type": "direct"},
        ],
    },
    {
        "id": 5,
        "title": "5. CUSTOMER ENGAGEMENT & ENV.",
        "count": "5 PROJECTS",
        "header_class": "dh-5",
        "projects": [
            {"code": "C1", "name": "Green DISCO", "type": "direct"},
            {"code": "C2", "name": "AMI lessons learned", "type": "support"},
            {"code": "C3", "name": "Buy REN@DISCO", "type": "direct"},
            {
                "code": "C4",
                "name": "Advanced smart meter analytics",
                "type": "direct",
            },
            {
                "code": "C5",
                "name": "Interactive energy applications",
                "type": "direct",
            },
        ],
    },
]

BENEFITS = [
    {"code": "B1", "title": "Deferred grid investment"},
    {"code": "B2", "title": "Avoided grid investment"},
    {"code": "B3", "title": "Reduced electricity losses"},
    {"code": "B4", "title": "Reduced planned outages"},
    {"code": "B5", "title": "Reduced unplanned outages"},
    {"code": "B6", "title": "Improved customer satisfaction"},
    {"code": "B7", "title": "Reduced CO₂ emissions"},
    {"code": "B8", "title": "Improved organizational efficiency"},
    {"code": "B9", "title": "EV integration benefits"},
]

# 4. State Management
if "selected_project" not in st.session_state:
    st.session_state.selected_project = "Dashboard Home"

if "active_horizon" not in st.session_state:
    st.session_state.active_horizon = "short"


def select_project(code):
    st.session_state.selected_project = code


def set_horizon(horizon):
    st.session_state.active_horizon = horizon


# 5. Sidebar
with st.sidebar:
    display_safe_image("images/giz_logo")
    st.title("⚡ EEHC GIS Control")
    st.markdown("**Egyptian Electricity Holding Company**")
    st.divider()

    if st.button(
        "🏠 Roadmap Dashboard",
        use_container_width=True,
        type=(
            "primary"
            if st.session_state.selected_project == "Dashboard Home"
            else "secondary"
        ),
    ):
        select_project("Dashboard Home")
        st.rerun()

    st.subheader("Quick Navigation")
    for domain in DOMAINS:
        with st.expander(domain["title"]):
            for proj in domain["projects"]:
                prefix = "🟢 " if proj.get("active") else ""
                if st.button(
                    f"{prefix}{proj['code']}: {proj['name'][:20]}...",
                    key=f"sb_{proj['code']}",
                    use_container_width=True,
                ):
                    select_project(proj["code"])
                    st.rerun()

# 6. Main Routing Logic
if st.session_state.selected_project == "Dashboard Home":

    st.markdown(
        """
        <div class="top-banner">
            <h1>Smart Grid Roadmap</h1>
            <p>5 domains • 26 projects • 9 potential benefits | EEHC and Egypt's nine DISCOs</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    cols = st.columns(5)
    for idx, domain in enumerate(DOMAINS):
        with cols[idx]:
            st.markdown(
                f'<div class="domain-header {domain["header_class"]}">{domain["title"]}</div>',
                unsafe_allow_html=True,
            )
            st.caption(f"📌 {domain['count']}")

            for proj in domain["projects"]:
                is_active = proj.get("active", False)
                icon = "🔵" if proj["type"] == "direct" else "⭕"

                if is_active:
                    st.markdown(
                        '<div class="gis-highlight">', unsafe_allow_html=True
                    )
                    st.markdown(
                        f"<span style='color:#2563EB; font-size:0.7rem; font-weight:800; float:right;'>{proj['tag']}</span>",
                        unsafe_allow_html=True,
                    )
                    if st.button(
                        f"{icon} **{proj['code']}** - {proj['name']}",
                        key=f"rm_{proj['code']}",
                        use_container_width=True,
                        type="primary",
                    ):
                        select_project(proj["code"])
                        st.rerun()
                    st.markdown("</div>", unsafe_allow_html=True)
                else:
                    if st.button(
                        f"{icon} **{proj['code']}** - {proj['name']}",
                        key=f"rm_{proj['code']}",
                        use_container_width=True,
                    ):
                        select_project(proj["code"])
                        st.rerun()

    st.markdown("---")
    st.subheader("Potential Benefits of the Smart-Grid Portfolio")

    b_cols = st.columns(9)
    for i, benefit in enumerate(BENEFITS):
        with b_cols[i]:
            st.markdown(
                f"""
                <div class="benefit-card">
                    <div class="benefit-code">{benefit['code']}</div>
                    <div class="benefit-title">{benefit['title']}</div>
                </div>
            """,
                unsafe_allow_html=True,
            )

    st.caption(
        "🔴 **⭕ 12 Support Projects** enable delivery | 🔵 **14 Direct Projects** deliver assessed benefits"
    )

elif st.session_state.selected_project == "IF2":

    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )

    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%); padding: 24px; border-radius: 12px; color: white; margin-top: 10px;">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">INFRASTRUCTURE DOMAIN (IF2)</span>
            <h1 style="color: white !important; margin-top: 8px;">Asset Management Design & Implementation (GIS Rollout)</h1>
            <p style="color: #BFDBFE; margin: 0;">EEHC and the Nine Distribution Companies (DISCOs)</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.write("")

    t1, t2, t3, t4 = st.tabs([
        "📌 Executive Overview",
        "🗺️ Delivery Roadmap",
        "🏛️ DISCO Readiness Routes",
        "📊 Monitoring & Apps",
    ])

    # TAB 1: EXECUTIVE OVERVIEW
    with t1:
        st.subheader("Strategic Objectives")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            * **Unified Network Record:** Nine DISCOs operating on one common standard model[cite: 1].
            * **Trusted Network Data:** Verified geographic locations and stable asset identities[cite: 1].
            """)
        with c2:
            st.markdown("""
            * **Continuous Updates:** Workflow covering field capture ➔ verify ➔ approve ➔ publish[cite: 1].
            * **Sector Applications:** Powering asset management, operations, OMS, and grid planning[cite: 1].
            """)

        st.write("")
        col_space_l, col_img_center, col_space_r = st.columns([1, 2, 1])
        with col_img_center:
            display_safe_image(
                "images/01_Strategic_objectives_Asset_record",
                caption="Strategic Objectives Schema & Asset Record Workflow",
                width=550,
            )

    # TAB 2: DELIVERY ROADMAP
    with t2:
        st.subheader("Delivery Roadmap Horizons")
        st.write(
            "Click a horizon icon below to view its specific milestones, deliverables, and architecture visual artifacts:"
        )

        h_col1, h_col2, h_col3 = st.columns(3)
        with h_col1:
            is_active = st.session_state.active_horizon == "short"
            if st.button(
                "🔴 **SHORT TERM**\n\nJan 2026 – Jun 2027",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ):
                set_horizon("short")
                st.rerun()

        with h_col2:
            is_active = st.session_state.active_horizon == "medium"
            if st.button(
                "🟡 **MEDIUM TERM**\n\nJun 2027 – May 2030",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ):
                set_horizon("medium")
                st.rerun()

        with h_col3:
            is_active = st.session_state.active_horizon == "long"
            if st.button(
                "🟢 **LONG TERM**\n\nMay 2030 Onward",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ):
                set_horizon("long")
                st.rerun()

        st.markdown("---")

        if st.session_state.active_horizon == "short":
            st.markdown(
                """
                <div class="horizon-box">
                    <h3 style="margin:0; color:#1E293B;">Short Term: Network Record & Continuous Updates</h3>
                    <p style="margin:0; color:#64748B;">Jan 2026 – Jun 2027 | Priority: Central Foundation, 9 DISCO Pilots & Full Medium Voltage (MV) Coverage</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("##### 1. Established Central GIS Foundation")
                st.markdown("""
                * **Platform Upgrade:** Upgraded Enterprise & ArcGIS Pro installed at EEHC data center[cite: 1].
                * **SQL Link:** Direct SQL–GIS connection with common asset IDs and symbology[cite: 1].
                * **Proof of Connection:** Smouha pilot completed with 7-person trained R&D team[cite: 1].
                """)
                display_safe_image(
                    "images/02_Established_central_GIS_foundation",
                    caption="Smouha Proof of Connection Interface",
                )
                st.markdown(
                    '<div class="image-caption-card">Verified location & kiosk attributes (ALX-MAC-10-K0475) in Smouha[cite: 1].</div>',
                    unsafe_allow_html=True,
                )

            with col2:
                st.markdown("##### 2. MV Network Drawing & Acceptance")
                st.markdown("""
                * **Delivery Method:** Smouha method ➔ 1 pilot per DISCO ➔ Full MV network[cite: 1].
                * **Target Date:** June 2027[cite: 1].
                * **Outcome:** Accepted MV components with verified coordinates & connectivity[cite: 1].
                """)
                display_safe_image(
                    "images/03_MV_network_drawing_and_acceptance",
                    caption="MV Component Placement & Connectivity Drawing",
                )
                st.markdown(
                    '<div class="image-caption-card">Medium Voltage network tracing and component verification map[cite: 1].</div>',
                    unsafe_allow_html=True,
                )

            st.write("")
            col3, col4 = st.columns(2)
            with col3:
                st.markdown(
                    "##### 3. Continuous Updates & Monitoring Dashboard"
                )
                st.markdown("""
                * **Workflow:** Field Change ➔ Verify ➔ Approve ➔ Publish in SQL/GIS[cite: 1].
                * **Monitoring:** Executive dashboards showing accepted coverage, exceptions, and backlog[cite: 1].
                """)
                display_safe_image(
                    "images/04_Continuous_updates_and_rollout_monitoring",
                    caption="GIS Rollout Executive Dashboard",
                )
                st.markdown(
                    '<div class="image-caption-card">Tracking MV Coverage, Data Quality, Update Backlog, and Synchronization[cite: 1].</div>',
                    unsafe_allow_html=True,
                )

            with col4:
                st.markdown("##### 4. Alexandria Region Integrated Output")
                st.markdown("""
                * **Integrated Grid Example:** Located components, connected MV feeders, and shared asset IDs across DISCOs[cite: 1].
                """)
                display_safe_image(
                    "images/05_Expected_short_term_network_record",
                    caption="Alexandria Network Record Overview",
                )
                st.markdown(
                    '<div class="image-caption-card">Integrated MV network record output for Alexandria Distribution Region[cite: 1].</div>',
                    unsafe_allow_html=True,
                )

        elif st.session_state.active_horizon == "medium":
            st.markdown(
                """
                <div class="horizon-box" style="border-left-color: #D97706;">
                    <h3 style="margin:0; color:#1E293B;">Medium Term: Coverage Extension & Operating Applications</h3>
                    <p style="margin:0; color:#64748B;">Jun 2027 – May 2030 | Focus: LV Coverage, OMS, Asset Maintenance, Fleet Routing & RE/PQ Pilots</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

            m_col1, m_col2 = st.columns(2)
            with m_col1:
                st.markdown("##### 1. Low Voltage (LV) Network Mapping")
                st.markdown(
                    "Extend accepted MV records down to all LV components and customer service links[cite: 1]."
                )
                display_safe_image(
                    "images/06_LV_network_expansion",
                    caption="LV Pillar & Service Box Mapping",
                )

                st.markdown("##### 2. Asset Management & Condition Status")
                st.markdown(
                    "Link mapped components to condition status, inspection logs, and SQL work orders[cite: 1]."
                )
                display_safe_image(
                    "images/07_Asset_Management_and_Maintenance",
                    caption="Transformer Condition & Risk Inspection",
                )

                st.markdown(
                    "##### 3. Loss Analysis & Energy Cost Visibility"
                )
                st.markdown(
                    "Compare energy across feeder, transformer, and customer boundaries to locate losses[cite: 1]."
                )
                display_safe_image(
                    "images/10_Loss_Analysis_and_Energy_Cost_Visibility",
                    caption="Energy Imbalance & Loss Boundary Map",
                )

            with m_col2:
                st.markdown("##### 4. Workforce & Fleet Dispatch")
                st.markdown(
                    "Route maintenance crews dynamically against network outage points[cite: 1]."
                )
                display_safe_image(
                    "images/08_Fleet_and_Field_Workforce_Management",
                    caption="Workforce Routing & Incident Tasks",
                )

                st.markdown("##### 5. Outage Management System (OMS)")
                st.markdown(
                    "Link customer incidents to affected grid feeder areas for faster restoration[cite: 1]."
                )
                display_safe_image(
                    "images/09_Outage_Management_System",
                    caption="OMS Incident Isolation & Feeder Tracing",
                )

                st.markdown(
                    "##### 6. Renewable Energy (PV) & BESS Screening"
                )
                st.markdown(
                    "Screen PV/EV connection headroom and evaluate Battery Storage (BESS) locations[cite: 1]."
                )
                display_safe_image(
                    "images/11_Renewable_Energy_and_EV_Connection_Planning",
                    caption="Renewable Capacity Headroom",
                )
                display_safe_image(
                    "images/13_Battery_Energy_Storage_for_Grid_Support",
                    caption="BESS Location Screening",
                )

        elif st.session_state.active_horizon == "long":
            st.markdown(
                """
                <div class="horizon-box" style="border-left-color: #16A34A;">
                    <h3 style="margin:0; color:#1E293B;">Long Term: Coordinated & Automated Network Operations</h3>
                    <p style="margin:0; color:#64748B;">May 2030 Onward | Focus: ADMS, Automated Restoration, Peak Management & Full AMI Integration</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

            l_col1, l_col2 = st.columns(2)
            with l_col1:
                st.markdown("##### 1. ADMS & Restoration Automation")
                st.markdown(
                    "Use maintained GIS topology inside Advanced Distribution Management Systems for automated switching[cite: 1]."
                )
                display_safe_image(
                    "images/14_ADMS_and_Restoration_Automation",
                    caption="Automated Fault Isolation & Restoration Pathway",
                )

                st.markdown("##### 2. Voltage Optimization & Peak Demand")
                st.markdown(
                    "Study volt/VAR control options across distribution feeders[cite: 1]."
                )
                display_safe_image(
                    "images/15_Voltage_Optimization_and_Peak_Management",
                    caption="Voltage Profile & Reactive Power Monitoring",
                )

            with l_col2:
                st.markdown(
                    "##### 3. Full AMI & Smart Meter Integration"
                )
                st.markdown(
                    "Link all smart meters precisely to their supply transformer and feeder[cite: 1]."
                )
                display_safe_image(
                    "images/16_Advanced_Metering_Infrastructure_Integration",
                    caption="Meter-to-Transformer Spatial Topology",
                )

    # TAB 3: DISCO READINESS ROUTES
    with t3:
        st.subheader("Three Integration Routes for DISCOs")
        st.markdown("""
        1. **Established GIS:** Map IDs and schema, retain local tools, synchronize approved updates to SQL[cite: 1].
        2. **Partial / Fragmented GIS:** Consolidate existing work, fill survey gaps, supply equipment and training[cite: 1].
        3. **No GIS:** Survey components from scratch, build local team capacity, utilize central platform[cite: 1].
        """)

    # TAB 4: MONITORING & APPS
    with t4:
        st.subheader("Continuous Update & Monitoring Workflow")
        st.info(
            "Field change ➔ DISCO Verification ➔ Joint Acceptance QA Checklist ➔ Publish in SQL/GIS[cite: 1]"
        )

else:
    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )
    code = st.session_state.selected_project
    proj_name = "Selected Project"
    for domain in DOMAINS:
        for p in domain["projects"]:
            if p["code"] == code:
                proj_name = p["name"]

    st.markdown(
        '<div class="project-workspace-container">', unsafe_allow_html=True
    )
    st.title(f"📌 {code}: {proj_name}")
    st.info(f"Workspace reserved for project `{code}`.")
    st.markdown("</div>", unsafe_allow_html=True)
