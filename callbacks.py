import json
from dash import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# Load once for use in all callbacks
df = pd.read_csv("data/typhoon_effects_clean.csv")
with open("data/ph.json") as f:
    region_geojson = json.load(f)

region_name_map = {
    'I': 'Ilocos',
    'II': 'Cagayan Valley',
    'III': 'Central Luzon',
    'IV-A': 'Calabarzon',
    'IV-B': 'Mimaropa',
    'V': 'Bicol',
    'VI': 'Western Visayas',
    'VII': 'Central Visayas',
    'VIII': 'Eastern Visayas',
    'IX': 'Zamboanga Peninsula',
    'X': 'Northern Mindanao',
    'XI': 'Davao',
    'XII': 'Soccsksargen',
    'CARAGA': 'Caraga',
    'ARMM': 'Autonomous Region in Muslim Mindanao',
    'NCR': 'National Capital Region'
}

metric_labels = {
    "Persons_Dead": "Deaths",
    "Persons_Affected": "Persons Affected",
    "ECs": "Evacuation Centers",
    "CUM_In_Persons": "Cumulative Displaced Inside ECs",
    "CUM_Out_Persons": "Cumulative Displaced Outside ECs",
    "Total_Assist": "Relief Aid (PHP)"
}

typhoon_context = {
    "Yolanda": "Yolanda (2013) — Deadliest storm in Philippine history. Major impact across the Visayas, especially Region VIII. While billions in relief aid were distributed, official regional-level data is not included due to fragmented reporting and lack of standardized tracking at the time. Highlights the need for improved transparency in post-disaster response.",
    "Odette": "Odette (2021) — Most recent storm in the dataset. Severely affected Visayas and Caraga during the COVID-19 pandemic. While regional death data is unavailable, Odette provides detailed displacement and relief aid records, offering valuable insight into how disaster response evolved in underrepresented regions and under pandemic constraints.",
    "Ulysses": "Ulysses (2020) — Caused severe flooding across NCR and Region II during the COVID-19 pandemic. Deaths were reported nationally, but no regional breakdown is included in this dataset. Highlights how urban density and strained pandemic response infrastructure shaped displacement and aid efforts.",
    "Rolly": "Rolly (2020) — One of the most powerful typhoons globally that year. Occurred during the COVID-19 pandemic, which complicated evacuation and reporting efforts. Over 20 deaths were recorded nationally, but no regional breakdown is included in this dataset. Strong displacement and aid patterns observed in the Bicol Region.",
    "Sendong": "Sendong (2011) — Earliest storm in dataset. Over 1,000 deaths reported. No regional relief data available due to limited disaster reporting systems at the time.",
    "Pablo": "Pablo (2012) — Severely affected the Davao Region in Mindanao. While data is available for all metrics, the impact underscored regional vulnerabilities and raised awareness about Mindanao’s historical underrepresentation in national disaster planning."
}

def register_callbacks(app):
    @app.callback(
        Output("choropleth-map", "figure"),
        Output("bar-chart", "figure"),
        Output("typhoon-context", "children"),
        Input("typhoon-dropdown", "value"),
        Input("metric-radio", "value")
    )
    def update_visuals(selected_typhoon, selected_metric):
        dff = df[df["Typhoon"] == selected_typhoon].copy()
        dff["Region_Full"] = dff["Region"].map(region_name_map)
        dff["missing_data"] = dff[selected_metric].isna()
        dff[selected_metric] = dff[selected_metric].fillna(0)

        dff["tooltip"] = dff.apply(
            lambda row: f"{row['Region_Full']}: No data reported"
            if row["missing_data"]
            else f"{row['Region_Full']}: {row[selected_metric]:,.0f}",
            axis=1
        )

        custom_colorscale = [
            [0.0, "#d3d3d3"],
            [0.00001, "#fff5f0"],
            [0.2, "#fcbba1"],
            [0.4, "#fc9272"],
            [0.6, "#fb6a4a"],
            [0.8, "#de2d26"],
            [1.0, "#a50f15"]
        ]

        map_title = f"{metric_labels[selected_metric]} by Region – Typhoon {selected_typhoon}"

        if dff[selected_metric].sum() == 0:
            fig_map = go.Figure()
            fig_map.update_layout(
                title="No available data to display for this metric and typhoon.",
                title_font=dict(color="gray"),
                showlegend=False,
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                geo=dict(visible=False),
                margin={"r": 0, "t": 60, "l": 0, "b": 0},
                paper_bgcolor="white",
                plot_bgcolor="white",
                height=700
            )

        else:
            fig_map = px.choropleth(
                dff,
                geojson=region_geojson,
                featureidkey="properties.name",
                locations="Region_Full",
                color=selected_metric,
                color_continuous_scale=custom_colorscale,
                title=map_title,
                labels = {selected_metric: metric_labels[selected_metric]}
            )
            fig_map.update_traces(
                hovertemplate="<b>%{location}</b><br>" + metric_labels[selected_metric] + ": %{z:,.0f}<extra></extra>",
                colorbar_title=metric_labels[selected_metric]  # 👈 this is the fix
            )
            fig_map.update_geos(
                visible=False,
                projection_type="mercator",
                center={"lat": 12.8797, "lon": 121.7740},
                lataxis_range=[4, 22],
                lonaxis_range=[116, 127]
            )
            fig_map.update_layout(mapbox_style="carto-positron", margin={"r": 0, "t": 30, "l": 0, "b": 0})

        bar_df = dff[dff[selected_metric] > 0]

        if bar_df.empty:
            fig_bar = go.Figure()
            fig_bar.update_layout(
                title="No bar chart data available.",
                title_font=dict(color="gray"),
                showlegend=False,
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                margin={"r": 0, "t": 60, "l": 0, "b": 0},
                paper_bgcolor="white",
                plot_bgcolor="white",
                height=400
            )
        else:
            fig_bar = px.bar(
                bar_df.sort_values(by=selected_metric, ascending=False),
                x="Region_Full",
                y=selected_metric,
                title=f"{metric_labels[selected_metric]} - {selected_typhoon}",
                labels={selected_metric: metric_labels[selected_metric], "Region_Full": "Region"},
            )
            fig_bar.update_traces(
                marker_color="#2c4b83",
                texttemplate='%{y:,.0f}',
                textposition='outside',
                hovertemplate='<b>%{x}</b><br>' + metric_labels[selected_metric] + ': %{y:,.0f}<extra></extra>'
            )
            fig_bar.update_layout(
                plot_bgcolor='white',
                paper_bgcolor='white',
                font=dict(color='black'),
                margin={"r": 20, "t": 50, "l": 20, "b": 80},
                height=500,
            )

        context = typhoon_context.get(selected_typhoon, "No additional context provided.")

        return fig_map, fig_bar, context
