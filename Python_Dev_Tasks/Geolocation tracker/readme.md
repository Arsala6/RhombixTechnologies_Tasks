# 📍 Advanced IP Geolocation Dashboard

A sleek, real-time web application built with Python that fetches a user's public IP address, extracts advanced network intelligence parameters, and displays the exact location on a bright, interactive geographic map.

---

## ✨ Features

* **Automatic IP Extraction:** Seamlessly identifies the client's public IP address upon launching the application.
* **Comprehensive Telemetry Data:** Extracts IP address, physical location (City, State, Country), Internet Service Provider (ISP), exact coordinate parameters, and system timezone.
* **Premium Glassmorphic Dashboard UI:** Designed using custom dark-slate themed modern HTML/CSS injection with dynamic hover states.
* **Interactive Spatial Mapping:** Features a bright, colorful, high-contrast OpenStreetMap integration with custom markers and tooltip details.
* **Data Caching Layer:** Leverages memory caching to ensure optimized performance and safe execution under API request constraints.

---

## 🛠️ Tech Stack & Dependencies

The project relies completely on a modern Python micro-framework environment:

* **[Streamlit](https://streamlit.io/):** For rendering the interactive web UI dashboard.
* **[Folium](https://python-visualization.github.io/folium/):** For generating the responsive geographic map engine.
* **[Streamlit-Folium](https://github.com/randyzwitch/streamlit-folium):** The bridge component to render Folium vector objects inside Streamlit layouts.
* **[Requests](https://requests.readthedocs.io/):** For executing safe HTTP handshakes with the remote IP-API telemetry endpoint.

---

## 🚀 Getting Started

Follow these step-by-step instructions to get the application up and running on your local machine.

### 1. Prerequisites
Make sure you have Python 3.8 or higher installed on your computer.

### 2. Install Project Requirements
Open your terminal or command prompt inside your project directory and run the following command to install the required libraries:

```bash
pip install streamlit requests streamlit-folium folium