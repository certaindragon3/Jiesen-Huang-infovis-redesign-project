import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import requests
from io import StringIO
import numpy as np
from PIL import Image
import os
import geopandas as gpd
import tempfile
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Set page config
st.set_page_config(
    page_title="NYC Heat Vulnerability Index",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #F5F5F5;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1, h2, h3 {
        color: #2C3E50;
    }
    .highlight {
        background-color: #FFF3CD;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .stat-box {
        background-color: white;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        text-align: center;
    }
    .legend-title {
        font-weight: bold;
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("NYC Heat Vulnerability Index Visualization")
st.markdown("""
    This interactive map shows heat vulnerability across NYC zip codes. Areas in red indicate higher vulnerability 
    to extreme heat events, which can have serious health impacts for residents, especially vulnerable populations.
""")

# Load data
@st.cache_data
def load_data():
    try:
        # Try to read the CSV file directly
        try:
            df = pd.read_csv('Heat_Vulnerability_Index_Rankings_20250406.csv')
        except FileNotFoundError:
            # If file is not found in the current directory, try with a path
            st.warning("CSV file not found in current directory, trying with a direct path...")
            # The CSV might be uploaded differently depending on the deployment environment
            import os
            possible_paths = [
                './Heat_Vulnerability_Index_Rankings_20250406.csv',
                '../Heat_Vulnerability_Index_Rankings_20250406.csv',
                '/app/Heat_Vulnerability_Index_Rankings_20250406.csv'
            ]
            
            df = None
            for path in possible_paths:
                if os.path.exists(path):
                    df = pd.read_csv(path)
                    break
            
            if df is None:
                # If still not found, create dummy data for demonstration
                st.error("Could not find the CSV file. Using sample data for demonstration.")
                return pd.DataFrame({
                    'zipcode': [10001, 10002, 10003, 10004, 10005, 10006, 
                                10007, 10009, 10010, 10011, 10012, 10013],
                    'hvi': [5, 3, 2, 4, 1, 5, 2, 3, 4, 5, 1, 2]
                })
        
        # Rename columns to more readable names if needed
        if 'ZIP Code Tabulation Area (ZCTA) 2020' in df.columns and 'Heat Vulnerability Index (HVI)' in df.columns:
            df = df.rename(columns={
                'ZIP Code Tabulation Area (ZCTA) 2020': 'zipcode',
                'Heat Vulnerability Index (HVI)': 'hvi'
            })
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        # Create sample data for demonstration
        return pd.DataFrame({
            'zipcode': [10001, 10002, 10003, 10004, 10005, 10006, 
                        10007, 10009, 10010, 10011, 10012, 10013],
            'hvi': [5, 3, 2, 4, 1, 5, 2, 3, 4, 5, 1, 2]
        })

# Load NYC GeoJSON
@st.cache_data
def load_nyc_geojson():
    """
    Load NYC GeoJSON from local file.
    """
    try:
        with open('GeoJSON.json', 'r') as f:
            geojson_data = json.load(f)
        return geojson_data
    except Exception as e:
        st.error(f"Failed to load local GeoJSON file: {e}")
        return None

# Load data
df = load_data()
nyc_geojson = load_nyc_geojson()

# Convert zipcode to string if it's numeric
if 'zipcode' in df.columns and pd.api.types.is_numeric_dtype(df['zipcode']):
    df['zipcode'] = df['zipcode'].astype(str)

# Sidebar
st.sidebar.header("Visualization Controls")

# Filter by vulnerability level
vulnerability_filter = st.sidebar.slider(
    "Filter by Vulnerability Index Range",
    int(df['hvi'].min() if 'hvi' in df.columns else 1),
    int(df['hvi'].max() if 'hvi' in df.columns else 5),
    (int(df['hvi'].min() if 'hvi' in df.columns else 1), int(df['hvi'].max() if 'hvi' in df.columns else 5))
)

# Apply filter
filtered_df = df[(df['hvi'] >= vulnerability_filter[0]) & (df['hvi'] <= vulnerability_filter[1])]

# Visualization type
viz_type = st.sidebar.radio(
    "Visualization Type",
    ["Choropleth Map", "Heat Map"]
)

# Color scale selection
color_scale = st.sidebar.selectbox(
    "Color Scale",
    ["Reds", "RdYlGn_r", "Oranges", "YlOrRd", "inferno"]
)

# Display statistics
st.sidebar.header("Heat Vulnerability Statistics")
if 'hvi' in df.columns:
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.markdown(
            f"""<div class="stat-box">
                <h3>{int(df['hvi'].max())}</h3>
                <p>Highest HVI</p>
            </div>""", 
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            f"""<div class="stat-box">
                <h3>{len(df[df['hvi'] >= 4])}</h3>
                <p>High Risk Zip</p>
            </div>""", 
            unsafe_allow_html=True
        )

# Information about heat vulnerability
st.sidebar.markdown("<br>", unsafe_allow_html=True)
with st.sidebar.expander("What is Heat Vulnerability?"):
    st.markdown("""
        Heat vulnerability measures a community's risk from extreme heat events. Factors include:
        - Percentage of vulnerable populations (elderly, children)
        - Access to air conditioning
        - Presence of green spaces
        - Building density and materials
        - Socioeconomic factors
        
        Higher values indicate areas that need more resources during heat events.
    """)

# Main content area - Map section (full width)
if viz_type == "Choropleth Map" and nyc_geojson is not None:
    # Create choropleth map
    try:
        # First attempt with standard property keys
        feature_id_key = "properties.ZCTA5CE10"
        # Check if we need to use a different property key based on the GeoJSON structure
        if nyc_geojson and 'features' in nyc_geojson and len(nyc_geojson['features']) > 0:
            first_feature = nyc_geojson['features'][0]
            if 'properties' in first_feature:
                properties = first_feature['properties']
                # Check for different potential zipcode property names
                if 'postalCode' in properties:
                    feature_id_key = "properties.postalCode"
                elif 'ZIPCODE' in properties:
                    feature_id_key = "properties.ZIPCODE"
                elif 'ZIP' in properties:
                    feature_id_key = "properties.ZIP"
                
        fig = px.choropleth_mapbox(
            filtered_df,
            geojson=nyc_geojson,
            locations='zipcode',
            featureidkey=feature_id_key,
            color='hvi',
            color_continuous_scale=color_scale,
            range_color=(1, int(df['hvi'].max() if 'hvi' in df.columns else 5)),
            mapbox_style="carto-positron",
            zoom=9.5,
            center={"lat": 40.7128, "lon": -74.0060},
            opacity=0.7,
            labels={'hvi': 'Heat Vulnerability Index'},
            hover_name='zipcode',
            hover_data={
                'zipcode': True,
                'hvi': True
            }
        )
    except Exception as e:
        st.error(f"Error creating choropleth map: {e}")
        # Fallback to simple scatter plot if choropleth fails
        st.info("Falling back to scatter plot visualization.")
        viz_type = "Scatter Plot with Zip Code Labels"
        
    # Update layout
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        coloraxis_colorbar={
            'title': 'Heat Vulnerability Index',
            'tickvals': [1, 2, 3, 4, 5],
            'ticktext': ['1 (Low)', '2', '3', '4', '5 (High)']
        },
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)
        
