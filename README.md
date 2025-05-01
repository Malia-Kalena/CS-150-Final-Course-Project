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

## Context
Natural disasters are a recurring and devastating reality in the Philippines. Typhoons
affect millions each year, but not all regions experience the same level of damage,
nor receive the same attention or support. This project was inspired by the Filipino
tradition of sending *balikbayan boxes*—care packages sent home by those abroad—and
aims to connect personal experiences of giving with data that shows where help is most
needed.

The project includes six typhoons chosen for their geographic diversity, historical
significance, and data availability:

- **Sendong (2011)** – Earliest storm in dataset; limited relief data available
- **Pablo (2012)** – Heavy Mindanao impact; shows regional inequality
- **Yolanda (2013)** – Deadliest storm in PH history; major Visayas impact
- **Odette (2021)** – Most recent storm; strong EC and aid data, but no death data
- **Ulysses (2020)** – Severe urban flooding during COVID; no regional death data
- **Rolly (2020)** – Strongest storm globally in 2020; pandemic-era response

## Data Visualization
The dashboard consists of three main components:

### 1. Choropleth Map
- Displays regional values for the selected metric (deaths, displaced, aid, etc.)
- Dropdown and radio buttons allow users to explore different storms and metrics
- Custom color scale shows missing data in gray

### 2. Bar Chart
- Ranks regions by the selected metric
- Bars include numeric labels and consistent styling

### 3. Context Card
- Dynamically updates with background information about the selected typhoon
- Provides interpretation and explains missing or incomplete data

## Data Source
- Data was curated from publicly available **DROMIC (Disaster Response Operations Monitoring and Information Center)** reports
- For storms before Yolanda (e.g., **Sendong** and **Pablo**), information was cross-referenced with **NDRRMC (National Disaster Risk Reduction and Management Council)** situation reports to supplement missing fields
- Region names were standardized to match the JSON region boundaries
- Missing data was filled with 0 and explicitly marked in hover text where appropriate

While the dataset contains gaps—especially in earlier storms—these inconsistencies help highlight the evolution of
disaster reporting in the Philippines and the unequal visibility of certain regions and metrics.

## Design Choices*
- **Effective Visuals** - Choropleth maps and bar charts make regional patterns easy to understand.
- **Minimal Clutter** - Clean layout, custom hover text, and clear labels help users focus on what matters.
- **Interactive Design** - Users can explore the data by typhoon and metric, inviting reflection and discovery.
- **Narrative Framing** - Context cards explain the human side of the data, highlighting regional inequality and community response.
- **Choose an effective visual** – Maps and bar charts chosen for clarity and regional comparison

