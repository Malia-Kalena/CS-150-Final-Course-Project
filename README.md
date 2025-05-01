# After the Storm: Mapping Typhoon Damage, Aid, and Loss in the Philippines
**Author:** Malia de Jesus\
**Course:** CS-150 Community Action Computing

## Thesis Statement
This project explores how typhoons have impacted different regions of the Philippines
by visualizing deaths, displacement, and relief aid across six major storms. Using
interactive maps and charts, the project highlights how natural disaster outcomes
and responses vary across geography and time. It also reflects on the limitations
of official data and uplifts the Filipino value of *bayanihan*—the spirit of community
solidarity and mutual aid.

## Context and Motivation
Natural disasters are a recurring and devastating reality in the Philippines. Typhoons
affect millions each year, but not all regions experience the same level of damage,
nor receive the same attention or support. This project was inspired by the Filipino
tradition of sending *balikbayan boxes*—care packages sent home by Filipinos living abroad. These
symbolic gestures are more than gifts; they are acts of love and solidarity in times of crisis. This visualization connects personal experiences of giving with national data to highlight where help is needed most and how the community responds.

## Typhoons Featured
Each storm was chosen for is geographic diversity, historical importance, and data availability:

- **Sendong (2011)** – Earliest storm in dataset; limited relief data available due to limited disaster reporting systems at the time
- **Pablo (2012)** – Heavy Mindanao impact; shows regional inequality and underrepresentation in national disaster planning.
- **Yolanda (2013)** – Deadliest storm in PH history; major Visayas impact; billions in relief aid distributed, but official regional-level data is not included due to fragmented reporting. Highlights the need for improved transperency in post-disaster response
- **Rolly (2020)** – Strongest storm globally in 2020 during COV; pandemic-era response; no regional death data available.
- **Ulysses (2020)** – Severe urban flooding during COVID across Metro Manila region; highlights how urban density and strained pandemic response infrastructure shape displacement and aid efforts; no regional death data available
- **Odette (2021)** – Most recent storm in dataset; gives insight into how disaster response evolved in underrepresented region; no regional death data available
  
## Dashboard Features
The dashboard consists of three main components:

### 1. Choropleth Map
- Displays regional values for the selected metric (deaths, displaced, aid, etc.)
- Dropdown and radio buttons allow users to explore different storms and metrics
- Custom color scale highlights severity; shows missing data in gray

### 2. Bar Chart
- Ranks regions by the selected metric
- Bars include numeric labels and consistent styling for easy comparison

### 3. Context Card
- Dynamically updates with background information about the selected typhoon
- Provides interpretation and explains missing or incomplete data

## Data Source
- Data was curated from publicly available **DROMIC (Disaster Response Operations Monitoring and Information Center)** reports
- For storms before Yolanda (e.g., **Sendong** and **Pablo**), information was cross-referenced with **NDRRMC (National Disaster Risk Reduction and Management Council)** situation reports to supplement missing fields
- Region names were standardized to match the JSON region boundaries
- Missing data was filled with 0 and explicitly marked in hover text where appropriate

While the dataset contains gaps—especially in earlier storms—these inconsistencies help highlight the evolution of disaster reporting in the Philippines and the unequal visibility of certain regions and metrics.

This project uses publicly available and government-sourced reports:
- [NDRRMC Situation Reports (National Disaster Risk Reduction and Management Council)](https://ndrrmc.gov.ph/)
- [DROMIC Reports by the Department of Social Welfare and Development (DSWD)](https://dromic.dswd.gov.ph/)

## Design Choices
- **Effective Visuals** - Choropleth maps and bar charts make regional patterns easy to understand.
- **Minimal Clutter** - Clean layout, custom hover text, and clear labels help users focus on what matters.
- **Interactive Design** - Users can explore the data by typhoon and metric, inviting reflection and discovery.
- **Narrative Framing** - Context cards explain the human side of the data, highlighting regional inequality and community response.