elif viz_type == "Heat Map" or (viz_type == "Choropleth Map" and nyc_geojson is None):
    # Create a density heat map using actual NYC zip code locations
    if 'zipcode' in filtered_df.columns:
        # Show notification if this is being used as a fallback
        if viz_type == "Choropleth Map" and nyc_geojson is None:
            st.info("Using heat map as a fallback because GeoJSON data couldn't be loaded.")
        
        # Load NYC zip code centroids data
        with open('nyc_zip_centroids.json', 'r') as f:
            nyc_zip_centroids = json.load(f)
        
        # Function to get lat/long for a zipcode, with a default fallback to central Manhattan
        def get_zip_location(zipcode):
            # Convert to string if it's a number
            zipcode = str(zipcode)
            # Return the known location or a default location in central NYC
            return nyc_zip_centroids.get(zipcode, (40.7128, -74.0060))  # Default to NYC center
        
        # Create multiple points based on heat value for better density visualization
        densified_lats = []
        densified_lons = []
        densified_values = []
        
        for _, row in filtered_df.iterrows():
            zipcode = str(row['zipcode'])
            hvi = row['hvi']
            lat, lon = get_zip_location(zipcode)
            
            # Add multiple points for each zip code based on its HVI value
            # Higher HVI means more points = hotter on the heatmap
            num_points = max(5, hvi * 3)  # At least 5 points, more for higher HVI
            
            # Add slight randomness to the points to create a more natural heat map
            for _ in range(int(num_points)):
                # Add jitter (small random offsets) to spread out the points
                jitter_lat = lat + np.random.normal(0, 0.003)  # ~0.3 km jitter
                jitter_lon = lon + np.random.normal(0, 0.003)
                
                densified_lats.append(jitter_lat)
                densified_lons.append(jitter_lon)
                densified_values.append(hvi)
        
        # Create the heatmap with densified points
        fig = go.Figure(go.Densitymapbox(
            lat=densified_lats,
            lon=densified_lons,
            z=densified_values,
            radius=15,  # Increased radius for better visibility
            colorscale=color_scale,
            zmin=1,
            zmax=int(df['hvi'].max() if 'hvi' in df.columns else 5),
            showscale=True,
            colorbar=dict(
                title='Heat Vulnerability',
                tickvals=[1, 2, 3, 4, 5],
                ticktext=['1 (Low)', '2', '3', '4', '5 (High)']
            )
        ))
        
        fig.update_layout(
            mapbox_style="carto-positron",
            mapbox_center_lat=40.7128,
            mapbox_center_lon=-74.0060,
            mapbox_zoom=10,
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
            height=600
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Heat map data is not available.")

# Add context for the visualization
st.markdown("""
    ### Understanding the Map
    
    This visualization shows the Heat Vulnerability Index (HVI) across NYC zip codes. The HVI shows neighborhoods 
    whose residents are more at risk for dying during and immediately following extreme heat. Neighborhoods are 
    scored from 1 (lowest risk) to 5 (highest risk).
    
    The HVI uses a statistical model to summarize the most important social and environmental factors that 
    contribute to neighborhood heat risk. The factors included in the HVI are:
    - Surface temperature
    - Green space (vegetative cover)
    - Access to home air conditioning
    - Percentage of residents who are low-income
    - Percentage of residents who are non-Latinx Black
    
    Differences in these risk factors across neighborhoods are rooted in past and present racism, according to the NYC Department of Health and Mental Hygiene.
""")

# Add contextual information about heat stress impacts
st.header("Impact of Heat Stress")

st.markdown("""
    ### Health Risks
    
    Extreme heat can lead to:
    - Heat stroke
    - Heat exhaustion
    - Worsening of existing medical conditions
    - Increased mortality rates
    - Disproportionate impacts on vulnerable communities
    
    ### Vulnerable Populations
    
    Those at highest risk include:
    - Low-income residents
    - Non-Latinx Black residents
    - Elderly individuals
    - People with chronic illnesses
    - Those without air conditioning
    - Residents of neighborhoods with less green space
    - Residents of areas with higher surface temperatures
""")

# Add action items
st.markdown("""
    ### Taking Action
    
    Communities can reduce heat vulnerability through:
    - Creating cooling centers in high-risk neighborhoods
    - Increasing green space and tree canopy in areas with high surface temperatures
    - Implementing cool roof programs in neighborhoods with older buildings
    - Improving access to air conditioning for low-income residents
    - Developing targeted heat emergency response plans for the most vulnerable communities
    - Addressing social and economic inequities that contribute to disproportionate heat risk
""")

# Add a humanizing element - personal stories
with st.expander("Community Stories"):
    st.markdown("""
        Wait til I find some sources for personal stories or testimonials from NYC residents affected by heat vulnerability.
    """)



# Data source and methodology
st.markdown("---")
st.markdown("""
    **Data Source:** Heat Vulnerability Index Rankings from NYC Department of Health and Mental Hygiene (DOHMH), last updated September 19, 2024.
    
    **Methodology:** The Heat Vulnerability Index combines social and environmental factors by summing the following factors and assigning them into 5 groups (quintiles):
    
    - **Median Household Income** (American Community Survey 5-year estimate, 2016-2020)
    - **Percent vegetative cover** (trees, shrubs or grass) (2017 LiDAR, NYC DOITT)
    - **Percent of population reported as Non-Hispanic Black** on Census 2020
    - **Average surface temperature** Fahrenheit from ECOSSTRESS thermal imaging, August 27, 2020
    - **Percent of households reporting Air Conditioning access**, Housing and Vacancy Survey, 2017
""")

# Add the ability to download the filtered data
st.download_button(
    label="Download filtered data as CSV",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name='nyc_heat_vulnerability_filtered.csv',
    mime='text/csv',
)
