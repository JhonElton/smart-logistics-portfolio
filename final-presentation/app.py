import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="Smart Logistics Portfolio", page_icon="🚚", layout="wide")

# 2. Inject Premium, Ultra-Clean Enterprise CSS
st.markdown("""
    <style>
        /* Modern Soft Background */
        .stApp {
            background-color: #f8fafc;
        }
        
        /* Custom Title & Subtitle Styling */
        .main-title { font-family: 'Inter', sans-serif; font-weight: 800; color: #0f172a; font-size: 2.5rem; margin-bottom: 0.2rem; }
        .sub-title { font-family: 'Inter', sans-serif; color: #475569; font-size: 1.1rem; margin-bottom: 1.8rem; font-weight: 400; }
        
        /* Premium Floating KPI Cards Styling */
        div[data-testid="stMetric"] {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            padding: 1.5rem;
            border-radius: 16px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        div[data-testid="stMetric"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
            border-color: #cbd5e1;
        }
        div[data-testid="stMetricLabel"] { color: #64748b !important; font-size: 0.9rem !important; font-weight: 600 !important; text-transform: uppercase; letter-spacing: 0.05em; }
        div[data-testid="stMetricValue"] { color: #0f172a !important; font-size: 2.2rem !important; font-weight: 800 !important; }
        
        /* Section Subheaders */
        .section-header {
            font-family: 'Inter', sans-serif;
            color: #1e293b;
            font-size: 1.3rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Clean Dashboard Header
st.markdown('<div class="main-title">🚚 Fleet Command Center</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Smart Logistics Intelligence Showcase — Final Internship Deliverable</div>', unsafe_allow_html=True)

# 4. Load Data & Compute Analytics 
@st.cache_data
def load_fleet_data():
    data = {
        "Driver ID": ["DRV-001", "DRV-002", "DRV-003", "DRV-004", "DRV-005"],
        "Driver Name": ["Driver A", "Driver B", "Driver C", "Driver D", "Driver E"],
        "Avg Speed (km/h)": [82, 58, 94, 65, 71],
        "Actual Delivery (mins)": [30, 45, 22, 38, 41],
        "Scheduled Time (mins)": [35, 40, 30, 35, 45],
        "Hard Braking Events": [4, 0, 7, 1, 2]
    }
    df = pd.DataFrame(data)
    # Lock down numeric formatting perfectly
    df["Efficiency Score (%)"] = np.minimum((df["Scheduled Time (mins)"] / df["Actual Delivery (mins)"]) * 100, 100).round(1)
    df["Risk Profile"] = df.apply(lambda row: "High Risk" if row["Avg Speed (km/h)"] > 75 or row["Hard Braking Events"] >= 3 else "Normal", axis=1)
    return df

df = load_fleet_data()

# 5. KPI Metrics Section
col1, col2, col3 = st.columns(3)
with col1:
    avg_speed = round(df["Avg Speed (km/h)"].mean(), 1)
    st.metric(label="Fleet Avg Velocity", value=f"{avg_speed} km/h")
with col2:
    avg_eff = round(df["Efficiency Score (%)"].mean(), 1)
    st.metric(label="Operational Efficiency", value=f"{avg_eff}%")
with col3:
    high_risk_count = int((df["Risk Profile"] == "High Risk").sum())
    st.metric(label="Active Risk Alerts", value=str(high_risk_count))

st.markdown("<br><br>", unsafe_allow_html=True)

# 6. Main Content Area (Layout split)
left_col, right_col = st.columns([1.1, 0.9], gap="large")

with left_col:
    st.markdown('<div class="section-header">📋 Telematics Registry & Safety Audits</div>', unsafe_allow_html=True)
    
    # Elegant Dataframe highlighting rules
    def style_risk(val):
        if val == "High Risk":
            return 'background-color: #fef2f2; color: #dc2626; font-weight: bold; border-radius: 4px;'
        elif val == "Normal":
            return 'background-color: #f0fdf4; color: #16a34a; border-radius: 4px;'
        return ''
        
    # Format the dynamic display
    styled_df = df.style.format({
        "Efficiency Score (%)": "{:.1f}%"
    }).map(style_risk, subset=["Risk Profile"])
    
    st.dataframe(styled_df, use_container_width=True, hide_index=True)

with right_col:
    st.markdown('<div class="section-header">📈 Driver Speed Profiling</div>', unsafe_allow_html=True)
    
    # Display minimalist native Streamlit Bar Chart
    chart_data = df.set_index("Driver Name")[["Avg Speed (km/h)"]]
    st.bar_chart(chart_data, color="#2563eb")
    
    st.caption("🔒 Safety Alert Context: Standard risk threshold limitations mapped at 75 km/h.")