import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="EEHC Smart Grid Roadmap Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS Styles
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
    .horizon-box {
        background: white;
        border-left: 6px solid #2563EB;
        padding: 18px 24px;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
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

# 4. State Management
if 'selected_project' not in st.session_state:
    st.session_state.selected_project = "Dashboard Home"

if 'active_horizon' not in st.session_state:
    st.session_state.active_horizon = "short"

def select_project(code):
    st.session_state.selected_project = code

def set_horizon(horizon):
    st.session_state.active_horizon = horizon

# 5. Sidebar
with st.sidebar:
    st.title("⚡ EEHC GIS Control")
    st.markdown("**Egyptian Electricity Holding Company**")
    st.divider()

    if st.button("🏠 Roadmap Dashboard", use_container_width=True, type="primary" if st.session_state.selected_project == "Dashboard Home" else "secondary"):
        select_project("Dashboard Home")
        st.rerun()

    st.subheader("Quick Navigation")
    for domain in DOMAINS:
        with st.expander(domain["title"]):
            for proj in domain["projects"]:
                prefix = "🟢 " if proj.get("active") else ""
                if st.button(f"{prefix}{proj['code']}: {proj['name'][:20]}...", key=f"sb_{proj['code']}", use_container_width=True):
                    select_project(proj['code'])
                    st.rerun()

# 6. Main Roadmap Dashboard
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
            st.markdown(f'<div class="domain-header {domain["header_class"]}">{domain
