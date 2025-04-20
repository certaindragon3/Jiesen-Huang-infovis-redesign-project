## Visualization Replicate Manual for non-code Users

This guide provides instructions for non-technical users to access the interactive NYC Heat Vulnerability map or create a similar visualization using the data.

**Goal:** To explore heat vulnerability patterns in NYC without needing to install software or write code.
### Option 1: Use the Live Interactive Web Application (Recommended & Easiest)

Your interactive visualization is already available online! This is the best way to experience the full functionality without any setup.

1. Access the App: Open a web browser and go to this URL:
    
    https://certaindragon3-jiesen-huang-infovis-redesign-project-app-yglh1o.streamlit.app
    
2. **Interact with the Map:**
    
    - **Controls:** Use the controls in the sidebar on the left to customize the view:
        - **Filter by Vulnerability Index Range:** Adjust the slider to focus on areas with specific HVI scores (1=Low Risk, 5=High Risk).
        - **Visualization Type:** Choose between "Choropleth Map" (colored zip code areas) and "Heat Map" (density-based coloring).
        - **Color Scale:** Select different color schemes for the map.
    - **Explore Data:** Hover over map areas (in Choropleth view) to see the Zip Code and HVI score.
    - **Learn More:** Read the explanations about Heat Vulnerability, data sources, and community stories provided in the app.
    - **Download Data:** Use the download button at the bottom of the sidebar to get the filtered data as a CSV file.
3. **Data Source:** This application visualizes the Heat Vulnerability Index (HVI) data provided by the NYC Department of Health and Mental Hygiene (DOHMH) via NYC Open Data.

**Advantages:**

- No installation required.
- Access to the full, intended functionality and interactivity.
- Always uses the intended data and calculations.

**Disadvantages:**

- Requires an internet connection. (With Access to International Internet)
- You cannot modify the underlying visualization code directly (only interact via controls).

### Option 2: Create a Similar Map using a No-Code Tool (Advanced - Requires Manual Setup)

If you want to try creating a _similar_ map visualization yourself using the source data without writing code, you can use online tools like Plotly Chart Studio or Tableau Public. This requires more effort and won't be an exact replica of the Streamlit application.

**General Steps (using Plotly Chart Studio as an example):**

1. **Get the Data:** You need two files:
    - **HVI Data:** `Heat_Vulnerability_Index_Rankings_20250406.csv` (or the latest version from NYC Open Data). This contains Zip Codes and their HVI scores.
    - **Geographic Boundaries:** `GeoJSON.json`. This file defines the shapes (polygons) of the NYC zip code areas needed for the choropleth map. _(Note: You would need to obtain this specific GeoJSON file used in the original project)._
2. **Sign Up/In:** Go to a platform like Plotly Chart Studio ([https://chart-studio.plotly.com/](https://chart-studio.plotly.com/)) and create a free account or sign in.
3. **Upload Data:** Use the platform's interface to upload your CSV data file.
4. **Create Chart:**
    - Select 'Create' > 'Chart'.
    - Choose 'Map' as the chart type. Select 'Choropleth'.
5. **Configure the Map:**
    - **Link Data to Geography:** You will need to specify:
        - The column in your CSV containing the location identifiers (e.g., `zipcode`).
        - The GeoJSON file containing the shapes and specify the corresponding identifier within the GeoJSON (e.g., `properties.ZCTA5CE10` or similar, depending on the file).
        - The column containing the data values to plot (e.g., `hvi`).
    - **Customize Appearance:** Set the color scale, map style (e.g., base map), title, legend, etc.
6. **Save and Share:** Save your map within the platform.

**Advantages:**

- Allows creating a map without writing code.
- You can use your own data if desired.

**Disadvantages:**

- Requires manually finding and uploading the correct data files (CSV and GeoJSON).
- Requires learning the specific GUI tool's interface.
- Will not replicate the exact appearance, interactivity (like sidebar controls, hover effects), or layout of the original Streamlit app.
- Heatmap/Density map creation might be more complex or unavailable depending on the tool.
