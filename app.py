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


# Helper function to find existing file regardless of single/double extensions
def find_existing_image(base_path):
    if os.path.exists(base_path):
        return base_path

    folder, filename = os.path.split(base_path)
    clean_name = filename.split(".")[0]

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


# Helper function to render image centered with standard 550px width
def display_centered_image(file_path, caption="", width=550):
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        display_safe_image(file_path, caption=caption, width=width)


# Base64 background assets
giz_b64 = get_base64_image("images/giz_logo")
eehc_b64 = get_base64_image("images/bg_eehc_banner")
skyline_b64 = get_base64_image("images/bg_city_skyline")
asset_rec_b64 = get_base64_image(
    "images/01_Strategic_objectives_Asset_record"
)

# 2. Custom CSS Styles
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: #F8FAFC !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }}
    /* Fixed GIZ logo in bottom-right corner */
    .stApp::after {{
        content: "";
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 180px;
        height: 90px;
        background-image: url('data:image/png;base64,{giz_b64}');
        background-repeat: no-repeat;
        background-position: bottom right;
        background-size: contain;
        opacity: 0.25;
        pointer-events: none;
        z-index: 0;
    }}
    /* Main Roadmap Top Banner - Clearer Image Overlay */
    .roadmap-banner {{
        background: linear-gradient(135deg, rgba(15,23,42,0.30) 0%, rgba(30,41,59,0.30) 100%), 
                    url('data:image/png;base64,{eehc_b64}');
        background-repeat: no-repeat;
        background-position: center right;
        background-size: cover;
        border-radius: 16px;
        padding: 28px 32px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
    }}
    .roadmap-banner h1 {{
        color: #FFFFFF !important;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.6);
    }}
    .roadmap-banner p {{
        color: #FFFFFF !important;
        font-size: 1.05rem;
        font-weight: 700;
        margin-top: 6px;
        margin-bottom: 0;
        text-shadow: 0 1px 3px rgba(0,0,0,0.7);
    }}
    /* Project Header Banner */
    .project-banner {{
        background: linear-gradient(135deg, rgba(15,23,42,0.40) 0%, rgba(30,41,59,0.40) 100%), 
                    url('data:image/png;base64,{skyline_b64}');
        background-repeat: no-repeat;
        background-position: center right;
        background-size: cover;
        border-radius: 12px;
        padding: 24px 32px;
        color: white;
        margin-top: 10px;
        margin-bottom: 20px;
        box-shadow: 0 8px 20px -4px rgba(37, 99, 235, 0.25);
    }}
    .project-banner h1 {{
        color: #FFFFFF !important;
        margin-top: 8px;
        margin-bottom: 4px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.6);
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

    /* Supported Projects Layout Matching Reference Image */
    .sp-wrapper {{
        position: relative;
        margin-top: 10px;
        margin-bottom: 20px;
    }}
    .sp-header-badge {{
        display: inline-flex;
        align-items: center;
        border: 2px solid #881337;
        color: #881337;
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 6px 18px;
        font-weight: 800;
        font-size: 0.85rem;
        letter-spacing: 0.5px;
        margin-bottom: 12px;
    }}
    .sp-card-body {{
        position: relative;
        border-left: 4px solid #1E3A8A;
        background-color: #F8FAFC;
        border-radius: 0 20px 20px 0;
        padding: 24px 28px;
        margin-left: 10px;
    }}
    .sp-row {{
        display: flex;
        align-items: center;
        margin-bottom: 16px;
    }}
    .sp-row:last-child {{
        margin-bottom: 0;
    }}
    .sp-arrow {{
        color: #B91C1C;
        font-size: 1.4rem;
        font-weight: 900;
        margin-right: 14px;
    }}
    .sp-pill {{
        background-color: #FFE4E6;
        color: #0F172A;
        border-radius: 10px;
        padding: 8px 18px;
        font-size: 0.95rem;
        font-weight: 700;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }}
    </style>
""",
    unsafe_allow_html=True,
)


# Fixed helper function to properly render HTML with unsafe_allow_html=True
def render_supported_projects_card(supported_list):
    rows_html = "".join([
        f'<div class="sp-row"><span class="sp-arrow">➔</span><span class="sp-pill">{item}</span></div>'
        for item in supported_list
    ])
    full_html = f"""
    <div class="sp-wrapper">
        <div class="sp-header-badge">🎯 SUPPORTED PROJECTS</div>
        <div class="sp-card-body">
            {rows_html}
        </div>
    </div>
    """
    st.markdown(full_html, unsafe_allow_html=True)


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


def select_project(code):
    st.session_state.selected_project = code


# 5. Sidebar Navigation
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
        <div class="roadmap-banner">
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
                icon = "🔵" if proj["type"] == "direct" else "⭕"
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

elif st.session_state.selected_project == "IF1":
    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )

    st.markdown(
        """
        <div class="project-banner">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">INFRASTRUCTURE DOMAIN (IF1)</span>
            <h1>Smart Meters: Commercial and Industrial / Rollout Projects</h1>
        </div>
    """,
        unsafe_allow_html=True,
    )

    if1_tab1, if1_tab2, if1_tab3 = st.tabs([
        "📊 250,000 Smart-Meter Pilot",
        "📈 270,000-Meter Expansion",
        "⚡ 410,000 Three-Phase Meters",
    ])

    with if1_tab1:
        st.subheader("250,000 Smart-Meter Pilot")
        render_supported_projects_card([
            "C2: AMI Lessons Learned",
            "TE2: Integrated Solution Selection",
        ])

    with if1_tab2:
        st.subheader("270,000-Meter Expansion")
        render_supported_projects_card([
            "TE3: Smart Meter Analytics (Loss Analytics)"
        ])

    with if1_tab3:
        st.subheader("410,000 Three-Phase Meters")
        render_supported_projects_card([
            "TE2: Integrated Solution Selection",
            "TE3: Smart Meter Analytics",
        ])

elif st.session_state.selected_project == "IF2":
    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )

    st.markdown(
        """
        <div class="project-banner">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">INFRASTRUCTURE DOMAIN (IF2)</span>
            <h1>Asset Management Design & Implementation (GIS Rollout)</h1>
            <p style="color: #E2E8F0; margin: 0;">EEHC and the Nine Distribution Companies (DISCOs)</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    t1, t2, t3, t4 = st.tabs([
        "📌 Executive Overview",
        "🗺️ Delivery Roadmap",
        "🏛️ DISCO Readiness Routes",
        "📊 Monitoring & Apps",
    ])

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
        display_centered_image(
            "images/01_Strategic_objectives_Asset_record",
            caption="Strategic Objectives Schema & Asset Record Workflow",
            width=550,
        )

    with t2:
        st.subheader("Delivery Roadmap Horizon")
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

        with col4:
            st.markdown("##### 4. Alexandria Region Integrated Output")
            st.markdown("""
            * **Integrated Grid Example:** Located components, connected MV feeders, and shared asset IDs across DISCOs[cite: 1].
            """)
            display_safe_image(
                "images/05_Expected_short_term_network_record",
                caption="Alexandria Network Record Overview",
            )

    with t3:
        st.subheader("Three Integration Routes for DISCOs")
        st.markdown("""
        1. **Established GIS:** Map IDs and schema, retain local tools, synchronize approved updates to SQL[cite: 1].
        2. **Partial / Fragmented GIS:** Consolidate existing work, fill survey gaps, supply equipment and training[cite: 1].
        3. **No GIS:** Survey components from scratch, build local team capacity, utilize central platform[cite: 1].
        """)

    with t4:
        st.subheader("Continuous Update & Monitoring Workflow")
        st.info(
            "Field change ➔ DISCO Verification ➔ Joint Acceptance QA Checklist ➔ Publish in SQL/GIS"
        )

elif st.session_state.selected_project == "IF3":
    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )
    st.markdown(
        """
        <div class="project-banner">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">INFRASTRUCTURE DOMAIN (IF3)</span>
            <h1>Smart Meters: Residential >200 kWh/month</h1>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.subheader("280,000 Single-Phase Meters")
    render_supported_projects_card(["TE2: Integrated Solution Selection"])

elif st.session_state.selected_project == "IF4":
    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )
    st.markdown(
        """
        <div class="project-banner">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">INFRASTRUCTURE DOMAIN (IF4)</span>
            <h1>Asset Management and Monitoring</h1>
        </div>
    """,
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### 1. Low Voltage (LV) Network Mapping")
        st.markdown(
            "Extend accepted MV records down to all LV components and customer service links."
        )
        display_safe_image(
            "images/06_LV_network_expansion",
            caption="LV Pillar & Service Box Mapping",
        )
    with col2:
        st.markdown("##### 2. Asset Management and Maintenance")
        st.markdown(
            "Link mapped components to condition status, inspection logs, and SQL work orders."
        )
        display_safe_image(
            "images/07_Asset_Management_and_Maintenance",
            caption="Transformer Condition & Risk Inspection",
        )

elif st.session_state.selected_project == "TE1":
    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )
    st.markdown(
        """
        <div class="project-banner">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">TECHNOLOGY DOMAIN (TE1)</span>
            <h1>Technology Evaluation and Selection</h1>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.subheader("Innovation Hub")
    render_supported_projects_card([
        "PS2: Technical Standards and Regulation",
        "TE2: Integrated Solution Selection",
    ])

elif st.session_state.selected_project == "TE2":
    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )
    st.markdown(
        """
        <div class="project-banner">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">TECHNOLOGY DOMAIN (TE2)</span>
            <h1>Integrated Solution Selection</h1>
        </div>
    """,
        unsafe_allow_html=True,
    )

    te2_tab1, te2_tab2, te2_tab3 = st.tabs([
        "⚡ ADMS & OMS Integration",
        "📡 Unified Head-End System",
        "🏢 Distribution Control Centres (DCC)",
    ])

    with te2_tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### ADMS and Restoration Automation")
            st.markdown(
                "Use maintained GIS topology inside Advanced Distribution Management Systems for automated switching."
            )
            display_safe_image(
                "images/14_ADMS_and_Restoration_Automation",
                caption="Automated Fault Isolation & Restoration Pathway",
            )
        with col2:
            st.markdown("##### Outage Management System (OMS)")
            st.markdown(
                "Link customer incidents to affected grid feeder areas for faster restoration."
            )
            display_safe_image(
                "images/09_Outage_Management_System",
                caption="OMS Incident Isolation & Feeder Tracing",
            )

    with te2_tab2:
        st.subheader("Unified Head-End System")
        st.markdown(
            "Standardized multi-vendor meter communication interface across all DISCOs."
        )
        render_supported_projects_card([
            "PS3: Privacy and Customer Data Ownership",
            "PS4: Cybersecurity",
        ])

    with te2_tab3:
        st.subheader("Distribution Control Centres (DCC)")
        render_supported_projects_card([
            "IF2: Asset Management Design and Implementation",
            "PS4: Cybersecurity",
            "IF4: Asset Management and Monitoring",
            "OS4: Smart Grid Governance",
        ])

        st.markdown("""
        * **Purpose & Scope:** Coordinated network operation across DCCs[cite: 4].
        * **Progress & Milestone:** Seven listed DCCs completed[cite: 4]. Advance remaining packages[cite: 4].
        * **Sector Value:** Service continuity[cite: 4]. Measure restoration performance[cite: 4].
        * **Resources & Decision:** Operators, communications, and integration[cite: 4]. Confirm next-stage readiness[cite: 4].
        """)

        st.markdown("##### DCC Delivery Stages Table")
        st.markdown("""
        | Stage | Regional Locations & Status[cite: 4] |
        | :--- | :--- |
        | **Completed** | Nasr City, El Mansoura, Dokki, 6 October[cite: 4] |
        | **Construction / Procurement** | Sharm El Sheikh (Construction), Helmeya (Construction), El Minia (Contracting), Ismailia & New Cities, Supervisory (Tendering)[cite: 4] |
        | **Phase 3 Feasibility** | 26 July, Beheira, East Alexandria, South Delta (after Minia signing), North & South El Sharkia, West Alexandria, Bani Suef, Damietta, Luxor & Aswan, Sohag[cite: 4] |
        """)
        
        st.write("")
        display_centered_image(
            "images/08_Fleet_and_Field_Workforce_Management",
            caption="DCC Coordinated Network Operation Model",
            width=550,
        )

