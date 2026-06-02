import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

# 1. Page Configuration
st.set_page_config(page_title="IP Telemetry Dashboard", page_icon="🌐", layout="wide")

# 2. Custom CSS Injection for a Premium UI Design
st.markdown("""
    <style>
        /* Main background and font styling */
        .stApp {
            background-color: #0f172a;
            color: #f8fafc;
        }
        
        /* Main Header Styling */
        .main-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #38bdf8;
            margin-bottom: 5px;
            letter-spacing: -1px;
        }
        .subtitle {
            color: #94a3b8;
            font-size: 1rem;
            margin-bottom: 30px;
        }
        
        /* Modern Card Containers for Telemetry Data */
        .telemetry-card {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 16px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }
        .telemetry-card:hover {
            transform: translateY(-2px);
            border-color: #38bdf8;
        }
        
        /* Card Text Properties */
        .card-label {
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #64748b;
            margin-bottom: 6px;
            font-weight: 600;
        }
        .card-value {
            font-size: 1.25rem;
            font-weight: 600;
            color: #e2e8f0;
        }
        
        /* Section Subheaders */
        .section-header {
            font-size: 1.25rem;
            font-weight: 600;
            color: #f8fafc;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Render Header UI Elements
st.markdown('<div class="main-title">🌐 IP Geolocation</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Real-time network lookup, server profiling, and visual coordinate tracking.</div>', unsafe_allow_html=True)

# 4. Fetch User Geolocation Data from API
@st.cache_data
def fetch_geolocation():
    try:
        # API automatically captures the public IP address of the sender
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        return data if data.get("status") == "success" else None
    except Exception as e:
        print(f"Network Request Error: {e}")
        return None

geo_data = fetch_geolocation()

# Helper function to generate standardized HTML cards easily
def render_card(label, value, accent_color="#38bdf8"):
    return f"""
    <div class="telemetry-card" style="border-left: 4px solid {accent_color};">
        <div class="card-label">{label}</div>
        <div class="card-value">{value}</div>
    </div>
    """

if geo_data:
    # Split the dashboard UI layout grid into two columns (Ratio 2:3)
    col1, col2 = st.columns([2, 3])

    # Left Column: Network Diagnostics Info
    with col1:
        st.markdown('<div class="section-header">📊 Network Intelligence</div>', unsafe_allow_html=True)
        
        st.markdown(render_card("IP Address", geo_data["query"], "#38bdf8"), unsafe_allow_html=True)
        st.markdown(render_card("Physical Location", f"{geo_data['city']}, {geo_data['regionName']}, {geo_data['countryCode']}", "#a855f7"), unsafe_allow_html=True)
        st.markdown(render_card("Internet Provider (ISP)", geo_data["isp"], "#22c55e"), unsafe_allow_html=True)
        st.markdown(render_card("System Timezone", geo_data["timezone"], "#eab308"), unsafe_allow_html=True)
        st.markdown(render_card("Coordinates", f"{geo_data['lat']}°, {geo_data['lon']}°", "#ec4899"), unsafe_allow_html=True)

    # Right Column: Visual Mapping Component
    with col2:
        st.markdown('<div class="section-header">🗺️ Live Geospatial Vector Map</div>', unsafe_allow_html=True)
        
        # Instantiate a clean, standard bright OpenStreetMap canvas
        interactive_map = folium.Map(
            location=[geo_data["lat"], geo_data["lon"]], 
            zoom_start=13, 
            tiles="OpenStreetMap",
            zoom_control=True
        )
        
        # Add a custom pop-up marker corresponding to the coordinates
        folium.Marker(
            [geo_data["lat"], geo_data["lon"]],
            popup=f"<div style='font-family:sans-serif; color:#0f172a;'><b>Location:</b> {geo_data['city']}<br><b>ISP:</b> {geo_data['isp']}</div>",
            tooltip="Detected Node Pointer",
            icon=folium.Icon(color="blue", icon="globe", prefix="fa")
        ).add_to(interactive_map)
        
        # Display the finalized interactive map structure
        st_folium(interactive_map, width="100%", height=530)

else:
    st.error("Telemetry Error: Unable to establish an API handshake. Please check your data connection.")