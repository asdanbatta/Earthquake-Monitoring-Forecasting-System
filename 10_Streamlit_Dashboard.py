import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Earthquake Monitoring & Forecasting System",
    page_icon="🌍",
    layout="wide"
)

# =====================================
# TITLE
# =====================================

st.title("🌍 Earthquake Monitoring & Forecasting System")

st.markdown("""
Welcome to the **Earthquake Monitoring & Forecasting Dashboard**.

This dashboard combines:

- 🌍 Earthquake Monitoring
- 📈 Time Series Forecasting
- 🌎 Regional Forecasting
- 🤖 AI Risk Classification
- 📊 Seismological Analysis
- 🗺️ GIS Mapping
""")

st.divider()

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select a Page",
    [
        "🏠 Home",
        "📄 Processed Data",
        "🌎 Regional Forecast",
        "📈 Multi-Region Forecast"
    ],
    key="navigation"
)

# =====================================
# HOME PAGE
# =====================================

if page == "🏠 Home":

    st.header("🏠 Dashboard Home")

    try:

        earthquakes = pd.read_csv(
            "data/processed/earthquakes_processed.csv"
        )

        forecast = pd.read_csv(
            "outputs/forecasts/multi_region_forecast.csv"
        )

        st.success("✅ Data Loaded Successfully")

        # Dashboard Summary

        total_earthquakes = len(earthquakes)
        total_locations = earthquakes["Location"].nunique()
        average_magnitude = earthquakes["Magnitude"].mean()
        average_depth = earthquakes["Depth_km"].mean()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "🌍 Total Earthquakes",
            f"{total_earthquakes:,}"
        )

        col2.metric(
            "📍 Locations",
            total_locations
        )

        col3.metric(
            "⭐ Avg Magnitude",
            f"{average_magnitude:.2f}"
        )

        col4.metric(
            "⬇️ Avg Depth (km)",
            f"{average_depth:.2f}"
        )

        st.divider()

        # Magnitude Chart

        st.subheader("📈 Earthquake Magnitude Distribution")

        fig, ax = plt.subplots(figsize=(10,5))

        ax.hist(
            earthquakes["Magnitude"],
            bins=20,
            edgecolor="black"
        )

        ax.set_xlabel("Magnitude")
        ax.set_ylabel("Number of Earthquakes")

        st.pyplot(fig)

        st.divider()

        # Depth Chart

        st.subheader("🌍 Earthquake Depth Distribution")

        fig, ax = plt.subplots(figsize=(10,5))

        ax.hist(
            earthquakes["Depth_km"],
            bins=20,
            color="orange",
            edgecolor="black"
        )

        ax.set_xlabel("Depth (km)")
        ax.set_ylabel("Number of Earthquakes")

        st.pyplot(fig)

        st.divider()

        # Top Locations

        st.subheader("🌎 Top 10 Earthquake Locations")

        top_locations = earthquakes["Location"].value_counts().head(10)

        st.bar_chart(top_locations)

        st.divider()

        # Map

        st.subheader("🗺️ Earthquake Map")

        map_data = earthquakes[
            ["Latitude","Longitude"]
        ].rename(
            columns={
                "Latitude":"lat",
                "Longitude":"lon"
            }
        )

        st.map(map_data)

    except Exception as e:

        st.error(e)
        # =====================================
# PROCESSED DATA PAGE
# =====================================

elif page == "📄 Processed Data":

    st.header("📄 Processed Earthquake Dataset")

    try:

        earthquakes = pd.read_csv(
            "data/processed/earthquakes_processed.csv"
        )

        st.success("✅ Dataset Loaded Successfully")

        st.write(f"Total Records: {len(earthquakes):,}")

        st.dataframe(
            earthquakes,
            use_container_width=True
        )

        st.download_button(
            label="📥 Download Processed Dataset",
            data=earthquakes.to_csv(index=False),
            file_name="earthquakes_processed.csv",
            mime="text/csv"
        )

    except Exception as e:

        st.error(e)


# =====================================
# REGIONAL FORECAST PAGE
# =====================================

elif page == "🌎 Regional Forecast":

    st.header("🌎 Regional Forecast")

    try:

        forecast = pd.read_csv(
            "outputs/forecasts/multi_region_forecast.csv"
        )

        st.success("✅ Forecast Loaded Successfully")

        st.dataframe(
            forecast,
            use_container_width=True
        )

        st.download_button(
            label="📥 Download Forecast",
            data=forecast.to_csv(index=False),
            file_name="regional_forecast.csv",
            mime="text/csv"
        )

    except Exception as e:

        st.error(e)


# =====================================
# MULTI-REGION FORECAST PAGE
# =====================================

elif page == "📈 Multi-Region Forecast":

    st.header("📈 Multi-Region Forecast")

    try:

        forecast = pd.read_csv(
            "outputs/forecasts/multi_region_forecast.csv"
        )

        st.subheader("Forecast Table")

        st.dataframe(
            forecast,
            use_container_width=True
        )

        st.subheader("Forecast Comparison")

        st.bar_chart(
            forecast.set_index("Region")["Forecast_30_Days"]
        )

        st.subheader("Forecast Statistics")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Regions",
            len(forecast)
        )

        col2.metric(
            "Highest Forecast",
            int(forecast["Forecast_30_Days"].max())
        )

        col3.metric(
            "Average Forecast",
            f"{forecast['Forecast_30_Days'].mean():.1f}"
        )

    except Exception as e:

        st.error(e)
        # =====================================
# SIDEBAR INFORMATION
# =====================================

st.sidebar.divider()

st.sidebar.markdown("## 📊 Dashboard Information")

st.sidebar.info(
    """
Earthquake Monitoring & Forecasting System

Version: 1.0
"""
)

st.sidebar.markdown("---")

st.sidebar.markdown("### Project Modules")

st.sidebar.markdown("""
- ✅ Data Collection
- ✅ Data Cleaning
- ✅ GIS Mapping
- ✅ Seismological Analysis
- ✅ Machine Learning
- ✅ Time Series Forecasting
- ✅ AI Risk Prediction
- ✅ Regional Forecasting
- ✅ Streamlit Dashboard
""")

# =====================================
# FOOTER
# =====================================

st.divider()

st.caption(
    """
🌍 Earthquake Monitoring & Forecasting System

Developed using Python, Pandas, Matplotlib and Streamlit.

This dashboard integrates:

• Earthquake Monitoring
• GIS Mapping
• Machine Learning
• AI Risk Prediction
• Time-Series Forecasting
• Regional Forecasting

© 2026
"""
)