from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import callbacks

# Load data
df = pd.read_csv("data/typhoon_effects_clean.csv")
# sorted by earliest year first
typhoon_options = (
    df[['Typhoon', 'Year']]
    .dropna()
    .drop_duplicates()
    .sort_values('Year')
    .assign(label=lambda d: d['Year'].astype(int).astype(str) + ' – ' + d['Typhoon'])
)

# Format options for dropdown
typhoons = typhoon_options["Typhoon"].tolist()
typhoon_dropdown_options = [
    {"label": row["label"], "value": row["Typhoon"]}
    for _, row in typhoon_options.iterrows()
]

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

app.layout = dbc.Container([
    # Title
    html.Div(
        [
            html.H1(
                "After the Storm: Mapping Typhoon Damage, Aid, and Loss in the Philippines",
                style={
                    'textAlign': 'center',
                    'color': 'white',
                    'margin': '0',
                    'padding': '20px'
                }
            ),
            html.P(
                "by Malia de Jesus (CS-150)",
                style={
                    'textAlign': 'center',
                    'color': 'white',
                    'margin': '0',
                    'padding': '10px'
                }
            ),
        ],
        style={
            'backgroundColor': '#2c4b83',
            'width': '100%',
            'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.2)',
            'marginBottom': '20px',
        }
    ),

    # Inputs and Map
    dbc.Row([
        # Dropdown, radio buttons, context
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Select a Typhoon:", style={'color': 'gray'}),
                    dcc.Dropdown(
                        id="typhoon-dropdown",
                        options=typhoon_dropdown_options,
                        value=typhoons[0],
                        placeholder="Select a Typhoon",
                        style={
                            'width': '200px',
                            'height': '35px',
                            'fontSize': '14px',
                            'padding': '2px 8px',
                            'marginBottom': '20px'
                        }
                    ),

                    html.H5("Choose a Metric:", style={'color': 'gray', 'marginBottom': '10px'}),
                    dcc.RadioItems(
                        id="metric-radio",
                        options=[
                            {"label": "Deaths", "value": "Persons_Dead"},
                            {"label": "Total People Affected", "value": "Persons_Affected"},
                            {"label": "Evacuation Centers", "value": "ECs"},
                            {"label": "Displaced People (in ECs)", "value": "CUM_In_Persons"},
                            {"label": "Displaced People (out ECs)", "value": "CUM_Out_Persons"},
                            {"label": "Relief Aid (PHP)", "value": "Total_Assist"},
                        ],
                        value="Persons_Dead",
                        labelStyle={'display': 'block', 'marginBottom': '8px'},
                        style={'color': 'gray'},
                    )
                ])
            ], className="mb-4"),

            dbc.Card([
                dbc.CardBody([
                    html.H5("Typhoon Context", className="card-title", style={'color': 'gray'}),
                    html.Div(id="typhoon-context", style={
                        "color": "gray",
                        "height": "100%",
                        "overflowY": "auto"
                    })
                ])
            ], style={"height": "370px"}),
        ]),

            # Right column: Map
        dbc.Col([
            dcc.Graph(
                id="choropleth-map",
                style={"height": "700px", "marginTop": "40px", "marginLeft": "-20px"}
            )
        ], width=9)
    ], className="mb-4"),

    # Bar chart
    dcc.Graph(id="bar-chart"),
    html.Footer([
        html.P("Data Sources:", style={"color": "white", "fontWeight": "bold"}),
        html.Ul([
            html.Li(html.A("NDRRMC Reports", href="https://ndrrmc.gov.ph/", target="_blank", style={"color": "white"})),
            html.Li(html.A("DROMIC Reports (DSWD)", href="https://dromic.dswd.gov.ph/", target="_blank",
                           style={"color": "white"})),
        ], style={"listStyleType": "none", "padding": "0"})
    ],
        style={
            "backgroundColor": "#2c4b83",
            "padding": "20px",
            "marginTop": "40px",
            "textAlign": "center"
        }),
], fluid=True),

callbacks.register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)
