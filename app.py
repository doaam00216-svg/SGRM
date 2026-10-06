import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="EEHC Smart Grid Roadmap Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #F8FAFC;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    .top-banner {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border-radius: 16px;
        padding: 24px 32px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
    }
    .top-banner h1 {
        color: #FFFFFF !important;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
    }
    .top-banner p {
        color: #94A3B8;
        font-size: 1.05rem;
        margin-top: 6px;
        margin-bottom: 0;
    }
    .domain-header {
        border-radius: 12px 12px 0 0;
        padding: 12px 14px;
        color: white;
        font-weight: 700;
        font-size: 0.85rem;
        text-transform: uppercase;
    }
    .dh-1 { background: #DC2626; }
    .dh-2 { background: #0284C7; }
    .dh-3 { background: #D97706; }
    .dh-4 { background: #B91C1C; }
    .dh-5 { background: #15803D; }

    .benefit-card {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 12px 14px;
        margin-bottom: 10px;
    }
    .benefit-code {
        font-weight: 800;
        font-size: 1rem;
        color: #D9381E;
    }
    .benefit-title {
        font-size: 0.85rem;
        color: #334155;
        font-weight: 600;
    }
    .gis-highlight {
        background: #EFF6FF;
        border: 2px solid #2563EB !important;
        border-radius: 8px;
        padding: 4px;
        margin-bottom: 8px;
    }
    .horizon-header {
        background: white;
        border-left: 6px solid #2563EB;
        padding: 16px 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        margin-bottom: 20px;
    }
    .image-caption-card {
        background: #F1F5F9;
        border-radius: 8px;
        padding: 10px 14px;
        margin-top: 8px;
        font-size: 0.85rem;
        color: #475569;
        border-left: 3px solid #0EA5E9;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Roadmap Data
DOMAINS = [
    {
        "id": 1,
        "title": "1. POLICY AND REGULATORY SUPPORT",
        "count": "4 PROJECTS",
        "header_class": "dh-1",
        "projects": [
            {"code": "PS1", "name": "Policy and regulatory review", "type": "support"},
            {"code": "PS2", "name": "Technical standards and regulation", "type": "support"},
            {"code": "PS3", "name": "Privacy and customer data ownership", "type": "support"},
            {"code": "PS4", "name": "Cybersecurity", "type": "support"}
        ]
    },
    {
        "id": 2,
        "title": "2. ORGANIZATIONAL SUPPORT",
        "count": "4 PROJECTS",
        "header_class": "dh-2",
        "projects": [
            {"code": "OS1", "name": "Business goals and use cases", "type": "support"},
            {"code": "OS2", "name": "Organizational KPIs", "type": "support"},
            {"code": "OS3", "name": "Asset management strategy", "type": "support"},
            {"code": "OS4", "name": "Smart grid governance", "type": "support"}
        ]
    },
    {
        "id": 3,
        "title": "3. INFRASTRUCTURE",
        "count": "6 PROJECTS",
        "header_class": "dh-3",
        "projects": [
            {"code": "IF1", "name": "Smart meters: commercial and industrial", "type": "direct"},
            {"code": "IF2", "name": "Asset management design and implementation", "type": "support", "active": True, "tag": "Includes GIS"},
            {"code": "IF3", "name": "Smart meters: residential >200 kWh/month", "type": "direct"},
            {"code": "IF4", "name": "Asset management and monitoring", "type": "direct"},
            {"code": "IF5", "name": "Smart Meter Plus: residential <200 kWh/month", "type": "direct"},
            {"code": "IF6", "name": "Phasor measurement units", "type": "direct"}
        ]
    },
    {
        "id": 4,
        "title": "4. TECHNOLOGY",
        "count": "7 PROJECTS",
        "header_class": "dh-4",
        "projects": [
            {"code": "TE1", "name": "Technology evaluation and selection", "type": "support"},
            {"code": "TE2", "name": "Integrated solution selection", "type": "support"},
            {"code": "TE3", "name": "Smart meter analytics", "type": "direct"},
            {"code": "TE4", "name": "PV and EV monitoring", "type": "direct"},
            {"code": "TE5", "name": "Demand response", "type": "direct"},
            {"code": "TE6", "name": "Demand-side management pilot", "type": "direct"},
            {"code": "TE7", "name": "Energy storage pilots", "type": "direct"}
        ]
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
            {"code": "C4", "name": "Advanced smart meter analytics", "type": "direct"},
            {"code": "C5", "name": "Interactive energy applications", "type": "direct"}
        ]
    }
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
    {"code": "B9", "title": "EV integration benefits"}
]

# State Management
if 'selected_project' not in st.session_state:
    st.session_state.selected_project = "Dashboard Home"

def select_project(code):
    st.session_state.selected_project = code

# Sidebar
with st.sidebar:
    st.title("⚡ EEHC GIS Control")
    st.markdown("**Egyptian Electricity Holding Company**")
    st.divider()

    if st.button("🏠 Roadmap Dashboard", use_container_width=True, type="primary" if st.session_state.selected_project == "Dashboard Home" else "secondary"):
        select_project("Dashboard Home")
        st.rerun()

    st.subheader("Quick Project Selector")
    for domain in DOMAINS:
        with st.expander(domain["title"]):
            for proj in domain["projects"]:
                prefix = "🟢 " if proj.get("active") else ""
                if st.button(f"{prefix}{proj['code']}: {proj['name'][:20]}...", key=f"sb_{proj['code']}", use_container_width=True):
                    select_project(proj['code'])
                    st.rerun()

# 6. Main Dashboard
if st.session_state.selected_project == "Dashboard Home":

    st.markdown("""
        <div class="top-banner">
            <h1>Smart Grid Roadmap</h1>
            <p>5 domains • 26 projects • 9 potential benefits | EEHC and Egypt's nine DISCOs</p>
        </div>
    """, unsafe_allow_html=True)

    cols = st.columns(5)
    for idx, domain in enumerate(DOMAINS):
        with cols[idx]:
            st.markdown(f'<div class="domain-header {domain["header_class"]}">{domain["title"]}</div>', unsafe_allow_html=True)
            st.caption(f"📌 {domain['count']}")

            for proj in domain["projects"]:
                is_active = proj.get("active", False)
                icon = "🔵" if proj["type"] == "direct" else "⭕"
                
                if is_active:
                    st.markdown('<div class="gis-highlight">', unsafe_allow_html=True)
                    st.markdown(f"<span style='color:#2563EB; font-size:0.7rem; font-weight:800; float:right;'>{proj['tag']}</span>", unsafe_allow_html=True)
                    if st.button(f"{icon} **{proj['code']}** - {proj['name']}", key=f"rm_{proj['code']}", use_container_width=True, type="primary"):
                        select_project(proj['code'])
                        st.rerun()
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    if st.button(f"{icon} **{proj['code']}** - {proj['name']}", key=f"rm_{proj['code']}", use_container_width=True):
                        select_project(proj['code'])
                        st.rerun()

    st.markdown("---")
    st.subheader("Potential Benefits of the Smart-Grid Portfolio")
    
    b_cols = st.columns(9)
    for i, benefit in enumerate(BENEFITS):
        with b_cols[i]:
            st.markdown(f"""
                <div class="benefit-card">
                    <div class="benefit-code">{benefit['code']}</div>
                    <div class="benefit-title">{benefit['title']}</div>
                </div>
            """, unsafe_allow_html=True)

    st.caption("🔴 **⭕ 12 Support Projects** enable delivery | 🔵 **14 Direct Projects** deliver assessed benefits")

# 7. GIS Project View (IF2) with Short, Medium, and Long Term Details & Visuals
elif st.session_state.selected_project == "IF2":
    
    st.button("← Back to Roadmap Dashboard", on_click=select_project, args=("Dashboard Home",))
    
    st.markdown("""
        <div style="background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%); padding: 24px; border-radius: 12px; color: white; margin-top: 10px;">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">INFRASTRUCTURE DOMAIN (IF2)</span>
            <h1 style="color: white !important; margin-top: 8px;">Asset Management Design & Implementation (GIS Rollout)</h1>
            <p style="color: #BFDBFE; margin: 0;">EEHC and the Nine Distribution Companies (DISCOs)</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Horizon Navigation Tabs
    tab_short, tab_med, tab_long, tab_arch = st.tabs([
        "🔴 Short Term (Jan 2026 – Jun 2027)", 
        "🟡 Medium Term (Jun 2027 – May 2030)", 
        "🟢 Long Term (May 2030 Onward)",
        "🏛️ Architecture & Governance"
    ])

    # --- TAB 1: SHORT TERM ---
    with tab_short:
        st.markdown("""
            <div class="horizon-header">
                <h3 style="margin:0; color:#1E293B;">Short Term: Network Record & Updates</h3>
                <p style="margin:0; color:#64748B;">Target: January 2026 – June 2027 | Priority: Full Medium Voltage (MV) Network Coverage</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("#### Key Short-Term Milestones & Visual Artifacts")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### 1. Established Central GIS Foundation")
            st.markdown("""
            * **Platform Upgrade:** Upgraded Enterprise & ArcGIS Pro installed at EEHC data center.
            * **SQL Link:** Direct SQL–GIS connection with common asset IDs and symbology.
            * **Proof of Connection:** Smouha pilot completed with 7-person trained R&D team.
            """)
            st.image("https://raw.githubusercontent.com/GIS-Assets/GIS-Media/main/smouha_proof.jpg", caption="Smouha Proof of Connection Interface", use_container_width=True)
            st.markdown('<div class="image-caption-card">Verified location & kiosk attributes (ALX-MAC-10-K0475) in Smouha[cite: 1].</div>', unsafe_allow_html=True)

        with col2:
            st.markdown("##### 2. MV Network Drawing & Acceptance")
            st.markdown("""
            * **Delivery Method:** Smouha method ➔ 1 pilot per DISCO ➔ Full MV network[cite: 1].
            * **Target Date:** June 2027[cite: 1].
            * **Outcome:** Accepted MV components with verified coordinates & connectivity[cite: 1].
            """)
            st.image("https://raw.githubusercontent.com/GIS-Assets/GIS-Media/main/mv_drawing.jpg", caption="MV Component Placement & Connectivity Drawing", use_container_width=True)
            st.markdown('<div class="image-caption-card">Medium Voltage network tracing and component verification map[cite: 1].</div>', unsafe_allow_html=True)

        st.divider()

        col3, col4 = st.columns(2)
        with col3:
            st.markdown("##### 3. Continuous Updates & Dashboard Monitoring")
            st.markdown("""
            * **Workflow:** Field Change ➔ Verify ➔ Approve ➔ Publish in SQL/GIS[cite: 1].
            * **Monitoring:** Executive dashboards showing accepted coverage, exceptions, and backlog[cite: 1].
            """)
            st.image("https://raw.githubusercontent.com/GIS-Assets/GIS-Media/main/gis_monitoring.jpg", caption="GIS Rollout Executive Dashboard", use_container_width=True)
            st.markdown('<div class="image-caption-card">Tracking MV Coverage, Data Quality, Update Backlog, and Synchronization[cite: 1].</div>', unsafe_allow_html=True)

        with col4:
            st.markdown("##### 4. Expected Short-Term Output Network")
            st.markdown("""
            * **Alexandria Grid Example:** Located components, connected MV feeders, and shared asset IDs across DISCOs[cite: 1].
            """)
            st.image("https://raw.githubusercontent.com/GIS-Assets/GIS-Media/main/alexandria_grid.jpg", caption="Alexandria Network Record Overview", use_container_width=True)
            st.markdown('<div class="image-caption-card">Integrated MV network record output for Alexandria Distribution Region[cite: 1].</div>', unsafe_allow_html=True)

    # --- TAB 2: MEDIUM TERM ---
    with tab_med:
        st.markdown("""
            <div class="horizon-header" style="border-left-color: #D97706;">
                <h3 style="margin:0; color:#1E293B;">Medium Term: Coverage & Operating Applications</h3>
                <p style="margin:0; color:#64748B;">Target: June 2027 – May 2030 | Focus: LV Coverage, OMS, Asset Maintenance & RE/PQ Pilots</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("#### Operational Applications Deployment")

        m_col1, m_col2 = st.columns(2)
        with m_col1:
            st.markdown("##### 1. Low Voltage (LV) Network Expansion")
            st.markdown("Extend accepted MV records down to all LV components and customer service links[cite: 1].")
            st.image("https://raw.githubusercontent.com/GIS-Assets/GIS-Media/main/lv_expansion.jpg", caption="LV Pillar & Box Mapping", use_container_width=True)

            st.markdown("##### 2. Asset Management & Risk Maintenance")
            st.markdown("Link mapped components to condition status, maintenance history, and SQL work orders[cite: 1].")
            st.image("https://raw.githubusercontent.com/GIS-Assets/GIS-Media/main/asset_management.jpg", caption="Transformer Condition & Inspection Data", use_container_width=True)

            st.markdown("##### 3. Loss Analysis & Energy Cost Visibility")
            st.markdown("Compare energy across feeder, transformer, and customer boundaries to locate losses[cite: 1].")
            st.image("https://raw.githubusercontent.com/GIS-Assets/GIS-Media/main/loss_analysis.jpg", caption="Energy Imbalance & Loss Boundary Map", use_container_width=True)

        with m_col2:
            st.markdown("##### 4. Fleet & Field Workforce Management")
            st.markdown("Route maintenance crews dynamically against network outage points[cite: 1].")
            st.image("https://raw.githubusercontent.com/GIS-Assets/GIS-Media/main/fleet_management.jpg", caption="Workforce Routing & Task Status", use_container_width=True)

            st.markdown("##### 5. Outage Management System (OMS)")
            st.markdown("Link customer incidents to affected grid feeder areas for faster restoration[cite: 1].")
            st.image("https://raw.githubusercontent.com/GIS-Assets/GIS-Media/main/oms_outage.jpg", caption="OMS Incident & Affected Feeder Isolation", use_container_width=True)

            st.markdown("##### 6. Renewable Energy & Battery Screening")
            st.markdown("Screen PV/EV connection headroom and evaluate Battery Storage (BESS) locations[cite: 1].")
            st.image("https://raw.githubusercontent.com/GIS-Assets/GIS-Media/main/pv_bess.jpg", caption="Renewable Capacity Headroom & BESS Screening", use_container_width=True)

    # --- TAB 3: LONG TERM ---
    with tab_long:
        st.markdown("""
            <div class="horizon-header" style="border-left-color: #16A34A;">
                <h3 style="margin:0; color:#1E293B;">Long Term: Coordinated Network Operations</h3>
                <p style="margin:0; color:#64748B;">Target: May 2030 Onward | Focus: ADMS, Automation, Peak Management & AMI</p>
            </div>
        """, unsafe_allow_html=True)

        l_col1, l_col2 = st.columns(2)
        with l_col1:
            st.markdown("##### 1. ADMS & Restoration Automation")
            st.markdown("Use maintained GIS topology inside Advanced Distribution Management Systems for automated switching[cite: 1].")
            st.image("https://raw.githubusercontent.com/GIS-Assets/GIS-Media/main/adms_restoration.jpg", caption="Automated Fault Isolation & Restoration Pathway", use_container_width=True)

            st.markdown("##### 2. Voltage Optimization & Peak Demand")
            st.markdown("Study volt/VAR control options across distribution feeders[cite: 1].")
            st.image("https://raw.githubusercontent.com/GIS-Assets/GIS-Media/main/voltage_control.jpg", caption="Voltage Profile & Reactive Power Monitoring", use_container_width=True)

        with l_col2:
            st.markdown("##### 3. Full AMI & Smart Meter Integration")
            st.markdown("Link all smart meters precisely to their supply transformer and feeder[cite: 1].")
            st.image("https://raw.githubusercontent.com/GIS-Assets/GIS-Media/main/ami_integration.jpg", caption="Meter-to-Transformer Spatial Topology", use_container_width=True)

    # --- TAB 4: ARCHITECTURE & GOVERNANCE ---
    with tab_arch:
        st.subheader("Joint Delivery Team & Sector Governance")
        st.markdown("""
        * **EEHC GIS & R&D Team:** Common model, SQL integration, publication and support[cite: 1].
        * **DISCO Control Teams:** Locate components, verify connections, own field updates[cite: 1].
        * **Joint Acceptance Team:** Check coordinates, attributes, and network relationships[cite: 1].
        """)

# 8. Reserved View for Other Projects
else:
    st.button("← Back to Roadmap Dashboard", on_click=select_project, args=("Dashboard Home",))
    
    code = st.session_state.selected_project
    proj_name = "Selected Project"
    for domain in DOMAINS:
        for p in domain["projects"]:
            if p["code"] == code:
                proj_name = p["name"]

    st.title(f"📌 {code}: {proj_name}")
    st.info("Workspace reserved for project development.")
