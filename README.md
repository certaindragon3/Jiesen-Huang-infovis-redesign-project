# NYC Heat Vulnerability Index Visualization

## Project Overview

This interactive web application visualizes the Heat Vulnerability Index (HVI) across New York City zip codes, providing insights into neighborhoods that face disproportionate risk during extreme heat events. The visualization helps identify areas where resources and interventions are most needed to protect vulnerable populations from heat-related health impacts.

The Heat Vulnerability Index (HVI) shows neighborhoods whose residents are more at risk for dying during and immediately following extreme heat. It uses a statistical model to summarize important social and environmental factors that contribute to neighborhood heat risk. Neighborhoods are scored from 1 (lowest risk) to 5 (highest risk).

## Contribution to Sustainable Development Goals (SDGs)

This project contributes to the United Nations Sustainable Development Goals (SDGs) by addressing urban climate resilience and public health:

SDG 11: Sustainable Cities and Communities: By visualizing heat vulnerability at a local level, this tool helps urban planners and communities identify areas needing climate adaptation measures (like cooling centers and green spaces) to build more resilient cities.

<div style="text-align: center;">
  <img src="./SDG_Logo/E_WEB_11.png"  style="width: 25%; display: inline-block; vertical-align: middle;">
</div>

SDG 3: Good Health and Well-being: The visualization highlights populations and areas most vulnerable to heat-related health risks, supporting targeted public health interventions to protect residents and improve well-being during extreme heat events.

<div style="text-align: center;">
  <img src="./SDG_Logo/E_WEB_03.png"  style="width: 25%; display: inline-block; vertical-align: middle;">
</div>

Through better data visualization and accessibility, this project supports efforts to create healthier, safer, and more sustainable urban environments.

## Future Research Directions

Inspired by observations from the Zhouzhuang Mystery of Life Museum field trip and the potential of visualization to address complex societal challenges, this project opens several avenues for future research and development, particularly bridging digital humanities, biodiversity, and community-based learning:

* **Integrating Biodiversity Data:** Explore incorporating biodiversity datasets into the visualization. This could involve mapping species distribution, habitat vulnerability, or the impact of environmental factors (like heat) on local ecosystems. Visualizing biodiversity alongside human vulnerability could highlight interconnectedness and inform conservation or urban planning efforts. The museum's approach to comparing different biological subjects  provides a model for presenting diverse life data clearly.

![![jpg_src/IMG_1622.jpeg](jpg_src/IMG_1622.jpeg)](./jpg_src/IMG_1622.jpg)

* **Digital Humanities Approaches to Environmental Storytelling:** Develop narrative-driven visualizations that use digital humanities tools and techniques to tell stories about climate change impacts, urban ecology, or community resilience. Drawing inspiration from the museum's scientific storytelling, these visualizations could incorporate historical data, personal narratives, or cultural contexts to create a more engaging and affectively resonant understanding of environmental issues.

* **Community-Based Participatory Design:** Implement methodologies for co-designing visualizations with vulnerable communities. This would involve working directly with residents to understand their information needs, incorporate local knowledge, and ensure the visualization is a relevant and empowering tool for action and advocacy. The ethical considerations highlighted by the museum's exhibits  underscore the importance of such collaborative and community-centered approaches.
  
* **Visualizing Affective Dimensions of Environmental Issues:** Further explore how visualization can effectively communicate the affective aspects of environmental challenges, such as the stress of extreme heat or the emotional connection to local biodiversity. Building on the reflections of scientific storytelling and aesthetics from the museum trip, this could involve developing visual encodings or interactive features that acknowledge and model affective responses, moving beyond purely cognitive data presentation.
  
* **Developing Open Educational Resources:** Transform the visualization and underlying data into educational resources for community-based learning initiatives or K-12 education. This could involve creating interactive modules, lesson plans, or simplified interfaces that make complex concepts about heat vulnerability, urban environment, and biodiversity accessible to a wider audience, using clear and intuitive visual communication principles learned from analyzing museum exhibits.

These directions aim to extend the project's impact by leveraging visualization not just as a tool for data display, but as a catalyst for interdisciplinary research, public engagement, and informed action in the context of pressing environmental and social issues.

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
- **NumPy**: Supports numerical operations and data transformation, generating small random jitter around each zip code's centroid to create a natural-looking heatmap

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

## Acknowledgments

I would like to thank several contributors and organizations whose insights and resources significantly enhanced this project:

- **Dongping Liu**: Provided critical insights during the Digital Technology for Sustainability Symposium at Duke Kunshan University, significantly improving the project's technical approach.
- **Prof. Luyao Zhang**: Facilitated the symposium and offered valuable academic perspectives that guided my understanding and approach.
- **NYC Department of Health and Mental Hygiene**: Provided essential data and resources, making this visualization possible.
- **NYC Open Data Team**: Supported access and utilization of critical datasets.
- **Streamlit, Plotly, Pandas, and NumPy Developers**: Their excellent libraries made the development of this application feasible and efficient.
- **Classmates and Symposium Participants**: Their collaborative feedback, questions, and discussions greatly enriched the project.

## References

- NYC Department of Health and Mental Hygiene. (2024). Heat Vulnerability Index Rankings. NYC Open Data.
- U.S. Census Bureau. (2020). ZIP Code Tabulation Areas (ZCTAs).
- NYC Environmental & Health Data Portal - Heat Vulnerability Explorer

## License

This project is licensed under the MIT License - see the LICENSE file for details.