elif st.session_state.selected_project == "TE3":
    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )
    st.markdown(
        """
        <div class="project-banner">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">TECHNOLOGY DOMAIN (TE3)</span>
            <h1>Smart Meter Analytics</h1>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown("##### Loss Analysis and Energy Cost Visibility")
    st.markdown(
        "Compare energy across feeder, transformer, and customer boundaries to locate losses."
    )
    display_centered_image(
        "images/10_Loss_Analysis_and_Energy_Cost_Visibility",
        caption="Energy Imbalance & Loss Boundary Map",
        width=550,
    )

elif st.session_state.selected_project == "TE4":
    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )
    st.markdown(
        """
        <div class="project-banner">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">TECHNOLOGY DOMAIN (TE4)</span>
            <h1>PV and EV Monitoring</h1>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(
        "##### Renewable Energy (PV) & Battery Energy Storage (BESS)"
    )
    c1, c2 = st.columns(2)
    with c1:
        display_safe_image(
            "images/11_Renewable_Energy_and_EV_Connection_Planning",
            caption="Renewable Energy and EV Connection Planning",
        )
    with c2:
        display_safe_image(
            "images/13_Battery_Energy_Storage_for_Grid_Support",
            caption="Battery Energy Storage for Grid Support",
        )

elif st.session_state.selected_project == "TE5":
    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )
    st.markdown(
        """
        <div class="project-banner">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">TECHNOLOGY DOMAIN (TE5)</span>
            <h1>Demand Response</h1>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown("##### Voltage Optimization and Peak Management")
    st.markdown(
        "Study volt/VAR control options across distribution feeders."
    )
    display_centered_image(
        "images/15_Voltage_Optimization_and_Peak_Management",
        caption="Voltage Profile & Reactive Power Monitoring",
        width=550,
    )

elif st.session_state.selected_project == "TE6":
    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )
    st.markdown(
        """
        <div class="project-banner">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">TECHNOLOGY DOMAIN (TE6)</span>
            <h1>Demand-Side Management Pilot</h1>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.subheader("Siwa Microgrid Assessment and Smart Design")
    render_supported_projects_card([
        "TE1: Technology Evaluation and Selection",
        "TE7: Energy Storage Pilots",
    ])

elif st.session_state.selected_project == "TE7":
    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )
    st.markdown(
        """
        <div class="project-banner">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">TECHNOLOGY DOMAIN (TE7)</span>
            <h1>Energy Storage Pilots</h1>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.subheader("BESS Assessment for a Weak Seasonal Network")
    render_supported_projects_card([
        "TE1: Technology Evaluation and Selection",
        "PS2: Technical Standards and Regulation",
    ])

    st.markdown("""
    * **Purpose & Scope:** Assess storage for seasonal weak-network stability[cite: 4].
    * **Progress & Next Milestone:** Assessment initiative[cite: 4]. Validate studies and compare options[cite: 4].
    * **Sector Value:** A justified investment based on measured needs[cite: 4].
    * **Resources & Decision:** Feeder data and specialist teams[cite: 4]. Agree on study scope[cite: 4].
    """)
    display_centered_image(
        "images/13_Battery_Energy_Storage_for_Grid_Support",
        caption="BESS Candidate Site & Voltage Support Screening Concept",
        width=550,
    )

elif st.session_state.selected_project == "PS2":
    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )
    st.markdown(
        """
        <div class="project-banner">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">POLICY & REGULATORY DOMAIN (PS2)</span>
            <h1>Technical Standards and Regulation</h1>
        </div>
    """,
        unsafe_allow_html=True,
    )

    ps2_tab1, ps2_tab2 = st.tabs([
        "📜 Unified OBIS Code",
        "⚖️ Distribution Code Update",
    ])

    with ps2_tab1:
        st.subheader("Unified OBIS Code")
        render_supported_projects_card([
            "TE2: Integrated Solution Selection",
            "IF4: Asset Management and Monitoring",
        ])

    with ps2_tab2:
        st.subheader("Distribution Code Update")
        render_supported_projects_card(["PS1: Policy and Regulatory Review"])

elif st.session_state.selected_project == "OS2":
    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )
    st.markdown(
        """
        <div class="project-banner">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">ORGANIZATIONAL SUPPORT DOMAIN (OS2)</span>
            <h1>Organizational KPIs</h1>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown("##### Fleet and Field Workforce Management")
    st.markdown(
        "Route maintenance crews dynamically against network outage points."
    )
    display_centered_image(
        "images/08_Fleet_and_Field_Workforce_Management",
        caption="Workforce Routing & Incident Tasks",
        width=550,
    )

elif st.session_state.selected_project == "OS4":
    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )
    st.markdown(
        """
        <div class="project-banner">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">ORGANIZATIONAL SUPPORT DOMAIN (OS4)</span>
            <h1>Smart Grid Governance</h1>
        </div>
    """,
        unsafe_allow_html=True,
    )

    os4_tab1, os4_tab2 = st.tabs([
        "🎓 Smart Grid Training Course",
        "✈️ BESS Study Tour & Capacity Building",
    ])

    with os4_tab1:
        st.subheader("Smart Grid Training Course")
        render_supported_projects_card(["Cross-Cutting Technical Capability"])

    with os4_tab2:
        st.subheader("BESS Capacity Building and Germany Study Tour")
        render_supported_projects_card([
            "TE7: Energy Storage Pilots",
            "TE1: Technology Evaluation and Selection",
            "IF4: Asset Management and Monitoring",
        ])

elif st.session_state.selected_project == "C2":
    st.button(
        "← Back to Roadmap Dashboard",
        on_click=select_project,
        args=("Dashboard Home",),
    )
    st.markdown(
        """
        <div class="project-banner">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">CUSTOMER ENGAGEMENT DOMAIN (C2)</span>
            <h1>AMI Lessons Learned</h1>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.subheader("Advanced Metering Infrastructure (AMI)")
    render_supported_projects_card(["C4: Advanced Smart Meter Analytics"])
    st.markdown(
        "Link all smart meters precisely to their supply transformer and feeder topology."
    )
    display_centered_image(
        "images/16_Advanced_Metering_Infrastructure_Integration",
        caption="Meter-to-Transformer Spatial Topology",
        width=550,
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
        f"""
        <div class="project-banner">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">PROJECT WORKSPACE ({code})</span>
            <h1>{proj_name}</h1>
            <p style="color: #E2E8F0; margin: 0;">Egyptian Electricity Holding Company Smart Grid Implementation</p>
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.info(f"Workspace reserved for project `{code}`.")
