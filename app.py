import streamlit as st

st.title("EEHC GIS Rollout Strategy")

# Define tabs for the rollout timeline
tab_short, tab_medium, tab_long = st.tabs([
    "Short-Term (Jan 2026 – Jun 2027)", 
    "Medium-Term (Jun 2027 – May 2030)", 
    "Long-Term (May 2030+)"
])

# GitHub raw URL prefix (Replace with your actual GitHub username and repository)
GITHUB_BASE_URL = "https://raw.githubusercontent.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPOSITORY_NAME>/main/"

# ==========================================
# 1. SHORT-TERM TAB
# ==========================================
with tab_short:
    st.header("Short-Term: Central GIS Foundation & Network Records")
    
    st.subheader("1. Asset Record Concept Map")
    st.image(
        GITHUB_BASE_URL + "01_asset_record.png", 
        caption="Red medium-voltage grid topology map with asset attribute records", 
        use_container_width=True
    )
    
    st.subheader("2. Smouha GIS Web Interface")
    st.image(
        GITHUB_BASE_URL + "02_smouha_web_gis.png", 
        caption="OpenStreetMap vector view showing kiosk asset details on Victor Emmanuel III St.", 
        use_container_width=True
    )
    
    st.subheader("3. MV Network Drawing & Acceptance Map")
    st.image(
        GITHUB_BASE_URL + "03_mv_network_drawing.png", 
        caption="GIS mapping canvas with MV network nodes along Mohamed Abu El Fetouh Hassab St.", 
        use_container_width=True
    )
    
    st.subheader("4. GIS Rollout Monitoring Dashboard")
    st.image(
        GITHUB_BASE_URL + "04_rollout_monitoring.png", 
        caption="City-wide feeder acceptance tracking across Capture, Verify, Approve, and Publish stages", 
        use_container_width=True
    )
    
    st.subheader("5. Alexandria Regional Distribution Network Map")
    st.image(
        GITHUB_BASE_URL + "05_alexandria_network_map.png", 
        caption="Overview of Alexandria's regional electricity distribution network (منطقة الإسكندرية)", 
        use_container_width=True
    )

# ==========================================
# 2. MEDIUM-TERM TAB
# ==========================================
with tab_medium:
    st.header("Medium-Term: Coverage & Operating Applications")
    
    st.subheader("6. Low-Voltage Network Expansion (Wall Boxes)")
    st.image(
        GITHUB_BASE_URL + "06_lv_network_wallboxes.png", 
        caption="Street-level mapping of LV wall distribution boxes along Qanal El Mahmoudeya St.", 
        use_container_width=True
    )
    
    st.subheader("7. Asset Management & Maintenance Interface")
    st.image(
        GITHUB_BASE_URL + "07_asset_management_transformer.png", 
        caption="Interactive GIS view of transformer asset parameters (ELMACO 800 KVA)", 
        use_container_width=True
    )
    
    st.subheader("8. Fleet & Field Workforce Management")
    st.image(
        GITHUB_BASE_URL + "08_field_workforce_fleet.png", 
        caption="Real-time field vehicle dispatching and work location routing", 
        use_container_width=True
    )
    
    st.subheader("9. Outage Management System (OMS)")
    st.image(
        GITHUB_BASE_URL + "09_outage_management.png", 
        caption="Fault trace schematic isolating impacted customer areas and feeder switches", 
        use_container_width=True
    )
    
    st.subheader("10. Loss Analysis & Energy Cost Visibility")
    st.image(
        GITHUB_BASE_URL + "10_loss_analysis.png", 
        caption="Metered boundary zones and transformer imbalance investigation areas", 
        use_container_width=True
    )
    
    st.subheader("11. Renewable & EV Connection Screening")
    st.image(
        GITHUB_BASE_URL + "11_renewable_connection_screening.png", 
        caption="Coastal grid headroom map highlighting constrained vs available capacity", 
        use_container_width=True
    )
    
    st.subheader("12. Power Quality Assessment & Response")
    st.image(
        GITHUB_BASE_URL + "12_power_quality_assessment.png", 
        caption="Feeder trace monitoring for voltage events, unbalance, and harmonics", 
        use_container_width=True
    )
    
    st.subheader("13. Battery Energy Storage System (BESS) Support")
    st.image(
        GITHUB_BASE_URL + "13_bess_grid_support.png", 
        caption="Candidate battery storage siting along constrained distribution feeders", 
        use_container_width=True
    )

# ==========================================
# 3. LONG-TERM TAB
# ==========================================
with tab_long:
    st.header("Long-Term: Coordinated Network Operations")
    
    st.subheader("14. ADMS & Restoration Automation")
    st.image(
        GITHUB_BASE_URL + "14_adms_restoration_automation.png", 
        caption="Automated fault section isolation and switching restoration paths", 
        use_container_width=True
    )
    
    st.subheader("15. Voltage Optimization & Peak Management")
    st.image(
        GITHUB_BASE_URL + "15_voltage_optimization.png", 
        caption="Grid control assets, real-time voltage profiles, and demand trace curves", 
        use_container_width=True
    )
    
    st.subheader("16. Advanced Metering Infrastructure (AMI) Integration")
    st.image(
        GITHUB_BASE_URL + "16_ami_integration.png", 
        caption="Smart meter link mapping, outage indications, and load profile analytics", 
        use_container_width=True
    )
