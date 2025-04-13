# NYC Heat Vulnerability Index Visualization

## Project Overview

This interactive web application visualizes the Heat Vulnerability Index (HVI) across New York City zip codes, providing insights into neighborhoods that face disproportionate risk during extreme heat events. The visualization helps identify areas where resources and interventions are most needed to protect vulnerable populations from heat-related health impacts.

The Heat Vulnerability Index (HVI) shows neighborhoods whose residents are more at risk for dying during and immediately following extreme heat. It uses a statistical model to summarize important social and environmental factors that contribute to neighborhood heat risk. Neighborhoods are scored from 1 (lowest risk) to 5 (highest risk).

## Data Source and Methodology

The Heat Vulnerability Index data is provided by the NYC Department of Health and Mental Hygiene (DOHMH). The index combines several key factors:

- Surface temperature
- Green space (vegetative cover)
- Access to home air conditioning
- Percentage of residents who are low-income
- Percentage of residents who are non-Latinx Black

These factors were selected based on research showing their strong association with heat-related mortality. The HVI methodology recognizes that differences in these risk factors across neighborhoods are rooted in past and present structural inequities.

## Features

- **Interactive Choropleth Map**: Visualize heat vulnerability by zip code with an intuitive color gradient
- **Heat Map View**: See density-based visualization of vulnerability hot spots
- **Filtering Options**: Focus on areas with specific vulnerability levels
- **Color Scale Selection**: Choose different color schemes to highlight patterns
- **Responsive Design**: Works on desktop and mobile devices
- **Contextual Information**: Detailed explanations of heat vulnerability factors and impacts

## Python Packages Used

This application leverages several Python libraries:

- **Streamlit**: Powers the interactive web application framework
- **Plotly**: Creates interactive choropleth and heat maps
- **Pandas**: Handles data processing and manipulation
- **NumPy**: Supports numerical operations and data transformation，to generate small random jitter around each zip code's centroid by sampling from a normal distribution, creating a more natural-looking heatmap.

## Data Sources

### Heat Vulnerability Index Data
- **Source**: NYC Department of Health and Mental Hygiene (DOHMH)
- **Format**: CSV file with zip codes and vulnerability scores
- **Last Updated**: September 19, 2024

### Geospatial Data

#### GeoJSON Boundary Data
The application uses a locally copied GeoJSON file from the NYC Department of Health repository. This file contains the polygon boundaries for NYC zip codes needed to create the choropleth map.

Alternative GeoJSON sources (used as fallbacks if needed):
- [NYC Open Data Portal](https://data.cityofnewyork.us/Health/Modified-Zip-Code-Tabulation-Areas-MODZCTA-/pri4-ifjk)

#### Zip Code Centroid Data
For the heat map visualization, the application uses a database of NYC zip code centroids (geographical center points). These centroids were compiled from:

- [US Census Bureau ZIP Code Tabulation Areas (ZCTAs)](https://www.census.gov/programs-surveys/geography/technical-documentation/records-layout/2020-zcta-record-layout.html)

## Installation and Usage

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```
   streamlit run app.py
   ```

You can also access the deployed web version at: https://certaindragon3-jiesen-huang-infovis-redesign-project-app-yglh1o.streamlit.app

## Future Improvements

- Add time-series data to show changes in vulnerability over time
- Incorporate additional environmental data layers (tree canopy, surface temperature)
- Add demographic overlays to explore correlations with social factors
- Implement address search functionality
- Include links to heat-related resources by neighborhood

## References

- NYC Department of Health and Mental Hygiene. (2024). Heat Vulnerability Index Rankings. NYC Open Data.
- U.S. Census Bureau. (2020). ZIP Code Tabulation Areas (ZCTAs).
- NYC Environmental & Health Data Portal - Heat Vulnerability Explorer

## License

This project is licensed under the MIT License - see the LICENSE file for details.
